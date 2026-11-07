#!/usr/bin/env python3
"""Static structure-risk checks for Chinese research reports; not a comprehension test."""
import argparse
from html.parser import HTMLParser
import json
import re
import sys

TOC_META = ('查证进度', '本报告', '怎么写', '写作说明', '进度')
DENY_HINTS = ('登记', '窜改', '调参', '配置A', '配置B', '配置 A', '配置 B', 'K1', 'K2', 'S3', 'B2a', 'B2b', 'B7a', 'B7b', 'ICE')
DISCLAIM = re.compile(r'(这不是|本文没有|本文不|并不代表|不代表|不主张|无意)')
PROCESS = re.compile(r'(预先写|预先登记|追加设置|追加的|事后补|事后加|独立复核|复核者|先例检索有效|检索结果只在|有效期|公平网格|按预先|第\s*\d+\s*轮复核|已逐条披露)')
ARABIC_NUMBER = re.compile(r'(?<![A-Za-z0-9])[-+]?\d+(?:\s*/\s*\d+|\.\d+)?\s*[%％]?(?![A-Za-z0-9])')
CJK_NUMBER = re.compile(r'(?<![零〇一二三四五六七八九十百千万两])(?:[零〇一二三四五六七八九十百千万两]+)(?=(?:人|次|天|小时|分钟|秒|年|月|日|件|个|篇|倍|%|％|元|美元))')
VALUE_UNIT = re.compile(r'(?:%|％|百分比|百分点|(?:\d|[零〇一二三四五六七八九十百千万两])\s*(?:人|次|天|小时|分钟|秒|年|月|日|件|个|篇|倍|元|美元|公里|米|毫秒|分))', re.I)
HEADER_UNIT = re.compile(r'(?:%|％|百分比|百分点|[（(]\s*(?:人|人次|次|天|小时|分钟|秒|年|月|日|件|个|篇|倍|元|美元|公里|米|毫秒|分|ms|s|sec|min|h|hr|day|year|USD|EUR|km|m)\s*[）)]|单位\s*(?:[:：=]|为|是)\s*(?:人|人次|次|天|小时|分钟|秒|年|月|日|件|个|篇|倍|元|美元|公里|米|毫秒|分))', re.I)
DIRECTION = re.compile(r'(?:越\s*(?:高|低|大|小)|更\s*(?:高|低|大|小)|↑|↓|\b(?:up|down)\b)', re.I)
DESCRIPTIVE = re.compile(r'(?:样本数|人数|受试者数|时间|时长|耗时|持续时间|年份|出版年|发布年|日期|年月|年龄|编号|序号|轮次|文献年份|周期|次数)')
NUMERIC_HEADER = re.compile(r'(?:准确率|准确性|误差|得分|分数|评分|比例|占比|成功率|失败率|召回率|精确率|命中率|成本|指标|表现评价)', re.I)
NOTE_PREFIX = re.compile(r'^(?:表注|注|备注|note)\s*[:：.]', re.I)
APPENDIX = re.compile(r'^(?:附录?|我们可能错了)(?:\s|[:：]|$)')
VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
BLOCKED = {'script','style','template'}


def is_number(value):
    return bool(ARABIC_NUMBER.search(value) or CJK_NUMBER.search(value))


def cell_has_unit(value):
    return bool(VALUE_UNIT.search(value))


def header_has_unit(value):
    return bool(HEADER_UNIT.search(value))


def unit_token(value):
    m = HEADER_UNIT.search(value) or VALUE_UNIT.search(value)
    return m.group(0).strip() if m else ''


def visible_text(value):
    return re.sub(r'\s+', ' ', value).strip()


class VisibleHTML(HTMLParser):
    """Collect static visible headings, paragraphs and table structure."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.events = []
        self.tables = []
        self.unsupported = []
        self.excluded = {'script': 0, 'style': 0, 'template': 0, 'hidden': 0, 'comments': 0}
        self.blocked = []
        self.captures = []
        self.table_stack = []
        self.current_heading = None
        self.current_paragraph = None
        self.dynamic_script = False

    def _location(self):
        line, col = self.getpos()
        return 'line %d, column %d' % (line, col + 1)

    def _hidden(self, attrs):
        a = dict(attrs)
        if 'hidden' in a or str(a.get('aria-hidden', '')).lower() == 'true':
            return True
        style = re.sub(r'\s+', '', str(a.get('style', '')).lower())
        return 'display:none' in style or 'visibility:hidden' in style

    def handle_comment(self, data):
        self.excluded['comments'] += 1

    def handle_decl(self, decl):
        pass

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if self.blocked:
            if tag not in VOID:
                self.blocked.append(tag)
            return
        if tag in BLOCKED or self._hidden(attrs):
            if tag in BLOCKED:
                self.excluded[tag] += 1
                if tag == 'script':
                    self.dynamic_script = True
            else:
                self.excluded['hidden'] += 1
            if tag not in VOID:
                self.blocked.append(tag)
            return
        if tag in ('h1','h2','h3','h4','h5','h6'):
            self.current_heading = {'type':'heading', 'level':int(tag[1]), 'text':'', 'location':self._location()}
            self.captures.append(('heading', self.current_heading))
            return
        if tag == 'p' and not self.table_stack:
            self.current_paragraph = {'type':'paragraph', 'text':'', 'location':self._location()}
            self.captures.append(('paragraph', self.current_paragraph))
            return
        if tag == 'table':
            parent = self.table_stack[-1] if self.table_stack else None
            record = {'format':'html', 'location':self._location(), 'title':'', 'caption':'', 'note':'',
                      'headers':[], 'rows':[], 'sections':[], 'unsupported':[], 'table_attrs':dict(attrs),
                      'nested': parent is not None, '_header_rows':[], '_row':None, '_group':'table', '_caption':None}
            if parent:
                parent['unsupported'].append('嵌套表格结构需人工核验')
                record['unsupported'].append('嵌套表格结构需人工核验')
            self.tables.append(record)
            self.events.append({'type':'table', 'record':record})
            self.table_stack.append(record)
            return
        if not self.table_stack:
            return
        table = self.table_stack[-1]
        if tag in ('thead','tbody','tfoot'):
            table['_group'] = tag
            table['sections'].append({'section':tag, 'location':self._location()})
        elif tag == 'caption':
            target = {'text':''}
            table['_caption'] = target
            self.captures.append(('caption', target))
        elif tag == 'tr':
            table['_row'] = {'cells':[], 'section':table['_group'], 'location':self._location()}
            table['rows'].append(table['_row'])
        elif tag in ('th','td') and table['_row'] is not None:
            cell = {'text':'', 'tag':tag, 'attrs':dict(attrs)}
            table['_row']['cells'].append(cell)
            self.captures.append(('cell', cell))
            span = dict(attrs).get('colspan') or dict(attrs).get('rowspan')
            if span and str(span) != '1':
                table['unsupported'].append('rowspan/colspan 合并单元格需人工核验')

    def handle_endtag(self, tag):
        tag = tag.lower()
        if self.blocked:
            if tag in self.blocked:
                index = len(self.blocked) - 1 - self.blocked[::-1].index(tag)
                del self.blocked[index:]
            return
        if tag in ('h1','h2','h3','h4','h5','h6') and self.current_heading is not None:
            self.current_heading['text'] = visible_text(self.current_heading['text'])
            self.events.append(self.current_heading)
            self.current_heading = None
            if self.captures and self.captures[-1][0] == 'heading': self.captures.pop()
            return
        if tag == 'p' and self.current_paragraph is not None:
            self.current_paragraph['text'] = visible_text(self.current_paragraph['text'])
            if self.current_paragraph['text']:
                self.events.append(self.current_paragraph)
            self.current_paragraph = None
            if self.captures and self.captures[-1][0] == 'paragraph': self.captures.pop()
            return
        if not self.table_stack:
            return
        table = self.table_stack[-1]
        if tag == 'caption':
            if table['_caption']:
                table['caption'] = visible_text(table['_caption']['text'])
                if self.captures and self.captures[-1][0] == 'caption': self.captures.pop()
                table['_caption'] = None
        elif tag in ('th','td'):
            if self.captures and self.captures[-1][0] == 'cell': self.captures.pop()
        elif tag == 'tr':
            table['_row'] = None
        elif tag == 'table':
            self.table_stack.pop()

    def handle_data(self, data):
        if self.blocked or not data.strip():
            return
        if self.captures:
            kind, target = self.captures[-1]
            if kind in ('heading','paragraph','caption','cell'):
                target['text'] += data
        elif not self.table_stack:
            self.events.append({'type':'text','text':visible_text(data),'location':self._location()})

    def finish(self):
        for table in self.tables:
            rows = table['rows']
            if not rows:
                table['unsupported'].append('未发现可解析的表格行/表体，需人工核验')
                continue
            thead_indices = [i for i, row in enumerate(rows) if row['section'] == 'thead']
            if thead_indices:
                initial = thead_indices
            else:
                initial = []
                for i, row in enumerate(rows):
                    pure_column_header = bool(row['cells']) and all(
                        cell['tag'] == 'th' and str(cell['attrs'].get('scope', 'col')).lower() != 'row'
                        for cell in row['cells'])
                    if pure_column_header and not initial:
                        initial.append(i)
                    elif pure_column_header and initial and i == initial[-1] + 1:
                        initial.append(i)
                    else:
                        break
            if not initial:
                table['unsupported'].append('未发现可确认的列标题；行首 th scope=row 保留为数据标签，列含义需人工核验')
            if len(initial) > 1:
                table['unsupported'].append('多行/多层表头需人工核验')
            table['_header_rows'] = initial
            if initial:
                table['headers'] = [visible_text(cell['text']) for i in initial for cell in rows[i]['cells']]
            else:
                width = max((len(row['cells']) for row in rows if row['section'] != 'tfoot'), default=0)
                table['headers'] = [''] * width
            table['section_rows'] = [{'section':row['section'],'location':row['location'],'cells':[visible_text(cell['text']) for cell in row['cells']], 'cell_metadata':[{'tag':cell['tag'],'scope':cell['attrs'].get('scope')} for cell in row['cells']]} for row in rows]
            table['body_rows'] = [row for i, row in enumerate(rows) if i not in initial and row['section'] != 'tfoot']
            expected = len(table['headers'])
            for row in rows:
                if len(row['cells']) != expected:
                    table['unsupported'].append('行列数与表头不齐，需人工核验（%s）' % row['location'])
                    break
            table['rows'] = [[visible_text(cell['text']) for cell in row['cells']] for row in table['body_rows']]
            for row in rows:
                if row['section'] == 'tfoot':
                    table['note'] = ' '.join([table['note']] + [visible_text(c['text']) for c in row['cells']]).strip()
        if self.dynamic_script:
            self.unsupported.append('检测到 script；脚本未执行，动态 JavaScript 表格不在验证范围')
        return self


def parse_html(raw):
    parser = VisibleHTML()
    parser.feed(raw)
    parser.close()
    parser.finish()
    headings = [event for event in parser.events if event['type'] == 'heading']
    last_heading = None
    for index, event in enumerate(parser.events):
        if event['type'] == 'heading': last_heading = (index, event['text'])
        elif event['type'] == 'table' and last_heading is not None:
            between = parser.events[last_heading[0]+1:index]
            if not between: event['record']['title'] = last_heading[1]
    for index, event in enumerate(parser.events):
        if event['type'] != 'table': continue
        if index + 1 < len(parser.events):
            following = parser.events[index + 1]
            if following['type'] == 'paragraph' and NOTE_PREFIX.match(following['text']):
                event['record']['note'] = following['text']
    visible = []
    for event in parser.events:
        if event['type'] == 'heading': visible.append('#' * event['level'] + ' ' + event['text'])
        elif event['type'] in ('paragraph','text'): visible.append(event['text'])
        elif event['type'] == 'table':
            rec = event['record']
            visible.extend([rec['caption'], ' | '.join(rec['headers'])])
            visible.extend(' | '.join(row) for row in rec.get('rows', []))
    return '\n'.join(x for x in visible if x), parser.tables, parser.unsupported, parser.events, parser.excluded


def strip_fenced_code_preserve_lines(raw):
    lines = raw.splitlines()
    output = []
    fence_char, fence_len = None, 0
    for line in lines:
        match = re.match(r'^\s*(`{3,}|~{3,})', line)
        if fence_char is None and match:
            marker = match.group(1)
            fence_char, fence_len = marker[0], len(marker)
            output.append('')
        elif fence_char is not None:
            if match and match.group(1)[0] == fence_char and len(match.group(1)) >= fence_len:
                fence_char, fence_len = None, 0
            output.append('')
        else:
            output.append(line)
    text = '\n'.join(output)
    return text + ('\n' if raw.endswith(('\n','\r')) else '')


def parse_markdown(raw):
    text = strip_fenced_code_preserve_lines(raw)
    lines = text.splitlines()
    global_unsupported = []
    if re.search(r'(?is)<table\b', text):
        global_unsupported.append('Markdown 内嵌 HTML table 未解析；需人工核验')
    tables, headings = [], []
    for i, line in enumerate(lines):
        hm = re.match(r'^\s*(#{1,6})\s+(.+?)\s*#*\s*$', line)
        if hm: headings.append({'level':len(hm.group(1)), 'text':hm.group(2).strip(), 'line':i+1})
    i = 0
    while i + 1 < len(lines):
        if '|' not in lines[i] or not re.match(r'^\s*\|?\s*:?-{3,}.*-?\s*\|?\s*$', lines[i+1]):
            i += 1; continue
        head = [c.strip() for c in lines[i].strip().strip('|').split('|')]
        sep = [c.strip() for c in lines[i+1].strip().strip('|').split('|')]
        if len(sep) != len(head) or any(not re.fullmatch(r':?-{3,}:?', c) for c in sep):
            i += 1; continue
        start = i
        i += 2
        body = []
        unsupported = []
        if re.search(r'\\\||`[^`\n]*\|[^`\n]*`', lines[start] + '\n' + lines[start+1]):
            unsupported.append('表头或分隔行含转义/行内代码管道符，Markdown 解析需人工核验')
        while i < len(lines) and '|' in lines[i] and lines[i].strip():
            if re.search(r'\\\||`[^`\n]*\|[^`\n]*`', lines[i]):
                unsupported.append('表体含转义/行内代码管道符，Markdown 解析需人工核验（line %d）' % (i+1))
            row = [c.strip() for c in lines[i].strip().strip('|').split('|')]
            if len(row) != len(head): unsupported.append('Markdown 行列数与表头不齐，需人工核验（line %d）' % (i+1))
            body.append(row)
            i += 1
        note = ''
        j = i
        while j < len(lines) and not lines[j].strip(): j += 1
        if j < len(lines) and NOTE_PREFIX.match(lines[j].strip()): note = lines[j].strip()
        prev_heading = [h for h in headings if h['line'] < start+1]
        between = [line.strip() for line in lines[prev_heading[-1]['line']:start] if line.strip()] if prev_heading else [line.strip() for line in lines[:start] if line.strip()]
        explicit_title = between[-1] if between and re.match(r'^表\s*\d*\s*[:：.]', between[-1]) else ''
        if explicit_title:
            title = explicit_title
        elif prev_heading and not between:
            title = prev_heading[-1]['text']
        else:
            title = ''
        tables.append({'format':'markdown', 'location':'line %d' % (start+1), 'title':title, 'caption':'', 'note':note,
                       'headers':head, 'rows':body, 'unsupported':unsupported})
    return text, tables, headings, global_unsupported


def context_applies(context, header):
    if not context: return False
    norm = re.sub(r'[（(].*?[）)]|[%％↑↓]', '', header).strip()
    if norm and norm in context: return True
    return bool(re.search(r'(全表|所有数值列|全部指标|本表各列|本表所有)', context))


def inspect_table(table, index):
    issues = list(dict.fromkeys(table['unsupported']))
    headers, rows = table['headers'], table['rows']
    if not (table['title'] or table['caption']): issues.append('缺少当前表的表题或 caption，需人工核验')
    if not rows: issues.append('没有可解析的数据行，需人工核验')
    context_sources = [('表题', table['title']), ('caption', table['caption']), ('当前表注', table['note'])]
    for col, header in enumerate(headers):
        vals = [row[col] for row in rows if col < len(row)]
        numeric = any(is_number(v) for v in vals)
        if not numeric:
            continue
        issues.append('第%d数值列“%s”含义需人工复述' % (col+1, header or '（空表头）'))
        descriptive = bool(DESCRIPTIVE.search(header))
        metric = bool(NUMERIC_HEADER.search(header))
        matching = [text for _, text in context_sources if context_applies(text, header)]
        scoped = ' '.join([header] + matching)
        inline_unit = any(cell_has_unit(v) for v in vals)
        if not header_has_unit(scoped) and not inline_unit:
            if descriptive or metric:
                issues.append('第%d数值列“%s”未找到可绑定单位；分母需人工核验' % (col+1, header))
            else:
                issues.append('第%d未知数值列“%s”是否需要单位/方向需人工判断' % (col+1, header))
        percent = '%' in scoped or '％' in scoped or any('%' in v or '％' in v for v in vals)
        if percent:
            issues.append('第%d列为百分数；分母与百分点的区别需人工核验' % (col+1))
        if metric and not DIRECTION.search(scoped):
            issues.append('第%d评价列“%s”未找到可绑定方向，需人工核验' % (col+1, header))
        elif not metric and not descriptive:
            issues.append('第%d列方向规则是否适用需人工判断' % (col+1))
        unrelated = [name for name, text in context_sources if text and not context_applies(text, header) and (HEADER_UNIT.search(text) or DIRECTION.search(text))]
        if unrelated:
            issues.append('表注/表题含单位或方向，但无法绑定到第%d列；需人工核验' % (col+1))
    numeric_columns = [{'index':i+1,'header':header,'numeric_cells':sum(is_number(row[i]) for row in rows if i < len(row))}
                       for i,header in enumerate(headers) if any(is_number(row[i]) for row in rows if i < len(row))]
    return {'index':index, 'format':table['format'], 'location':table['location'], 'title':table['title'], 'caption':table['caption'],
            'note':table['note'], 'sections':table.get('sections', []), 'section_rows':table.get('section_rows', [{'section':'tbody','cells':row} for row in rows]), 'columns':len(headers), 'rows':len(rows),
            'headers':headers, 'numeric_columns':numeric_columns, 'issues':list(dict.fromkeys(issues)), 'unsupported':list(dict.fromkeys(table['unsupported']))}


def report_body_and_appendix(text, headings):
    cut = len(text)
    for heading in headings:
        if APPENDIX.match(heading['text'].strip()):
            cut = min(cut, heading.get('offset', len(text)))
    return text[:cut]


def first_screen_proxy(text, headings, limit, number_limit, density_limit):
    h2 = [h for h in headings if h['level'] == 2]
    first_h2 = h2[0]['offset'] if h2 else len(text)
    intro = text[:first_h2]
    intro = re.sub(r'(?m)^\s*#\s+.*$', '', intro).strip()
    if intro:
        first = intro
        boundary = '源码结构代理：文档开篇到首个二级章节前的可见文字'
    elif h2:
        end = h2[1]['offset'] if len(h2) > 1 else len(text)
        first = text[h2[0]['offset']:end]
        boundary = '源码结构代理：首个二级章节到第二个二级章节（或文档结尾）'
    else:
        first = text
        boundary = '源码结构代理：无二级章节，按全文可见文字计量'
    density_text = re.sub(r'`[^`]*`|https?://\S+|\[[^\]]*\]\([^)]*\)', '', first)
    density_text = re.sub(r'(?m)^\s*#{1,6}.*$|^\s*\[\^?\d+\]:.*$', '', density_text)
    density_text = re.sub(r'\[\^?\d+\]', '', density_text)
    density_text = re.sub(r'(?<!\d)(?:19|20)\d{2}(?:[-年/]\d{1,2}(?:[-月/]\d{1,2}日?)?)?(?!\d)', '', density_text)
    density_text = re.sub(r'\[\^?\d+\]', '', density_text)
    density_text = re.sub(r'(?m)^\s*\d+[.、)]\s*', '', density_text)
    nums = ARABIC_NUMBER.findall(density_text) + CJK_NUMBER.findall(density_text)
    visible_chars = len(re.sub(r'\s+', '', density_text))
    density = round(100 * len(nums) / max(visible_chars, 1), 3)
    warnings = ['开篇长度和数字密度是源码结构代理量，不是真实 viewport 首屏、屏幕显示或理解测量']
    if len(first) > limit: warnings.append('开篇源码代理长度 %d 超过提醒阈值 %d' % (len(first), limit))
    if len(nums) > number_limit: warnings.append('开篇源码代理数字片段 %d 超过提醒阈值 %d' % (len(nums), number_limit))
    if density > density_limit: warnings.append('每百可见字符数字片段 %.3f 超过提醒阈值 %.3f' % (density, density_limit))
    return {'characters':len(first), 'number_fragments':len(nums), 'number_tokens_per_100_characters':density,
            'boundary':boundary, 'measurement':'源码代理量；不是真实viewport首屏或用户阅读',
            'limits':{'characters':limit,'numbers':number_limit,'density':density_limit}}, warnings, first


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('report')
    ap.add_argument('--deny', nargs='*', default=[])
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--first-screen-limit', type=int, default=1200)
    ap.add_argument('--first-screen-numbers-limit', type=int, default=8)
    ap.add_argument('--number-density-limit', type=float, default=3.0)
    ap.add_argument('--table-columns-limit', type=int, default=8)
    args = ap.parse_args()
    try:
        with open(args.report, encoding='utf-8') as f: raw = f.read()
    except (OSError, UnicodeError) as exc:
        obj = {'report':args.report,'parse_status':'read_error','error':str(exc),'hard_failures':[],'warnings':[],
               'unsupported':[],'tables':[],'manual_review':['无法读取报告文件'],'comprehension':'未测量'}
        print(json.dumps(obj, ensure_ascii=False) if args.json else 'ERROR ' + str(exc))
        sys.exit(2)
    unsupported = []
    if args.report.lower().endswith(('.html','.htm')):
        text, tables, unsupported, events, excluded = parse_html(raw)
        headings = []
        cursor = 0
        for event in events:
            if event['type'] == 'heading':
                heading = dict(event)
                needle = '#' * heading['level'] + ' ' + heading['text']
                heading['offset'] = text.find(needle, cursor)
                if heading['offset'] < 0: heading['offset'] = cursor
                cursor = heading['offset'] + len(needle)
                headings.append(heading)
    else:
        text, tables, headings, markdown_unsupported = parse_markdown(raw)
        unsupported.extend(markdown_unsupported)
        excluded = {'script':0,'style':0,'template':0,'hidden':0,'comments':0}
        for heading in headings:
            heading['offset'] = sum(len(x)+1 for x in text.splitlines()[:heading['line']-1])
    hard, warnings = [], []
    cjk = len(re.findall(r'[\u4e00-\u9fff]', text))
    latin = len(re.findall(r'[A-Za-z]{2,}', text))
    if cjk < 4 * max(latin, 1) and cjk < 800:
        warnings.append('中英比例偏低（%d 个汉字，%d 个英文词），仅结构风险提醒，需人工判断' % (cjk, latin))
    deny_hits = []
    for label in args.deny:
        count = text.count(label)
        if count:
            deny_hits.append({'label':label,'count':count})
            hard.append('用户 --deny 规则命中“%s” %d 次' % (label,count))
    for label in DENY_HINTS:
        if label in text: warnings.append('关键词“%s”命中；可误报或被改写绕过，不构成语义判断' % label)
    proxy, proxy_warnings, proxy_text = first_screen_proxy(text, headings, args.first_screen_limit, args.first_screen_numbers_limit, args.number_density_limit)
    warnings.extend(proxy_warnings)
    warnings.append('待人工复述：标题属于问题还是结论、核心发现及其证据；出现“发现”一词不构成通过')
    if not args.report.lower().endswith(('.html', '.htm')):
        bold_spans = re.findall(r'\*\*[^*\n]+\*\*', proxy_text)
        if not bold_spans:
            warnings.append('首屏没有加粗；需人工判断核心发现、关键数字和决定是否一眼可见')
        bold_all = sum(len(x) for x in re.findall(r'\*\*[^*\n]+\*\*', raw))
        if bold_all > 0.10 * max(len(raw), 1):
            warnings.append('全文加粗约占 %d%%；超过一成时，需人工判断是否滥用加粗' % int(100 * bold_all / max(len(raw), 1)))
    if not re.search(r'!\[[^\]]*\]\([^)]+\)|```mermaid|<svg\b|<img\b|<canvas\b', raw, re.I):
        warnings.append('未发现图（图片、Mermaid、SVG）；需人工判断是否有关系或比较适合用图表达，见 SKILL.md 原则 4')
    fig_re = r'!\[[^\]]*\]\([^)]+\)|```mermaid|<svg\b|<img\b|<canvas\b'
    fig_m = re.search(fig_re, raw, re.I)
    h2_m = re.search(r'(?m)^##\s|<h2\b', raw)
    if fig_m and h2_m and fig_m.start() > h2_m.start():
        warnings.append('第一张图出现在首个二级标题之后；研究结果汇报需人工判断首屏是否已有一张画主结论的图')
    for label, pat in (
            ('弱动词加抽象名词（进行/作出/加以 + 研究、比较等），需人工判断能否换成具体动词', r'(?:进行|作出|做出|加以|予以|给予)了?[^，。；\s]{0,4}(?:研究|分析|比较|检验|验证|评估|讨论|调整|改进|训练|测试|试验|实验|说明|处理)'),
            ('“之一”', r'之一'),
            ('“由于……所以/因此/使得”叠用', r'由于[^。]{0,40}(?:所以|因此|使得|导致)'),
            ('“成功地”这类多余副词', r'成功地'),
            ('“性/度”加高低的抽象名词说法（如“可读性很高”）', r'[\u4e00-\u9fff]{1,3}(?:性|度)(?:很|较|比较|极|更)?(?:高|低|强|大)')):
        hits = re.findall(pat, text)
        if hits:
            warnings.append('出现%s %d 处；见 references/report/examples.md 中文句子一节，需人工判断能否改写，技术名词和确有逻辑需要时保留' % (label, len(hits)))
    de_clauses = [c for c in re.split(r'[，。；：\n]', text) if c.count('的') >= 3]
    if len(de_clauses) >= 3:
        warnings.append('有 %d 个分句含 3 个以上“的”；见 references/report/examples.md 中文句子一节，需人工判断能否拆句或改用“而”' % len(de_clauses))
    if args.report.lower().endswith(('.md', '.markdown')):
        blocks = [b for b in re.split(r'\n\s*\n', raw) if b.strip()]
        paras = [b for b in blocks if not re.match(r'\s*(#|\||[-*] |\d+\. |!\[|```)', b)]
        if paras:
            lens = [len(re.sub(r'\s+', '', b)) for b in paras]
            avg = sum(lens) / len(lens)
            if avg > 110 or max(lens) > 200:
                warnings.append('正文段平均 %d 字、最长 %d 字；见 references/report/result.md 的表格与结构一节，需人工判断是否需要分段、分行或做表，让版面能扫读' % (avg, max(lens)))
    if args.report.lower().endswith(('.md', '.markdown')) and len(raw) > 800 and not re.search(r'(?m)^\s*(?:[-*]|\d+\.) |^\|', raw):
        warnings.append('全文没有列表或表格；见 references/report/result.md 的表格与结构一节，需人工判断三项以上并列的内容是否该分行或做表')
    jargon = [w for w in ('全绿', '哑火', '铁律', '红线', '对拍', '翻皮', '原地生产', '验尸', '僵尸', '落盘', '拉齐', '闭环', '抓手', '赋能', '颗粒度', '底座') if w in text]
    if jargon:
        warnings.append('出现内部行话或比喻：%s；见 references/report/examples.md 的拒收样例，需人工判断读者是否见过，没见过就改成直接描述' % '、'.join(jargon))
    if re.search(r'小(?:网络|程序|模型)', text):
        warnings.append('出现“小网络/小程序/小模型”这类口语称呼；需人工判断能否换成标准名词，如模块、校准器、读出头')
    intro_paras = [p for p in re.split(r'\n\s*\n', proxy_text) if p.strip()]
    if intro_paras:
        first_para = intro_paras[0]
        if len(first_para) > 220:
            warnings.append('第一段 %d 字；需人工判断是否塞了多件事，第一段只讲问题、做法、结果和决定' % len(first_para))
    if len(intro_paras) > 5:
        warnings.append('开篇源码代理有 %d 段；超过 5 段时，需人工判断总判断和三问是否各自只占一段' % len(intro_paras))
    if re.search(r'(95% ?区间|Brier|置信区间)', proxy_text): warnings.append('开篇源码片段出现统计术语，需人工确认是否已定义')
    if re.search(r'^\s*(?:本文|报告|这份报告)(?:不讲|不涉及|不讨论|没有)', proxy_text, re.M): warnings.append('开篇源码片段以范围/限制句开始，需人工判断')
    if re.search(r'例[^\n]{0,40}(不是|并非|仅演示|只演示)|(不是模型输出|不是真实|只演示)', proxy_text): warnings.append('示例包含免责声明措辞，需人工判断')
    if len(DISCLAIM.findall(text)) >= 4: warnings.append('否定/局限措辞命中多次；关键词可能误报或被改写绕过，需人工检查')
    body = report_body_and_appendix(text, headings)
    flow_hits = PROCESS.findall(body)
    if flow_hits:
        warnings.append('主线流程词命中 %d 次；词语可误报或被改写绕过，需人工判断，不能证明语义' % len(flow_hits))
    stat_terms = re.findall(r'(置信区间|\d+% ?区间|重抽样|分箱|Brier|bootstrap|训练种子|随机种子|p ?值|显著性)', body, re.I)
    if len(stat_terms) >= 6:
        warnings.append('主线统计口径词出现 %d 次；词语可误报，需人工判断区间、重抽样、分箱、种子数等细节是否应移到表注或附录' % len(stat_terms))
    role_hits = re.findall(r'(师兄|师姐|导师|用户决定|用户同意|AI 设计|AI设计)', body)
    if role_hits:
        warnings.append('主线出现内部称呼 %d 次（如“%s”）；词语可误报，需人工判断读者是否认得这个角色' % (len(role_hits), role_hits[0]))
    appendix_line = None
    for heading in headings:
        if APPENDIX.match(heading['text'].strip()) and 'line' in heading:
            appendix_line = heading['line']; break
    if appendix_line is not None:
        main_tables = [t for t in tables if t['location'].startswith('line ') and int(t['location'].split()[1]) < appendix_line]
        if len(main_tables) > 6:
            warnings.append('主线有 %d 张表；超过 6 张时，需人工判断是否有只供复算或追溯的表应移到附录' % len(main_tables))
    parsed = [inspect_table(table, i+1) for i, table in enumerate(tables)]
    for item in parsed:
        note_text = item.get('note') or ''
        if len(note_text) > 220:
            warnings.append('第%d张表的表注 %d 字；超过 220 字时，需人工判断口径细节是否应移到附录' % (item['index'], len(note_text)))
        warnings.extend('第%d张%s表（%s）：%s' % (item['index'],item['format'],item['location'],issue) for issue in item['issues'])
        if item['columns'] > args.table_columns_limit:
            warnings.append('第%d张表有%d列，超过宽表提醒阈值%d' % (item['index'],item['columns'],args.table_columns_limit))
    for line in text.splitlines():
        if re.match(r'^\s*(\d+[.、]|[-*])\s*',line) and any(word in line for word in TOC_META) and len(line)<40:
            warnings.append('目录/清单疑似含步骤或元信息：'+line.strip()[:40])
    manual = ['复述标题属于问题还是结论','复述核心发现及证据','核验数值列含义、单位/分母，以及适用时的比较或评价方向；描述量可无方向']
    if unsupported: manual.append('检查脚本列出的 unsupported 结构')
    warnings = list(dict.fromkeys(warnings))
    obj = {'report':args.report,'parse_status':'parsed','hard_failures':hard,'warnings':warnings,'unsupported':unsupported,'excluded_content':excluded,
           'first_screen_proxy':proxy,'tables':parsed,'manual_review':manual,
           'deny_hits':deny_hits,'keyword_policy':'默认仅提醒；只有用户显式 --deny 命中才硬失败',
           'comprehension':'未测量；代理阈值仅是结构提醒，不是真实viewport或理解标准'}
    if args.json: print(json.dumps(obj,ensure_ascii=False,indent=2))
    else:
        for item in hard: print('FAIL',item)
        for item in warnings: print('WARN',item)
        for item in unsupported: print('UNSUPPORTED',item)
        print('结构检查结束：%d 项硬失败，%d 项提醒；仅静态结构检查，不证明理解。' % (len(hard),len(warnings)))
    sys.exit(1 if hard else 0)

if __name__ == '__main__':
    main()
