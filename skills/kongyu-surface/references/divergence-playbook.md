# 发散手册（Divergence Playbook）

> 来源：多样性受控实验（任务 G）的直接发现——没有强制机制时，模型会给出
> "深空霓虹 / 黑白黑胶 / 荧光终端"这种看似不同、实则都在暗色酷炫舒适区的伪多样方案。
> 用途：Phase 2 出三套方案前、任何"给我几个方向/风格"的请求。

## 一、轴级差异检验（核心机制）

多个方向之间的差异必须发生在**轴**上，而不是同一条轴的不同刻度。

| 轴 | 两端 | 伪多样的表现 |
|----|------|--------------|
| 明度轴 | 亮底 ↔ 暗底 | 三个方向全是暗色 |
| 字体家族轴 | 衬线 ↔ 无衬线 ↔ 等宽 ↔ 展示体/手写 | 全是几何无衬线换个名字 |
| 色彩策略轴 | 单色克制 ↔ 双色对撞 ↔ 多色系统 | 全是"深底 + 一个荧光色" |
| 布局结构轴 | 对称网格 ↔ 编辑式不等比 ↔ 自由构成 | 全是居中卡片 |
| 密度轴 | 美术馆留白 ↔ 报纸密排 | 全是中等密度 |
| 时代气质轴 | 复古印刷 ↔ 当代极简 ↔ 未来科幻 | 全是"现代科技感" |
| 材质轴 | 平面 ↔ 玻璃 ↔ 纸质 ↔ 拟物 | 全是毛玻璃 |

**规则（按 Surface Mode）：**
- `brand` / 开放创意：任意两个方向之间至少 4 条轴取值不同，其中必须包含明度轴或时代气质轴之一；字体家族轴尽量互斥。
- `shell` / `workbench`：至少 **一个** 方向是 Geist/极简精确；其余方向允许在同一稳定字栈上，用密度、边界工艺、focus/交互态、布局语法、明度拉开差异——**不强制**字体家族互斥。任意两方向仍须在遮住颜色后可辨。
- `paper`：方向未定时优先 cool-white/paper 家族内比密度与层级，不默认甩出 Geist dark 产品壳。
- `micro` / 方向已定：不跑本手册全套发散。

## 二、强制自检三问

1. **遮住颜色还能区分吗？**（`brand`：布局和字体就该不同；`shell`/`workbench`：布局/密度/边界/focus 语法就该不同）
2. **有一个方向让你不舒服吗？** 三个方向都在自己审美舒适区 = 没有真正发散（`shell` 的「不舒服」可以是更密/更冷/更响的功能壳，不必是混乱美学）
3. **每个方向能一句话说出"它像什么杂志/店铺/年代/工具"吗？** 说不出 = 气质模糊

## 三、美学方向库（跳出舒适区用）

> 来源：frontend-design (Anthropic) 的方向词表 + 实验中出现过的高分方向

brutally minimal（残酷极简）· maximalist chaos（极繁混乱）· retro-futuristic（复古未来）·
organic/natural（有机自然）· luxury/refined（奢华精制，Art Deco 航空、香槟金衬线）·
playful/toy-like（玩具感）· editorial/magazine（编辑杂志，衬线斜体大字 + 细线）·
brutalist/raw（粗野主义，等宽 + 粗黑边框 + ASCII）· industrial/utilitarian
（工业实用，奶油纸底 + 印刷规则线）· soft/pastel（软糖粉彩）· constructivist
（构成主义，不等宽网格 + 大字装饰）· terminal/hacker（终端）· watercolor/craft
（水彩手作）· skeuomorphic/clay（黏土拟物）

**抽选纪律**：从库里选方向时，至少一个来自你上次没用过的类别。
跨项目跨生成禁止收敛到同一批安全选择——"每次都不一样"本身就是标准。

**掷骰子反惰性机制（吸收自 gpt-taste）**：LLM 天生会选"第一个想到的选项"。
选方向、字体、Hero 架构时，用确定性种子做一次伪随机（如：任务描述字符数 mod
候选数量），并在设计计划中写明掷骰结果。骰子选中舒适区之外的选项时，禁止悄悄换回。

**风格协议卡（深度协议挂载）**：方向若命中本地确实存在的完整风格协议，Phase 3 可以加载对应协议做深度约束；不存在就不要引用、等待或脑补。当前稳定来源是：
- 极简精确 / 开发者工具 / 工作台 → `vercel-precision-system.md`
- 真实站点族谱选择 → `design-systems-catalog.md`
- 中文读者表层 / XiaoLab 壳层 → `reader-surface-style-and-prose.md`
- 动效方向 → `motion-craft.md`

Phase 2 风格试衣间按 `style-preview.md` 的桌面 2×2 规则执行。正式多方向展示不是默认交付物；只有用户明确要“可分享/可展示的多方向页面”时，才做全宽沉浸带和更重的展示工艺。

## 四、方向呈现格式

每个方向必须给足以下四项，否则用户无法真正选择：

```
### 方向 X：〈方向名〉
- 一句话气质：像〈具体参照物：某类杂志/空间/年代〉
- 字体策略：〈展示体 + 正文体，具体到字体名〉
- 色彩策略：〈底色 + 重音色 + 策略类型〉
- 布局动作：〈这个方向最有辨识度的一个布局决定〉
- 记忆点：〈用户会记住的那一个东西〉
```

## 五、创意武器库（高端交互模式）

> 保留自 v1，用于给选定方向注入冲击力。一个页面最多 2-3 个，效果必须服务功能。

**导航/菜单**：Mac OS Dock 放大 · 磁吸按钮 · 液体分离粘性菜单 · Dynamic Island 药丸变形
**布局/网格**：Bento Grid · Masonry 瀑布流 · 分屏反向滚动 · 帷幕揭开 Hero
**卡片/容器**：视差倾斜（3D 跟随鼠标）· 聚光灯边框 · 真毛玻璃 + 内折射边 · 全息箔纸
**滚动**：粘性堆叠 · 横向滚动劫持 · 缩放视差 · SVG 路径自绘
**数据**：数字滚动计数器 · 缓动进度条 · 实时数据流轮播 · 呼吸状态指示器

性能约束：复杂动画隔离在独立组件；滚动侦听禁用裸 `window.addEventListener('scroll')`，
用 IntersectionObserver 或 CSS scroll-driven animations。

---

## 六、结构多样性（Structural Variety）

> 吸收自 Nutlope/hallmark `structure.md` / `macrostructures.md`（MIT）。
> **结构同质是 AI 指纹，不是视觉同质。** 换色不算发散；两个 brief 做出两套「Hero→三卡→CTA」仍是失败。
> 本节主要服务 Surface Mode=`brand` 与方向选择。`shell`/`workbench`/`paper` 用密度/边界/信息架构做差异，不要硬套营销宏结构。

### 6.1 结构指纹六轴

绿场 `brand` 页在动手前应能口头报出指纹（不必逐轴填表，但同项目相邻两页不得整表重合）：

| 轴 | 在选什么 | 默认避坑 |
|----|----------|----------|
| 1. 标题落位 | hanging / centered display / bottom-aligned / overlapping image / sticky / inline-with-body | 左栏编号眉批 + 标题横排（opt-in only）；默认 Speciman 左缘编号禁 |
| 2. 正文构图 | single column / two-col asymmetric / multi-col / marginalia / full-bleed reset / asymmetric spans | 假百科三等分等宽当默认 |
| 3. 分隔语言 | hairline / ornament / negative space / bleed-colour / rule+label | 全程等距空白、零节奏变化 |
| 4. CTA 形态 | solid button / typographic-only / inline text / sticky bar / dual split | 居中大 pill 当唯一 CTA 语法 |
| 5. 图像策略 | none / tightly cropped / full-bleed photo / diagram-led / product UI chrome | 假 3D 抽象渐变球 |
| 6. 动势语法 | static / fade-up once / horizontal sweep / sticky stack / typewriter | 每 section 同款 scroll fade-up |

### 6.2 结构同质反模式（直接否决）

- **SaaS Hero 模板：** 居中标题 + 居中副题 + 居中 pill CTA + 满屏 hero + 统一 fade-up
- **三 feature 行：** 三等分、上图标下标题下两行说明、相同 padding
- **利益列表 → 注册块：** 可预测的功能 bullet + Sign up
- **全员 fade-in：** 每块相同入场，像幻灯片
- **碳拷贝页脚：** Logo + 四列链接 + 社交行 + © 无信息架构差异

### 6.3 宏结构速选（brand；点名即可，勿整库搬运）

优先整页形状，而不是从零拼六轴。同项目连续输出避免落在同一族：

| 族 | 名称（报这个） | 何时 |
|----|----------------|------|
| 网格 | Bento Grid / Portfolio Grid | 多能力并陈、作品墙 |
| 数据 | Stat-Led / Workbench | 指标证明、产品控制台感营销 |
| 叙事 | Long Document / Letter / Quote-Led | 故事、公开信、引言驱动 |
| 海报 | Manifesto / Marquee Hero / Photographic | 运动主张、大标题、影像主导 |
| 索引 | Index-First / Catalogue / Ecosystem Index | 目录、清单、多入口发现 |
| 工具体 | Component Playground / Map-Diagram | 组件可玩、空间关系 |

**不要默认 Specimen**（编号左栏 + 巨型衬线编辑腔），除非 brief 明确要求编辑/铸字/specimen 气质。

### 6.4 域 → 三选一（方向未定时）

方向开放且 Mode=`brand` 时，按 brief 域词给出**三个不同族**的宏结构，让用户选或授权你选；禁止给三个近亲：

| 域词 | 三选 |
|------|------|
| 播客/音频/音乐 | Photographic · Quote-Led · Letter |
| 电商/商品 | Catalogue · Photographic · Bento Grid |
| 文档/CLI/SDK/API | Workbench · Long Document · Component Playground |
| B2B SaaS/平台/可观测 | Bento Grid · Workbench · Stat-Led |
| 工作室/案例集 | Portfolio Grid · Split Studio · Index-First |
| 个人单页/关于 | Long Document · Letter · Index-First |
| 餐饮/菜单 | Photographic · Long Document · Catalogue |
| 金融/支付 | Stat-Led · Workbench · Long Document |
| 运动/倡议 | Manifesto · Quote-Led · Stat-Led |
| 编辑/字体/杂志 | Specimen · Long Document · Type Specimen（仅此时 Specimen） |
| 无信号 fallback | Bento Grid · Long Document · Manifesto |

用户说「你定」：选与同项目上一戳记**族距离最远**的一项。用户只说「现代/干净/专业」：不算选型，用上表三选重问。

### 6.5 与 style-preview / 轴级差异的关系

- `style-preview` 管四方向**视觉试衣**；本节管**页面骨架族**不可撞车。
- 轴级差异检验（第一节）仍然有效：遮住颜色仍应可分。
- `shell`/`workbench` 四方向预览：至少一档 Geist/precision；其余用密度/边界/focus/布局语法发散，不强制宏结构三选秀。
