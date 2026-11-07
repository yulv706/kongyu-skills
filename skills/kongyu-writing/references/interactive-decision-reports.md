# Interactive Decision Reports

只有读者需要在浏览器中点击决策选项、且 agent 必须持久读取并执行选择时，才使用此模式。它是 Decision Memo shell 的交互式升级；简单 A/B/C 选择可直接在聊天中答复。

## 何时使用

- 报告列出了多个需要用户拍板的选项（A/B/C）
- 用户在浏览器中点击选项，agent 需要立即或稍后读取决策结果
- 报告需要保持离线可读（PDF 导出时决策状态保留）

不用于：
- 纯信息展示（没有决策项）→ 用普通 Progress Report
- 用户只需在聊天中回复的简单选择 → 不需要服务器

## 架构

```
浏览器 (gate-audit-report.html)
  ↓ POST /api/decision
本地 HTTP 服务器 (serve.py, 127.0.0.1:<port>, dedicated sanitized preview dir)
  ↓ write JSON
私有决策文件 (served directory 外的 runtime path)
  ↑ agent reads
Agent
```

三个组件：

1. **HTML 报告**：只从专用、经过清洗的 preview directory 提供，嵌入 `decide(id, choice, button)` JS 函数，POST 成功后才显示已保存。页面加载时 GET 已有决策并恢复状态；GET/POST 失败时明确显示未保存或未能恢复。
2. **本地 HTTP 服务器**：`http.server.HTTPServer` 绑定 127.0.0.1，处理 POST /api/decision（写入 JSON）和 GET /api/decisions（返回 JSON）。优先使用同源 HTTP；不要用 `Access-Control-Allow-Origin: *` 暴露私有决策数据。
3. **决策 JSON 文件**：数组结构 `[{decision_id, choice, question, timestamp, updated_at}]`，agent 用 `json.load()` 读取。

## 服务器脚本模板

```python
import http.server, json, os, datetime

PORT = 8765  # replace with a verified-free port and record it in the owner file
DIR = r"<dedicated-sanitized-preview-dir>"
DECISIONS_FILE = r"<private-runtime-dir>\<slug>-decisions.json"  # outside DIR

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def do_POST(self):
        if self.path == "/api/decision":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length).decode("utf-8")
            data = json.loads(body)
            # Upsert by decision_id
            existing = []
            if os.path.exists(DECISIONS_FILE):
                with open(DECISIONS_FILE, "r", encoding="utf-8") as f:
                    existing = json.load(f)
                    if not isinstance(existing, list):
                        existing = [existing]
            found = False
            for item in existing:
                if item.get("decision_id") == data.get("decision_id"):
                    item.update(data)
                    item["updated_at"] = datetime.datetime.now().isoformat()
                    found = True
                    break
            if not found:
                data["updated_at"] = datetime.datetime.now().isoformat()
                existing.append(data)
            with open(DECISIONS_FILE, "w", encoding="utf-8") as f:
                json.dump(existing, f, ensure_ascii=False, indent=2)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"ok": True}).encode())
        else:
            self.send_error(404)

    def do_GET(self):
        if self.path == "/api/decisions":
            content = "[]"
            if os.path.exists(DECISIONS_FILE):
                with open(DECISIONS_FILE, "r", encoding="utf-8") as f:
                    content = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(content.encode())
        else:
            super().do_GET()

    def log_message(self, *args):
        pass

if __name__ == "__main__":
    server = http.server.HTTPServer(("127.0.0.1", PORT), Handler)
    print(f"Serving on http://127.0.0.1:{PORT}/")
    server.serve_forever()
```

## HTML 决策卡片模板

```html
<div class="decision-card" id="dc-<id>">
  <div class="dc-question">决策 <id>：<问题标题></div>
  <div class="dc-context"><背景和选项说明></div>
  <div class="dc-options">
    <button type="button" class="dc-opt" data-choice="A" onclick="decide('<id>', 'A', this)">A: <选项A标签></button>
    <button type="button" class="dc-opt" data-choice="B" onclick="decide('<id>', 'B', this)">B: <选项B标签></button>
  </div>
  <div class="dc-result" id="dc-<id>-result"></div>
  <div class="dc-save-status" role="status" aria-live="polite"></div>
</div>
```

```javascript
function showSavedChoice(card, choice) {
  const selected = Array.from(card.querySelectorAll('.dc-opt'))
    .find(button => button.dataset.choice === choice);
  if (!selected) return false;
  card.classList.add('decided');
  card.querySelectorAll('.dc-opt').forEach(button => {
    button.classList.toggle('selected', button === selected);
    button.setAttribute('aria-pressed', String(button === selected));
  });
  card.querySelector('.dc-result').textContent = selected.textContent.trim();
  card.querySelector('.dc-save-status').textContent = '已保存';
  return true;
}

async function decide(id, choice, button) {
  const card = document.getElementById('dc-' + id);
  if (!card || button.dataset.choice !== choice) return;
  const status = card.querySelector('.dc-save-status');
  const options = card.querySelectorAll('.dc-opt');
  options.forEach(option => { option.disabled = true; });
  status.textContent = '正在保存…';
  try {
    const response = await fetch('/api/decision', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        decision_id: id,
        choice,
        question: card.querySelector('.dc-question').textContent,
        timestamp: new Date().toISOString()
      })
    });
    if (!response.ok || (await response.json()).ok !== true) {
      throw new Error('decision was not saved');
    }
    showSavedChoice(card, choice);
  } catch (_error) {
    status.textContent = '新选择未保存，请重试';
  } finally {
    options.forEach(option => { option.disabled = false; });
  }
}

async function restoreDecisions() {
  try {
    const response = await fetch('/api/decisions');
    if (!response.ok) throw new Error('decisions could not be loaded');
    const items = await response.json();
    if (!Array.isArray(items)) throw new Error('invalid decisions response');
    items.forEach(item => {
      const card = document.getElementById('dc-' + item.decision_id);
      if (card) showSavedChoice(card, item.choice);
    });
  } catch (_error) {
    document.querySelectorAll('.decision-card .dc-save-status').forEach(status => {
      status.textContent = '无法读取已有选择';
    });
  }
}
document.addEventListener('DOMContentLoaded', restoreDecisions);
```

替换占位内容时，把 `<id>` 限定为不会破坏 HTML/JS 字符串的稳定 slug，并正确转义问题与选项文字。必须从实际 POST 响应和私有 JSON 文件确认保存；页面按钮变色不是持久化证据。

## Agent 读取决策

```python
import json
with open(decisions_file, "r", encoding="utf-8") as f:
    decisions = json.load(f)
for d in decisions:
    print(f"决策 {d['decision_id']}: {d['choice']}")
```

或通过 HTTP：
```bash
curl http://127.0.0.1:<port>/api/decisions
```

## PDF 导出

浏览器原生 `window.print()` (Ctrl+P) 触发。报告 HTML 包含 print CSS：
- 隐藏 action bar 和 filter 控件
- 展开 details 元素
- 决策卡片只显示已选结果，隐藏未选选项
- 防止表格/卡片跨页断裂

在 action bar 中放一个"导出 PDF"按钮，`onclick="window.print()"`。不需要第三方库。

## 本地预览安全与服务器生命周期

- 启动前把 HTML/资源复制或生成到专用、经过清洗的 preview directory；不得把项目根目录、源层或 `_tmp` 作为 `DIR`。`DECISIONS_FILE` 必须在 served directory 外的私有 runtime path。
- 选择并验证空闲端口，绑定 127.0.0.1；启动后写 owner 文件（在 served directory 外），至少记录 `pid`、`port`、`bind`、解析后的 `DIR`、`started_at` 和 owner/session 标识，不写密钥、cookie、passphrase 或私有正文。
- 分享 URL 前确认该 PID/启动时间确实拥有该端口且命令身份正确。任务完成后默认停止：停止前再次核对 owner 文件与端口归属，停止后验证端口已关闭；不要按一个未经核对的 PID 杀进程。
- 清理只删除已停止且明确属于本次会话的 preview directory、私有决策文件和 owner 文件；用户要求保留的预览不擅自删除。若用户明确要求继续运行，记录责任人、PID、端口、目录和停止命令。
- 没有服务器时可用 `file://` 查看静态页面，但不要把“页面能打开”当作决策已保存；通过文件或 HTTP 读取并确认实际决策。

## 与 kongyu-writing 其他 shell 的关系

- Interactive Decision Report 是 Decision Memo 的交互式实现
- 报告结构仍然遵循冷启动门控和认知熵减少原则
- 决策卡片放在证据之后、修改清单之前
- 导出 PDF 时决策状态保留（print CSS 显示已选结果）

## 边界

- 服务器只绑定 127.0.0.1，不暴露到网络
- preview directory 只包含清洗后的读者层；私有决策文件和 owner 文件放在 served directory 外，不提交到 Git
- 如果用户不在浏览器中操作，agent 不应假设决策已做出——读文件确认
- 服务器进程需要 agent 管理：启动时记录 PID/端口归属，结束时按 owner 核对并验证已停止
- 端口冲突时换一个经过验证的空闲端口（8765 只是示例默认值）
