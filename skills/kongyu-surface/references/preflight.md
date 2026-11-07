# 交付前门禁（Pre-flight Checklist）

> 规则：按入口大小适用门禁。**适用项不过就不交付**；不适用项标记 N/A，不阻止交付。
> 微调（单组件/单状态）只过 A 节相关项 + I 节；整页 polish 过全部适用项；方向选择额外过 C 节。
> 先定 Surface Mode（`shell|paper|brand|workbench|diagram|micro`，见 skill 主文），再勾禁令与正面工艺；不要同时套全部 reference。

## 0. Surface Mode

- [ ] 已声明 Surface Mode，并只加载该模式正面语法 + 中文叠加（若有 CJK）
- [ ] 未把 `paper` 报告壳误套 Geist dark，也未把 `brand` 营销页误锁死成产品 shell token

## A. 反套路扫描（AI Tells）

> Surface Mode=`brand` 的绿场/营销页与「反 AI 味」交付：先跑 `references/slop-gates.md`（六轴自检 + 门禁表），本节省查与功能无关的遗漏项。只读打分用 `review-protocols.md` §八 Audit。


- [ ] Surface Mode=brand 绿场/反 AI 味已跑 references/slop-gates.md（六轴自检 + 适用门禁目标答案均为否）；其它 mode 已跑通用门禁或标明 N/A
- [ ] 无紫蓝渐变、无装饰性 `#000000` 纯黑块、无外发光霓虹、无大标题渐变文字（Geist dark 产品壳 canvas 的 `#000` 除外，见 `vercel-precision-system.md`）
- [ ] 字体选择匹配页面气质：营销/创意/方向预览不得只靠 Inter/Roboto/Arial/系统默认；生产产品壳、工作台、设置页、中文 UI 可用稳定系统字体栈，记忆点来自比例、边界、密度、focus、交互一致性
- [ ] **全页无 `font-style: italic`**（中文伪斜体尤其禁止；强调只用字重/颜色/字号）
- [ ] Hero 不是居中构图（`brand` 且设计读取明确要求时可居中；其余模式默认禁止 AI 居中 Hero）
- [ ] 无三等分卡片横排；卡片没有被当作万能分组容器
- [ ] 无 John Doe/张三、无 99.99% 式整数假数据、无 Acme 式烂梗名
- [ ] 文案无"革命性/颠覆/无缝/赋能/下一代"；感叹号 ≤ 1
- [ ] 眉批（eyebrow）数量 ≤ ⌈section 数 / 3⌉；无 "SECTION 01" 式编号 meta-label
- [ ] H1 不超过 2-3 行（窄容器多行大标题 = 失败）
- [ ] Bento/网格无空洞（`grid-auto-flow: dense`，span 完全咬合）
- [ ] DNA 注入（from-scratch/重设计/营销/创意/方向预览适用）：能逐条说出"从哪个参考站偷了哪 3-5 个具体值"
- [ ] 视觉细节服务于内容与使用，不为达到签名动作数量而添加装饰
- [ ] Hero 视觉侧过关（营销/创意/方向预览适用）：高保真组件预览/抽象编辑构图/真实图像资产——无空心 div 假截图；功能型页面改为能指认 Vercel/Linear/IBM 等真实系统的具体继承点
- [ ] 暗底正文 `rgba(255,255,255,.85)`、次要文字 ≥ `.60`；正文区纹理 ≤ 3%
- [ ] 每个 CTA 做过对比度审计；主 CTA 不换行；同一意图全页一个文案
- [ ] 文案自审完成：无语法不通/指代不明/AI 装深沉句；假精确数据已清理
- [ ] 禁令之后有正面工艺：边界、spacing、字重、focus、交互态不是随手值；功能型页面可指认 Vercel/Linear/IBM 等真实系统的具体继承点

## B. 功能契约（任何 VARIANCE 值都不豁免）

- [ ] 已写下本页功能契约（存在理由 / 3 秒必得信息 / 必须能完成的动作）并逐条核对
- [ ] 页面类型的核心标识首屏可辨（404 的错误码、定价的价格、表单的提交路径）
- [ ] 创意元素没有遮蔽或稀释任何契约项

## C. 方向选择 / 多方案预览门禁（详见 style-preview.md）

- [ ] 本节仅在用户要求比较方向或实质品牌决策需要用户选择时适用；一般新页面或重设计可沿用项目风格或合理默认直接执行
- [ ] 适用时生成可打开的预览；候选数量按用户要求或实际决策需要确定，不设四份最低配额；方向在布局、密度、字体或色彩上有可辨差异
- [ ] 一个方向标「推荐」并说明理由；选择回传证据已观察（selection.json 或用户明确回复）
- [ ] 桌面和移动端截图都已检查：无横向滚动，mockup 占满或居中，内部无挤压遮挡
- [ ] 完整流程、选择外壳、回传协议见 `references/style-preview.md`

## D. 设计读取一致性

- [ ] 产出与声明的设计读取、三拨盘值一致（说了 VARIANCE 9 就不能交居中对称）
- [ ] 全页主题锁定：一页只有一个明暗主题，不混
- [ ] 功能、可读性、布局与约定风格符合要求；记忆点是可选表达，不是交付门槛
- [ ] 动效气质与视觉气质一致（cohesion）

## E. 动效抽查（详见 motion-craft.md）

- [ ] 无 `transition: all`；无 `ease-in`；无 `scale(0)` 入场
- [ ] UI 动效 ≤ 300ms；按压有 `:active` 反馈
- [ ] `prefers-reduced-motion` 兜底存在
- [ ] hover 动效包在 `@media (hover: hover) and (pointer: fine)` 内
- [ ] 只动了 transform/opacity

## F. 工程抽查（详见 engineering-checklist.md）

- [ ] 图标按钮有 `aria-label`；表单控件有 label；焦点可见
- [ ] 高频控件具备 default / hover / focus / active / disabled；focus 比 hover 更明确，不能只靠轻微颜色变化
- [ ] 弹窗：焦点陷阱 + Esc + 焦点返还；危险操作有确认/撤销
- [ ] 数字用 tabular-nums/等宽；标题 balance、正文 pretty
- [ ] 空态/加载态/错误态/成功态齐全；超长文本不破版
- [ ] 移动端：非对称布局塌缩单列；无 `h-screen`；无横向滚动条
- [ ] Mixed raster + Mermaid/SVG/canvas surfaces use a shared visual scale: comparable content width, readable labels, and balanced visual weight. Inspect rendered desktop and mobile output; static source checks are not visual verification.
- [ ] 暗色页有 `color-scheme` + `theme-color`

## G. 中文页追加项（页面含中文时必查，详见 chinese-typography.md）

- [ ] 中文正文/UI 用系统字体栈；装饰中文字体只在创意标题且已 `text=` 子集化
- [ ] 中文行高 ≥ 1.5；正文 ≥ 14px；字重只用 400/500/600
- [ ] 中西文之间、中文与数字之间有空格；数字与单位之间有空格（°、% 除外）
- [ ] 全角标点；暗色页正文 `rgba(255,255,255,.85)` 且对比度 ≥ 7:1

## H. 身份边界（详见 reader-surface-style-and-prose.md）

- [ ] 除非用户明确要求，无打赏二维码/公众号关注/浮条/个人 Profile 区块
- [ ] 对外分享页如需署名，最多低干扰页脚 `Powered by 向阳乔木`

## I. 三秒测试（最后一关）

眯起眼睛看整页三秒：

- [ ] 最重要的信息第一眼就在视线里吗？
- [ ] 页面在争夺注意力的元素 ≤ 1 个吗？
- [ ] 这一页**像不像 AI 做的**？像，就回到 A 节找出泄密点。

---

**通过标准**：适用项全部勾选。适用项差一条都不许说"基本完成"；不适用项标 N/A。
