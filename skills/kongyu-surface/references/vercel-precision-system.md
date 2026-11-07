# Vercel / Geist 精确系统（官方 DESIGN.md 迁移）

来源（权威，优先于第三方反推）：
- Light: https://vercel.com/design.md
- Dark: https://vercel.com/design.dark.md

名称：Geist（Vercel design system）  
版本声明：`version: alpha`  
本地对齐日期：2026-07-15  

旧第三方反推（educlopez/design-bites）仅作历史对照，**执行时以官方 dual URL 为准**。使用方式：当作可迁移的工程化极简样本与 token 源，不是品牌法典。

## 何时读

- Surface Mode = `shell` 或 `workbench`（见 skill 主文 Surface Mode 表）时作为**正面语法主读**。
- 开发者工具、科研/Agent 工作台、云服务、设置页、表单、文档型产品、部署/运维后台需要「精确、可信、低噪音」时。
- 页面已通过反 AI 味禁令，但仍显得空、散、廉价、像 backend form 时。
- 需要 light/dark 成对 token、button/input 态机、focus ring、spacing/radius 硬值时。
- 审视本 skill 自身规则是否过度追求「有记忆点 / 换字体 / 配色完整」，反而破坏产品壳一致性时。

不用于：摄影/品牌沉浸页、暖色编辑式文章、强人格表达页、需要亲和插画或消费级情绪的页面。  
不覆盖：报告 paper 壳（cool-white / Archscribe `paper`）、中文排版（`chinese-typography.md`）、手势/抽屉物理（`motion-craft.md` 手势节）。

## 核心模型

Geist 的可迁移价值不是「黑白好看」，而是「每个可见选择都有工程理由」：

1. **灰阶意图阶梯**：`gray-100`…`gray-1000` 编码状态意图，不是随便挑一档浅深。
2. **background 与 gray 分离**：`background-*` 是页面/卡片面；`gray-*` 是文字、不透明填充、语义边界。
3. **颜色只承担语义**：accent 给 link / focus / 单一主操作；状态色小尺度出现。
4. **边界与 elevation 克制**：层级先靠色阶与边，阴影保持轻。
5. **组件 token 化**：button/input 有高度、圆角、padding、typography 配方，不手写随手值。

禁令清单只告诉你不要渐变/玻璃/三卡片；本文件补上**替代语法**。

## Gray 意图阶梯（官方）

每档非 background 色阶（gray / blue / red…）统一语义：

| Step | 意图 |
|------|------|
| `100` | default background |
| `200` | hover background |
| `300` | active background |
| `400` | default border |
| `500` | hover border |
| `600` | active border |
| `700` | solid fill, high contrast |
| `800` | solid fill, hover |
| `900` | secondary text and icons |
| `1000` | primary text and icons |

`background-100`：主页面与卡片面。  
`background-200`：仅作**细微分区**，不作通用大填充。  
`gray-alpha-*`：半透明，叠在任意底上做 border / divider / overlay / hover。  
实心 `gray-*`：文字与不透明填充（对比稳定）。

## 核心 token 对照（精简）

执行时优先用 token 名；hex 供落地 CSS。完整表以官方 design.md 为准。

### 语义角色

| 角色 | Light | Dark |
|------|-------|------|
| primary（主文字/主填充语义） | `#171717` | `#ededed` |
| secondary | `#4d4d4d` | `#a0a0a0` |
| tertiary / accent 蓝 | `#006bff` | `#006efe` |
| neutral 面 | `#f2f2f2` | `#1a1a1a` |
| background-100 | `#ffffff` | `#000000` |
| background-200 | `#fafafa` | `#000000` |

### Gray 阅读与面

| Token | Light | Dark |
|-------|-------|------|
| gray-100 | `#f2f2f2` | `#1a1a1a` |
| gray-200 | `#ebebeb` | `#1f1f1f` |
| gray-300 | `#e6e6e6` | `#292929` |
| gray-400 | `#eaeaea` | `#2e2e2e` |
| gray-500 | `#c9c9c9` | `#454545` |
| gray-600 | `#a8a8a8` | `#878787` |
| gray-700 | `#8f8f8f` | `#8f8f8f` |
| gray-800 | `#7d7d7d` | `#7d7d7d` |
| gray-900 | `#4d4d4d` | `#a0a0a0` |
| gray-1000 | `#171717` | `#ededed` |
| gray-alpha-400（默认半透明边） | `#00000014` | `#ffffff24` |

### Accent / 状态（常用）

| Token | Light | Dark | 用法 |
|-------|-------|------|------|
| blue-700 | `#006bff` | `#006efe` | link、主 accent 实心、light focus 外环 |
| blue-900 | `#005ff2` | `#47a8ff` | dark focus 外环用 dark 的 blue-900 |
| red-800 | `#ea001d` | `#e2162a` | destructive button 填充 |

Accent 全阶（blue/red/amber/green/teal/purple/pink 各 100–1000 + P3 oklch）只在需要状态面时查官方文件；默认产品壳不铺满。

### Spacing / Radius

```
spacing base: 4px
scale: 4, 8, 12, 16, 24, 32, 40, 64, 96
节奏: 组内 8 · 组间 16 · 区块 32–40
卡片 padding: 24（compact 16 · hero 32）
内容列: 居中 max 1200px；宽工作台可到 1400px
breakpoints: sm 401 · md 601 · lg 961 · xl 1200 · 2xl 1400

rounded.sm: 6px   # 日常控件与表面
rounded.md: 12px  # menu / modal
rounded.lg: 16px  # fullscreen
rounded.full: 9999px  # pill / avatar
```

同一视图只保留**一个圆角家族**，不混圆角与直角。

### Elevation（官方）

层级优先靠 tonal surface + border；阴影保持轻。

**Light**

- Raised cards: `0 2px 2px rgba(0, 0, 0, 0.04)`
- Popovers / menus: `0 1px 1px rgba(0,0,0,.02), 0 4px 8px -4px rgba(0,0,0,.04), 0 16px 24px -8px rgba(0,0,0,.06)`
- Modals: `0 1px 1px rgba(0,0,0,.02), 0 8px 16px -4px rgba(0,0,0,.04), 0 24px 32px -8px rgba(0,0,0,.06)`

**Dark**

- Raised cards: `0 1px 2px rgba(0, 0, 0, 0.16)`
- Popovers / modals: 与 light 同结构的多层 shadow（官方 dark 文案同值）

Tooltip 用最轻一档。Elevation 与 radius 成对使用。

### Focus ring

| Theme | box-shadow |
|-------|------------|
| Light | `0 0 0 2px #ffffff, 0 0 0 4px #006bff`（surface 色缝 + blue-700） |
| Dark | `0 0 0 2px #000000, 0 0 0 4px #47a8ff`（surface 色缝 + blue-900） |

所有可交互元素在 `:focus-visible` 显示；禁止去掉 outline 却不给可见替代。

## Typography tokens（结构）

官方家族：Geist Sans（UI/prose）、Geist Mono（code/data/tabular）。

| 族 | 用途 | 字重习惯 |
|----|------|----------|
| heading-72 … heading-14 | 标题；字号越大 letter-spacing 越紧 | 600 |
| label-20 … label-12 | 单行可扫：导航、表单 label、表头、meta | 400 |
| copy-24 … copy-13 | 多行正文，行高更高 | 400 |
| button-16 / 14 / 12 | 按钮与紧凑控件 | 500 |

默认正文/控件：`copy-14`、`label-14`。数字对齐用 `*-mono` + tabular figures。

**中文界面不照搬 Geist 字栈。** 中文正文/UI 服从 `chinese-typography.md`：系统中文字体栈、足够行高、400/500/600。Latin、数字、代码、标题 Latin 部分可借 Geist-like 气质。不要在中文 UI 上套 Title Case。

## Components 态机

默认 medium 高度 **40px**；small **32px**；large **48px**（large 按钮用 `button-16`）。

| 变体 | 配方 |
|------|------|
| Primary | 实心 `gray-1000` 底 + `background-100` 字；视图上**唯一**最重要操作 |
| Secondary | `background-100` 底 + 半透明 `gray-alpha-400` 边 |
| Tertiary | 透明底 + `gray-1000` 字；hover 用 `gray-alpha` 轻染 |
| Error | 实心 `red-800` + 白字；破坏性操作 |
| Input | `background-100` 底、半透明边、`rounded.sm`（6px） |

交互阶梯：

- fill：`100` → hover `200` → active `300`
- border：`400` → hover `500` → active `600`
- disabled：`gray-100` 底 + `gray-700` 字 + `cursor: not-allowed`
- focus：上表双环

功能页按钮/链接不要用 scale、漂移、发光证明「高级」；高频 UI 优先改 `background-color` / `color` / `box-shadow`。Ghost 导航：默认透明，hover 到 gray-200 区，字从 secondary 升到 primary。

## Motion（官方 Geist）

- 动效只澄清状态变化，不做装饰。
- **多数交互优先 `0ms`**（尤其每日高频）。
- 需要动时：easing `cubic-bezier(0.175, 0.885, 0.32, 1.1)`；约 **150ms** 状态切换、**200ms** popover/tooltip、**300ms** overlay/modal。
- 禁止长循环、抢注意力动画；遵守 `prefers-reduced-motion`。

与 `motion-craft.md` 的关系（Surface Mode 绑定）：

- Mode `shell` / `workbench`：**必须** Geist 曲线与 0ms 优先；按钮不用 press-scale。
- Mode `brand`：短交互可用 `motion-craft` 默认 ease 与按压缩放。
- sheet / drawer / drag / swipe 不论模式仍读 `motion-craft.md` 手势物理节。
- 同一视图只保留一条招牌 ease，不混 `0.23,1,0.32,1` 与 Geist `0.175,0.885,0.32,1.1`。

## Voice & Content（中英分流）

官方英文纪律（产品文案为英文时直接用）：

- Labels / buttons / titles / tabs：**Title Case**；body / helper / toast：**sentence case**。
- 动作名 = 动词 + 名词（`Deploy Project`），不用光秃 `Confirm` / `OK`。
- 错误 = 发生了什么 + 下一步。
- Toast 写清对象、去掉句号、不写 `successfully`。
- 空状态指向第一个动作；进行中用现在分词 + 省略号字符（`Deploying…`）。
- 用数字、弯引号、省略号字符；少用 please 与营销最高级。

**中文界面：** 继承精确、可执行、无成功套话；不套 Title Case；按钮用完整动宾（「部署项目」「删除成员」）；错误仍写现象 + 下一步。

## Do / Don't（官方 + 我们的边界）

Do：

- 用 gray 阶梯排信息：`1000` 主文、`900` 次文、`700` disabled。
- 实心 accent 只给状态与**单一**主操作。
- WCAG AA（正文对比 ≥ 4.5:1）。
- 用 typography token，不手写 size/line-height/weight 散值。
- 状态不单靠颜色，配 icon 或文案。

Don't：

- 把 `background-200` 当通用大底。
- 混圆角家族，或一视图超过两个字重。
- 把 `gray-*` 与 `background-*` 互换使用。
- 为「完整五角色」在极简壳上硬加 highlight / 第二主色（见 `color-palette-roles.md` 折叠模式）。

我们的边界：

- 报告 / 读者 HTML 默认 paper cool-white，不因本文件改成 Geist dark。
- Archscribe 新图默认 `style=paper`；已有 dark 图用户认可则不动。
- 纯黑：`ai-anti-patterns` 对营销/AI 装饰页仍禁纯黑块；**Geist dark 的 `background-100: #000000` 作为 canvas 合法**。

## 反向审视我们的体系

- 反 AI 味不能只靠禁令。禁完渐变、玻璃、居中 Hero 后，必须落到 token 边界、可见 focus、稳定字重、可复用 spacing。
- `color-palette-roles.md` 五角色在极简精确模式可折叠为「灰阶 + 一个交互 accent + 小状态色」。
- 「每次换字体」只适合一次性创意方向；产品壳要稳定字体系统。
- 「每页一个记忆点」可以是数学留白、密度、双环 focus、极窄色彩配额，不必加装饰。
- 设计预览里，开发者工具/工作台任务至少考虑一个「极简精确 / Geist」方向；不用则说明输给谁。

## 快速执行清单

- [ ] 是否走极简精确壳（而非报告 paper / 品牌沉浸）？
- [ ] 颜色是否压到灰阶 + 一个交互蓝 + 小状态点？
- [ ] light/dark 是否用同一 token 名、不同值？
- [ ] 容器边界是否有存在理由？能否用留白或 divide 替代？
- [ ] 控件高度 32/40/48、圆角 6/12/16、gap 是否落在 4px scale？
- [ ] 字重是否克制（中文 400/500/600；无伪斜体）？
- [ ] hover / focus / active / disabled 是否走 100–600 阶梯 + 双环 focus？
- [ ] 动效是否 0ms 优先，需要时才 150/200/300 + 官方 easing？
- [ ] 中文文案是否精确可执行，且未误套 Title Case？
- [ ] 记忆点能否用「精确纪律」命名，而不是装饰物？

## 刷新方式

官方为 alpha，token 会变。需要刷新时：

```text
GET https://vercel.com/design.md
GET https://vercel.com/design.dark.md
```

对比本文件「核心 token 对照」与 Components / Focus / Motion 段；只更新漂移的硬值与意图表，不整文件 vendor 17KB YAML 进 skill。
