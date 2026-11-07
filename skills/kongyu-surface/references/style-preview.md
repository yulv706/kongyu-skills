# 风格试衣间规范（Style Preview）

> 本参考只用于需要用户比较视觉方向的任务。预览帮助作出实际决策，不是每次设计的固定前置步骤。

## 何时生成

- 用户明确要求比较几个风格或方向
- 存在尚未解决且需要用户选择的实质品牌决策

不适用：普通新页面或重设计、纯代码审查、纯交互逻辑优化、用户已指定参考或授权代理决定风格。此时沿用项目风格或选合理默认直接完成，不因方向未指定而暂停。

候选数量按用户要求或最小决策需要确定，通常两到三个即可。下方四方向外壳和快捷键是可裁剪示例，不是数量或交互组件配额。

## 产物要求

生成一个浅层、非隐藏、经过清洗且专用的预览任务目录。预览目录只承载
`index.html` 和确实需要的读者层 assets；不得把项目根目录、源层、`_tmp`
或其父目录作为 server root。任务名先清洗为只含安全字母、数字、`-`、`_`
的 slug，去掉路径分隔符、`..`、密钥和私有内容。

1. 用户指定输出位置时，以它为**专用目录或专用父目录**为准；先解析绝对路径并确认不会覆盖或暴露其它文件
2. 当前在项目 / Git 仓库中工作时，写到项目根目录下的专用目录：`design-previews/YYYY-MM-DD-<sanitized-slug>/index.html`
3. 同目录可放 `README.md` 和必要 assets；owner/PID/port 文件放在 served directory 外。`selection.json` 只在已有本地回传桥时使用，静态预览默认不写文件
4. 当前不在任何项目目录时，退到专用桌面目录：`~/Desktop/qiaomu-design-YYYY-MM-DD-<sanitized-slug>/`
5. 预览目录用于方向选择、截图、打包分享；最终生产代码仍写进用户当前项目文件，并由该项目 Git 管理

主入口固定叫 `index.html`，自包含单文件（CSS/JS 内联，Google Fonts 允许），打开即用。

### 固定选择外壳

预览页的 demo 可以有不同视觉风格，但**选择外壳必须稳定一致**：

- 顶部固定中性工具条：任务名 / 回传状态 / 快捷键 1-4
- 一句低干扰文案说明：这是**设计方向样机**，不是最终 App / 最终页面；点选方向后才进入正式实现
- 设计拨盘用中文标签：`视觉冒险度`、`动效强度`、`信息密度`（括号可保留英文变量名，但不能只显示英文）
- 三拨盘必须是可拖动滑块，拖动时数值即时变化；确认选择时随方向一起回传
- 每个方向卡片底部有统一按钮：`选择 A · 方向名`；按钮上方短说明横排 full-width，最多两行
- 点选方向或按键 1-4 后先打开确认弹层（方向名 + 拨盘值 + 调整建议输入框），确认后才回传
- 选中后卡片高亮 + 底部 toast 显示"已回传"
- 外壳保持中性克制，不参与方向风格竞争；方向差异只发生在 demo/mockup 内

### 多方向隔离协议

多个方向不能由同一套默认样式连续换皮。先写 Surface Mode（与 skill 主文一致），再写 brief：

1. 为实际需要的候选分别写简短 brief：目标用户、功能契约与主要视觉差异；`shell`/`workbench` 可以共享稳定字栈，通过密度、边界、focus 或布局语法区分
2. 只有用户明确授权 subagent/并行代理且当前工具政策允许时，才把方向拆给 subagent；否则主流程按独立 brief 逐个生成
3. 每个方向使用独立 stage 和 scoped CSS：类名前缀如 `.dir-a` / `.sa-a`，不得写全局 `button`、`.card`、`body`
4. 整合统一壳、选择回传、推荐理由和横向对比；确认候选并非仅换色
5. 单 agent 生成不是降级失败；只要 brief、CSS scope、轴级差异和最终截图/人工检查成立，就满足隔离目标

### 页面结构

1. **顶部状态条**：任务名 + "方向样机，不是最终 App / 最终页面" + 快捷键提示 + 回传状态
2. **设计样机区**（候选数量按实际需要，一个标「推荐」徽标）。布局随候选数量调整。每个样机块：
   - 真实迷你 mockup（真字体、真配色、真布局，约 480×300 逻辑尺寸，`transform: scale` 适配卡宽），不是色板色块
   - 候选可直接比较，嵌在同一个 `index.html` 的独立 stage 容器中
   - mockup 舞台填满空间；比例不匹配时居中，不允许大片空白
   - 方向名、极短标签和选择按钮；长解释移到方向说明区
   - 明显的「选择 A/B/C/D · 方向名」按钮，位置样式交互在所有方向一致且独立成行
3. **方向说明区**：样机区之外，一句话气质、字体策略、色彩策略、记忆点、适用场景、推荐理由
4. **三拨盘控制区**：`视觉冒险度`、`动效强度`、`信息密度`，范围 1-10，当前数值可见
5. **确认弹层**：点击方向/卡片/按键 1-4 后打开，包含方向名、拨盘值、调整建议输入框、取消/确认并回传
6. **选中反馈**：确认后卡片高亮 + 底部浮条显示"已选择方向 X，已回传"
7. 支持键盘 1/2/3/4 选择；说明区注明可混搭（"要 A 的配色 + B 的字体"）
8. **禁止自动推进**：无倒计时、超时默认选择或自动回传

### Mockup 质量标准

- 每个 mockup 必须能独立通过反套路扫描（无 AI 紫、无斜体、无居中套路）
- 预览页自身遵守中文字体纪律：壳与所有 mockup 正文用系统字体栈；装饰中文字体只用于 mockup 标题短语且 `text=` 子集化
- 方向之间满足 divergence-playbook 的轴级差异（按 Surface Mode：`brand` ≥4 轴且含明度/时代气质；`shell`/`workbench` 含 ≥1 个 Geist/精确方向 + 语法轴可辨）
- mockup 内文案用任务的真实内容，不用 Lorem ipsum
- 壳（说明条、卡片框）保持中性克制，不与方向 mockup 抢戏

### 选择协议

默认是静态选择协议，真实世界优先：预览页必须能通过 `file://` 或本地浏览器直接打开，不依赖临时服务。

1. 页面选择按钮/卡片点击/键盘 1-4 都先打开确认弹层；确认后高亮选择并复制“选 X + 拨盘 + 调整建议”文本
2. 用户在对话中回复“选 X / 你定 / 按推荐继续 / A 的配色 + B 的字体”等明确选择，才进入 Phase 3
3. 如果项目已经有本地回传桥，可以额外写入同目录 `selection.json`，包含 `{id,label,name,notes,dials,adjustments}`；没有桥就不要临时发明服务器
4. 进入 Phase 3 前必须满足其一：用户在对话中明确选择、用户授权默认、或已观察到现成回传桥产生的 `selection.json`

禁止在没有选择证据时把推荐态当作用户选择。
禁止用超时、倒计时、推荐态自动写入选择。
禁止因为“能做服务”就新增预览服务器；先用静态协议，除非已有项目约束需要自动回传。

## 本地预览安全与生命周期

- 静态 `file://` 预览也必须从上述专用清洗目录打开。若已有项目约束需要 HTTP，先确认空闲端口，绑定 `127.0.0.1`，并在 served directory 外写 owner 文件，记录 `pid`、`port`、`bind`、解析后的 preview directory、`started_at` 和 owner/session 标识；不记录密钥、cookie、passphrase 或私有源文档。
- 交付 URL 前验证端口确实由记录的 PID/启动时间和正确命令拥有。预览结束后默认停止并验证端口关闭；停止前重新核对 owner 与端口归属，不能只按一个裸 PID 停止。
- 清理只针对已停止且明确属于本次会话的专用预览目录、回传文件和 owner 文件；用户要求保留或分享的预览不擅自删除。若保持后台运行，必须向用户说明 owner、PID、端口、目录和停止方式。
- 分享或截图前检查目录清单，确认没有源层、`_tmp`、凭据、cookie、私有 URL、未发表草稿或私有过程文件。

## 页面骨架模板

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>设计方向预览 — {任务名}</title>
<style>
  body{margin:0;font-family:system-ui;background:#f4f4f2;color:#1a1a1a}
  .bar{padding:20px 32px;border-bottom:1px solid #ddd;display:flex;justify-content:space-between}
  .dials{display:grid;grid-template-columns:repeat(3,minmax(180px,1fr));gap:12px;padding:20px 32px;border-bottom:1px solid #ddd}
  .dial{display:grid;gap:6px;font-size:13px}.dial b{font-weight:650}.dial output{font-variant-numeric:tabular-nums}
  .grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;padding:32px}
  .card{background:#fff;border:2px solid #e2e2e0;border-radius:12px;overflow:hidden;cursor:pointer;display:flex;flex-direction:column;min-width:0}
  .card.selected{border-color:#1a1a1a}
  .mock{height:300px;overflow:hidden;position:relative;display:grid;place-items:center}
  .mock>.stage{width:960px;height:600px;transform:scale(.5);transform-origin:center center}
  .meta{padding:16px 20px;display:grid;gap:10px;min-width:0;width:100%;box-sizing:border-box}
  .meta p{margin:0;max-width:64ch;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;writing-mode:horizontal-tb;white-space:normal;overflow-wrap:break-word;word-break:normal;line-height:1.55}
  .qmdp-pick-button{position:relative;z-index:1;width:calc(100% - 40px);min-height:44px;margin:0 20px 20px;white-space:normal;writing-mode:horizontal-tb}
  .confirm{position:fixed;inset:0;display:none;place-items:center;background:rgb(0 0 0 / 32%);z-index:20}
  .confirm.open{display:grid}.dialog{width:min(520px,calc(100vw - 32px));background:#fff;border-radius:12px;padding:20px}
  textarea{width:100%;min-height:84px;resize:vertical}
  .pickbar{position:fixed;bottom:0;left:0;right:0;padding:14px;background:#1a1a1a;color:#fff;
           text-align:center;transform:translateY(100%);transition:transform 200ms cubic-bezier(.23,1,.32,1)}
  .pickbar.show{transform:translateY(0)}
  @media (max-width:760px){
    .bar{padding:16px;gap:12px;flex-wrap:wrap}
    .dials{grid-template-columns:1fr;padding:16px}
    .grid{grid-template-columns:1fr;padding:16px}
  }
</style>
</head>
<body>
  <div class="bar"><strong>{任务名} · 方向样机</strong>
    <span>键盘 1-4 选择 · 确认后回传</span></div>
  <div class="dials" data-qmdp-dials aria-label="设计拨盘">
    <label class="dial"><b>视觉冒险度 <output id="varianceOut" data-qmdp-output="variance">7</output></b><input id="variance" data-qmdp-dial="variance" type="range" min="1" max="10" value="7"></label>
    <label class="dial"><b>动效强度 <output id="motionOut" data-qmdp-output="motion">6</output></b><input id="motion" data-qmdp-dial="motion" type="range" min="1" max="10" value="6"></label>
    <label class="dial"><b>信息密度 <output id="densityOut" data-qmdp-output="density">4</output></b><input id="density" data-qmdp-dial="density" type="range" min="1" max="10" value="4"></label>
  </div>
  <div class="grid"><!-- 4 张方向卡片，推荐卡片加 data-rec 与「推荐」徽标 --></div>
  <div class="confirm" id="confirm" role="dialog" aria-modal="true" aria-labelledby="confirmTitle">
    <div class="dialog">
      <h2 id="confirmTitle">确认设计方向</h2>
      <p id="confirmMeta"></p>
      <textarea id="adjustments" placeholder="可选：写下想调整的地方，比如更稳一点、要 B 的字体 + C 的配色"></textarea>
      <button type="button" id="cancelPick">取消</button>
      <button type="button" id="confirmPick">确认并回传</button>
    </div>
  </div>
  <div class="pickbar" id="pickbar"></div>
<script>
  let pending = null;
  function dials(){
    return {
      variance: Number(document.getElementById('variance').value),
      motion: Number(document.getElementById('motion').value),
      density: Number(document.getElementById('density').value)
    };
  }
  ['variance','motion','density'].forEach(id => {
    const input = document.getElementById(id), out = document.getElementById(id + 'Out');
    input.addEventListener('input', () => { out.value = input.value; out.textContent = input.value; });
  });
  function selectionText(payload){
    const values = payload.dials || dials();
    const advice = payload.adjustments ? '；建议：' + payload.adjustments : '';
    return payload.label + '；拨盘：视觉冒险度 ' + values.variance +
      ' / 动效强度 ' + values.motion + ' / 信息密度 ' + values.density + advice;
  }
  async function sendSelection(payload){
    const msg = selectionText(payload);
    if (navigator.clipboard) await navigator.clipboard.writeText(msg).catch(()=>{});
    return {ok:false, static:true, text:msg};
  }
  function openConfirm(i, name){
    document.querySelectorAll('.card').forEach((c,idx)=>c.classList.toggle('selected', idx===i));
    const id = 'ABCD'[i];
    pending = {id, name, label:'选 ' + id + '：' + name};
    const values = dials();
    document.getElementById('confirmMeta').textContent =
      pending.label + ' · 视觉冒险度 ' + values.variance + ' / 动效强度 ' + values.motion + ' / 信息密度 ' + values.density;
    document.getElementById('confirm').classList.add('open');
    document.getElementById('adjustments').focus();
  }
  async function confirmSelection(){
    if(!pending) return;
    const msg = pending.label;
    const bar = document.getElementById('pickbar');
    const payload = {...pending, dials: dials(), adjustments: document.getElementById('adjustments').value.trim()};
    const result = await sendSelection(payload);
    bar.textContent = '已选择 ' + msg + ' — 已复制，请回到对话发送这句话';
    bar.classList.add('show');
    document.getElementById('confirm').classList.remove('open');
    if (navigator.clipboard) navigator.clipboard.writeText(result.text || msg).catch(()=>{});
  }
  document.addEventListener('keydown', e=>{
    const i = ['1','2','3','4'].indexOf(e.key);
    if(i>-1){ const c=document.querySelectorAll('.card')[i]; if(c) c.click(); }
  });
  document.getElementById('cancelPick').onclick = () => document.getElementById('confirm').classList.remove('open');
  document.getElementById('confirmPick').onclick = confirmSelection;
</script>
</body>
</html>
```

## 选择协议

1. 对话侧输出候选的简短差异、推荐理由和可打开的预览路径；如使用 HTTP 或后台仍在运行，保留其归属及停止信息
2. 三拨盘必须在预览页里可拖动；确认选择时随方向一起回传
3. 用户点击方向后必须进入确认弹层，可补充调整建议；确认后复制选择文本并高亮
4. 用户明确选择（回复"选 X"/混搭描述/授权默认；或现成回传桥写入 `selection.json`）→ 以用户为准
5. 用户未选时不得自动推进；只有用户明确说"你定/按推荐继续"才可按推荐方向进入 Phase 3
6. 推荐方向的选择标准：最贴合设计读取与受众，而非最炫

## 交付话术

生成后对用户说：

"候选方向预览已生成并打开：`design-previews/YYYY-MM-DD-<sanitized-slug>/index.html`。推荐 X：〈一句理由〉。" 仅当任务确实需要用户选择时等待回复；已有的默认选择授权继续有效，无需再次确认。
