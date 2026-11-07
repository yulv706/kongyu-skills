# AI 反套路禁令（Anti-AI-Slop Patterns）

> 禁令比正面示范更能打破模型的统计惯性。Skill 的第一作用是"禁止"而非"教学"。
> 每条禁令附替代方案——光说"不要"不够，必须给出"用什么代替"。

## 视觉禁令

- ❌ 紫蓝渐变光晕（"AI 美学"头号标志）— 用中性底色 + 单一高对比重音色
- ❌ 纯黑 #000000 作营销/AI 装饰面 — 用 Off-Black / Zinc-950 / Charcoal；**例外**：官方 Geist dark 的 `background-100: #000000` 作为产品壳 canvas 合法（见 `vercel-precision-system.md`）
- ❌ 过饱和重音色 — 饱和度 < 80%，让重音色与中性色优雅融合
- ❌ 外发光 / 霓虹光晕 — 用内边框或微妙的色调阴影
- ❌ 大标题渐变文字（text-fill 渐变）
- ❌ 全员玻璃拟态 — backdrop-filter 只用在真正需要浮层语义的地方

## 字体禁令

- ❌ Inter / Roboto / Arial / 系统默认作为唯一选择（营销/创意页的 AI 默认偏好）— 用有态度的字体：
  展示体 + 正文体配对，且每次生成都换，禁止跨项目收敛到同一套安全选择
  （Space Grotesk 用滥了也算违规）
  豁免：生产级产品壳、工作台、设置页、中文 UI 可以使用稳定中性字体系统；此时记忆点必须来自比例、边界、密度、focus、交互一致性，而不是“换字体”。
- ❌ 斜体（italic）— 界面排版禁用斜体，中文尤其（CJK 伪斜体渲染丑陋且不和谐）。
  强调一律用字重、颜色、字号或下划线装饰，不用 font-style: italic。
  唯一豁免：英文长引文的书目惯例，且需设计读取明确支持
- ❌ 装饰性中文 webfont 滥用（ZCOOL 系列、全量思源等）— 用户没装、CDN 拖慢首屏
  （中文字体 5-20MB）。中文正文/UI 一律系统栈；"每次生成都换字体"的个性要求
  通过西文/数字展示字体、中文字重与排版结构实现。装饰中文字体仅限创意展示页
  标题短语且必须 text= 子集化——详见 chinese-typography.md
- ❌ 数据 UI 用衬线 — 技术界面只用高质量无衬线 + 等宽
- ❌ 靠字号砸层级 — 用字重、颜色、字距控制层级，不是无脑放大 H1

## 布局禁令

- ❌ 居中 Hero（AI 默认）— 用分屏、左对齐 + 非对称留白、编辑式网格；Surface Mode=`brand` 且设计读取明确要求时可居中
- ❌ 三等分卡片横排 — 用 2 列 Zig-Zag、不等比网格（2fr 1fr）、横向滚动
- ❌ 卡片当分组的万能药 — 优先 border-t / divide-y / 纯留白；只在需要
  z 轴层级时用卡片
- ❌ 每个 section 都有一个小标签眉批（eyebrow）— 眉批数量 ≤ ⌈section 数 / 3⌉
- ❌ 编号式 meta-label（"SECTION 01"、"QUESTION 05" 式标签）— 廉价感，整体删除
- ❌ 窄容器多行大标题 — H1 不超过 2-3 行：用宽容器（max-w-5xl+）+ clamp() 字号
  让文字横向流动，4 行以上即失败
- ❌ Bento 网格留空洞 — grid-auto-flow: dense + 数学验证 col-span/row-span
  完全咬合；卡片 3-5 张精雕胜过 8 张潦草

## 内容禁令

- ❌ 通用占位名（John Doe、张三）— 用有真实感的名字
- ❌ 整数假数据（99.99%、50%、1234567）— 用有机数据（47.2%、¥3,847）
- ❌ 创业烂梗名（Acme、Nexus、SmartFlow）— 发明有语境的品牌名
- ❌ AI 文案陈词滥调 — 禁用"革命性 / 颠覆 / 无缝 / 释放 / 赋能 / 下一代"；
  用具体动词和可验证的事实
- ❌ 中文文案滥用破折号和感叹号 — 一页最多一个感叹号

## 动效禁令（详见 motion-craft.md）

- ❌ transition: all — 逐属性声明
- ❌ ease-in 用于任何 UI 动效 — 用强化 ease-out：cubic-bezier(0.23, 1, 0.32, 1)
- ❌ 从 scale(0) 入场 — 从 scale(0.95) + opacity: 0 起
- ❌ 键盘触发的高频操作加动画 — 每天用一百次的东西不许动
- ❌ UI 动效超过 300ms
- ❌ 无 prefers-reduced-motion 兜底
- ❌ hover 动效不包 @media (hover: hover) and (pointer: fine)

## 自检方法

遮住颜色，三个方案还能被区分吗？不能就重来。颜色是最容易做表面差异的维度，
也是最容易让多方向坍缩成同一方案陷阱的维度。

禁令之后必须有正面工艺：如果页面只是没有渐变、没有玻璃、没有三卡片，但边界、spacing、字重、focus、交互态仍是随手值，它仍然是 AI 味。开发者工具/工作台用 `vercel-precision-system.md`（官方 Geist design.md / design.dark.md）补齐这套正面语法。

## 结构同质禁令（比换色更致命）

> 视觉可以不同，结构仍然可以是 AI。完整门禁表见 `slop-gates.md`；宏结构选择见 `divergence-playbook.md` §六。

- ❌ **Hero → 三等分 feature → CTA → footer** 作为默认骨架 — 先选宏结构族（Bento / Stat-Led / Long Document / Manifesto…），再填内容
- ❌ **同项目多页只换色板** — 换结构指纹（标题落位 / 正文构图 / 分隔语言 / CTA 形态至少动两轴）
- ❌ **Specimen 坠落**：未要求编辑/铸字气质时默认「左栏编号 + 巨型衬线 + 标签旁置标题」— 仅 opt-in
- ❌ **眉批与标题同一行横排**（tag-left / header-right）— 眉批只能同栏竖叠；默认 eyebrow 仍受配额约束
- ❌ **每个 section 同款 scroll fade-up** — 动势语法每页最多一套主语法，其余静态或局部

## 与 slop-gates 的关系

- 本文件：禁令 + 替代（读得懂、记得住）
- `slop-gates.md`：交付前 yes/no 扫表（跑得完、可判过）
- 新 `brand` 页与「反 AI 味」请求：先过 slop-gates，再勾 preflight
