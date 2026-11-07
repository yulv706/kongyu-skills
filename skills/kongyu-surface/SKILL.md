---
name: kongyu-surface
description: "流云展示. Visual display craft ONLY: UI/product page, layout, typography, hierarchy, responsive overflow, screenshot critique, visual anti-slop aesthetics, redesign, motion, Chinese typography, hand-drawn/animated architecture diagrams, or surface audit/design-DNA study from screenshot or URL. For report/汇报 requests route to kongyu-writing FIRST; use this skill only for the visual polish of an already-structured report. Do not let a bare report request trigger this skill."
---

# L1uyun Surface

Owns the **human display layer** (展示层): anything a limited-attention human must see, scan, trust, and act on. Not a general design methodology, not frontend engineering, not machine-document formatting.

Use when the real problem is the human-facing surface: layout, hierarchy, spacing, visual noise, repeated labels, control weight, screenshot ugliness, AI-slop aesthetics, motion on interactive surfaces, a service page that feels like backend forms, or a diagram humans must read (architecture, workflow, swimlane, topology).

## Audience gate（机器看机器该看的，人看人该看的）

Before applying this skill, classify the artifact audience:

| Audience | Typical form | Goal | Owner |
|----------|--------------|------|-------|
| Machine / agent | AI-facing Markdown, contracts, schemas, source facts, prompt packets | Maximize machine readability: flat structure, no decoration, field-aligned, high density | **Not this skill.** Use the contract skill, project source layers, or the report source layer. Do not impose visual hierarchy, line-height fashion, palette, or responsive layout on machine docs. |
| Human | HTML, product UI, workbench, settings, dashboards, report reader pages, style previews, architecture/workflow diagrams for humans | Minimize human cognitive entropy under fatigue, small screens, Chinese text, partial knowledge | **This skill** for display quality. Report *facts/structure* are not part of this skill. Diagrams use the Archscribe track in `references/archscribe-diagram.md`. |

Rules:

- [ ] If the primary reader is an LLM/tokenizer or another agent, **do not route here** just because the file is “a page of text.”
- [ ] If a deliverable has both layers (e.g. report `.md` source + human HTML), polish only the human layer here; keep the machine layer flat and undecorated.
- [ ] Never “beautify” a machine source to look like a human page, and never collapse a human page into inventory-style machine density without hierarchy.

## Routing

- [ ] Use for service pages, dashboards, workbenches, settings surfaces, forms, search pages, report reader pages (only after report structure/evidence has settled), screenshot critique, design direction selection, redesign, or any surface where visual/structural quality for humans is the blocker
- [ ] A bare 汇报/报告/HTML汇报/收口报告 request does not trigger this skill; come back only for the visual polish pass of an already-structured report
- [ ] A request to create or restructure a PPT/deck, or to review its story/content, routes to `kongyu-ppt` for audience/story/slide semantics first. A story-locked request that only asks for visual direction, page-family craft, diagrams, or rendered-surface polish stays here. Actual SVG/PPTX production belongs to `ppt-master`.
- [ ] Use for **audit** (只读打分/列 punch list) and **study** (从截图或 URL 抽设计 DNA / 可选锁定 design.md)：仍在本 skill；协议见 `references/review-protocols.md` §八 / §九。不立、不路由到独立 hallmark skill
- [ ] `brand` 绿场与「反 AI 味」交付前跑 `references/slop-gates.md`；结构多样性读 `references/divergence-playbook.md` §六
- [ ] Use for human-facing architecture / workflow / swimlane / topology diagrams (手绘架构图、动态架构图、Excalidraw 风格图、泳道图): stay in this skill; load `references/archscribe-diagram.md` and run the vendored engine under `archscribe/` — do **not** create a separate `archscribe` skill
- [ ] Do not use for pure data flow, API contracts, auth, deployment, server debugging, or AI-only Markdown/source formatting unless a human surface is the actual blocker
- [ ] Design direction selection with visual previews: this skill handles it; for prior requirement alignment use Grill, for code review of implemented design use the code review skill
- [ ] Report information structure / evidence / source-of-truth: not this skill; then return here for human HTML/UI surface quality
- [ ] Conversation-only interactive labs / adjustable simulators remain `visualize`; static Mermaid one-offs may stay Mermaid when that fully answers; publishable hand-drawn or animated diagram deliverables use the Archscribe track
- [ ] For a human-facing technical explainer built around a real mechanism, use the optional mechanism-as-explanation method below; keep source facts and instructional sequence with `kongyu-writing`, and do not create a separate skill for this visual technique

## Core principle

**Primary:** Minimize human cognitive entropy on the display layer so a real reader/user can understand, trust, navigate, and act.

- [ ] Design for real-world human use under ordinary constraints (small screens, Chinese text, keyboard focus, messy content, fatigue, partial knowledge)
- [ ] Audience first: machine artifacts stay machine-readable; human surfaces get hierarchy, grouping, contrast, and justified interaction — not the reverse
- [ ] Reader entropy, anti-AI-slop, Chinese typography, style preview, motion craft, and Vercel precision are means toward that goal; if a rule does not improve real-world comprehension, trust, action, or maintainability, weaken or delete it
- [ ] Reduce reader entropy before adding visual expression
- [ ] Prefer deleting, weakening, merging, or demoting UI entities over styling more entities
- [ ] Ban AI-slop patterns first (see references/ai-anti-patterns.md); run executable gates in references/slop-gates.md before brand/anti-slop handoff; prohibitions beat positive demonstrations for breaking model statistical inertia
- [ ] Break **structural** sameness on marketing/greenfield pages (divergence-playbook §六); colour-swaps of Hero→3-features→CTA are still AI
- [ ] After bans, supply the **mode** positive grammar (not every reference at once): tokenized spacing, restrained color roles, visible focus, consistent interaction states, and justified surface boundaries


## 解释性图示、交互与动画

进入已有结构的解释页面时，先明确读者应能回答或预测的问题；媒介选择沿用 `kongyu-writing/references/report/explainer.md` 的“减少歧义与选择表达形式”。关系用标注图，变量影响用交互，连续变化才用动画。不要给简单答案增加页面或视频。

每个控制项要改变对应的可见结果，说明量的含义、单位、范围及模型假设。动画提供暂停、重播或分步查看；必要信息不能只在运动中短暂出现。区分示例模型与实测结果，并按任务目标核对一次有意义的变化和一个边界状态。一次性教学产物采用最小可运行形式，持续需求出现前不增加应用壳或常驻服务。

### 机制即解释（可选）

当一个技术原理确实由部件及其因果关系构成时，可以把原理映射成一件可辨认、可观察的装置，让装置的运作直接呈现原理。先写清每个关键部件代表什么、它如何影响下一步；只有映射真实且有助理解时才采用，避免为了视觉效果硬造机械隐喻。

- 先确定可信的来源、参数或明确标注的示例模型，再设计部件和运动；读数、标签和动画必须与同一模型一致。
- 面向新手时，先说明当前步骤所需的部件和术语，再逐步展示因果或时间顺序；需要时同步高亮正在起作用的部件。
- 细节服务于识别部件、理解关系或观察变化。优先保证 1× 阅读清晰、移动端可读和运动可暂停/重播，不以零件数量或装饰密度作为质量指标。
- 核对关键关系、数值和边界状态；把已知事实、示例假设和简化之处区分清楚。视觉精细或运动可信不能替代事实核验。
- 如果机制映射会误导，或读者只需看懂静态关系，就改用标注图、短文或更简单的交互，不强行做成装置动画。

## Surface Mode（表面模式）

References are dialects, not parallel canons. After Audience gate, pick **one** mode before loading positive grammar. Chinese is an **overlay**, not a mode: any surface with CJK text still reads `references/chinese-typography.md` above Latin/Geist stacks.

| Mode | When | Primary positive grammar | Ban notes | Avoid loading as default |
|------|------|--------------------------|-----------|---------------------------|
| `shell` | product UI, settings, cloud, deploy/ops, developer console | `references/vercel-precision-system.md` | full bans; Geist dark `#000` canvas allowed | five-role full palette, brand Hero rules, Archscribe |
| `paper` | report/reader HTML, calm reading pages | `references/reader-surface-style-and-prose.md` + cool-white/paper preference | full bans; **no** Geist dark default | Geist dark tokens as page chrome |
| `brand` | landing, campaign, portfolio, expressive marketing | `references/divergence-playbook.md` + `references/style-preview.md` | full bans; pure-black canvas exception **off** | forcing Geist shell tokens |
| `workbench` | research/agent workbench, dense tools | `references/research-workbench-minimalism.md` + shell subset | full bans; Geist dark canvas allowed if product shell | brand maximalism |
| `diagram` | human architecture/workflow/swimlane figures | `references/archscribe-diagram.md` | diagram track rules | product page component recipes |
| `micro` | one component/state/spacing fix | only the relevant reference slice | only relevant ban rows | style-preview ceremony |

### Conflict arbitration order

1. Audience: machine → leave this skill
2. Entry size (`micro` … systematic review)
3. **Surface Mode** (table above)
4. Chinese overlay if CJK present
5. Bans (`references/ai-anti-patterns.md`) with mode exceptions
6. That mode's positive grammar
7. `brand`/反 AI 味：`references/slop-gates.md`（其它 mode：通用门或 N/A）
8. Preflight → polish-pass / audit / study only if needed

Mode-bound hard rules:

- `shell` / `workbench`: motion = Geist, 0ms first; **no** decorative press-scale on buttons; ease value + one-ease-family rule: ban list below
- `brand`: `references/motion-craft.md` press feedback and stronger expression allowed; centered-Hero exception: ban list below; pick a macrostructure family before colour (divergence §六); handoff through `references/slop-gates.md`
- `paper`: cool-white / paper; do not mix Geist dark chrome; XiaoLab shared paper tokens hard gate still applies on self-hosted pages
- When a comparison is requested and mode is `shell`/`workbench`, a precision direction may be useful; vary density/border/focus/layout grammar rather than requiring unrelated font families. An open direction alone does not require previews.

## Entry size gate

Do not run the whole design ceremony for every tiny change. Pick the smallest entry that protects real-world quality:

Verification scope follows the declared target surfaces. A desktop-only or Chrome PC deliverable gets desktop verification only; mobile checks are N/A unless responsive or mobile behavior is requested. Do not change viewports merely because a general preflight mentions small screens.

| Entry | Trigger | Required behavior |
|-------|---------|-------------------|
| Micro polish | One component, one state, one spacing/overflow/contrast issue | Inspect actual surface, apply the relevant reference only, verify the changed state |
| Existing page polish | Direction is settled; user asks 打磨/优化/反 AI 味/加动效 | Audit current page, keep shell consistency, change only the reader-visible bottleneck |
| Direction selection | User requests alternatives or an unresolved material brand decision needs their choice | `references/style-preview.md`; ordinary new UI/redesign uses the project style or a reasonable default |
| Report/reader artifact | Substantial standalone report/HTML/memo | Not this skill; visual surface quality routes back here |
| Systematic review | 交付前需要深度审查，或层次散/节奏乱 preflight 无法定位 | Run `references/review-protocols.md` polish-pass：四轮 pass（无障碍/AI 味/层次节奏/交互态）-> 聚合去重 -> 按 blocker/质量/打磨优先级修复 |
| Read-only audit | audit / 打分 / 只审不改 | `references/review-protocols.md` §八；对照 slop-gates + anti-patterns；不改代码 |
| Design DNA study | study / 抽 DNA / 参考截图或 URL | `references/review-protocols.md` §九；诊断后等待确认；可选 design.md |
| Desktop theme delivery | 桌面主题/壁纸/视觉合成交付（Rainmeter/Lively/komorebi 等） | **Hard gate (karma #414)**：宣称 done/applied 前必须读并通过 `references/engineering-checklist.md` §十一——每个工具本轮可运行证明 + 全帧截图检视，缺一不可 |
| Android / mobile shell | Android app 主题、DayNight、移动端 chat/settings 基础主题 | **Hard gate (karma #444)**：定基础主题前必须读并执行 `references/engineering-checklist.md` §十二——`values/` 默认浅色、暗色只进 `values-night/`、运行时验证 |

## Diagnosis output format

For existing page polish, direction selection, and substantial visual changes, output a one-line design read + three dials before writing design code or proposing changes. For micro polish, keep this internal unless the choice affects scope.

> 读取为：Mode=〈shell|paper|brand|workbench|diagram|micro〉；〈页面类型〉，面向〈受众〉，用〈气质〉语言，倾向〈设计系统或美学家族〉。

| 拨盘 | 1 | 10 | 说明 |
|------|---|----|------|
| 视觉冒险度 VARIANCE | 完美对称、可预期 | 艺术性混乱 | 布局不对称程度、美学冒险幅度 |
| 动效强度 MOTION | 纯静态 | 电影级编排 | 动画数量与复杂度 |
| 信息密度 DENSITY | 美术馆留白 | 驾驶舱满载 | 间距与数据密度 |

Show dials in Chinese to the user; English param names are internal execution fields only. Task-type inference:
- 功能页（表单/向导/设置/仪表盘）→ VARIANCE 4-6, MOTION 4-5, DENSITY 5-7
- 营销页（落地页/官网）→ VARIANCE 7-8, MOTION 6-7, DENSITY 3-4
- 个性页（作品集/品牌页）→ VARIANCE 8-9, MOTION 6-8, DENSITY 3
- 开放创意命题（404/活动页）→ VARIANCE 9-10, MOTION 8-9, DENSITY 2-3
- 信任优先（政务/金融/无障碍）→ VARIANCE 3-4, MOTION 2-3, DENSITY 4-5

Dials adjust aesthetic risk only; functional contract (what the page must let the user do) is never exempt.

## References (read narrowest relevant, by frequency)

**高频（按入口大小读取）：**
- [ ] `references/ai-anti-patterns.md` — AI 反套路禁令清单；输出前过一遍适用项，微调只查相关条目
- [ ] `references/slop-gates.md` — 交付前 yes/no 门禁表 + 六轴自检（吸收自 Nutlope/hallmark slop-test，MIT）；`brand`/反 AI 味必跑，其它 mode 跑通用门或 N/A
- [ ] `references/chinese-typography.md` — 含中文界面必读，优先级高于通用字体规则
- [ ] `references/color-palette-roles.md` — 选色/配色推导时读，五角色结构 + 6 套现成色板
- [ ] XiaoLab shell color hard gate: reuse live shared paper tokens; do not introduce cold gray-blue workbench backgrounds on self-hosted pages without explicit user direction (karma #307).
- [ ] `references/preflight.md` — 交付前门禁；按入口大小适用，微调只过相关节
- [ ] `references/review-protocols.md` — 系统化设计审查流程：发现提问、美学方向承诺、无填充、层次/节奏/交互态/无障碍、polish-pass；另含 **audit**（§八）、**study/DNA**（§九）和 **rendered re-review**（§十，吸收 Hallmark 的渲染后复审，MIT）；基线吸收自 Trystan-SA/claude-design-system-prompt

**中频（有具体场景才读）：**
- [ ] `references/motion-craft.md` — 有动画/过渡/交互反馈时读；含 sheet/drawer/drag/swipe 时再读「手势物理」节（非 Apple 视觉风格包）
- [ ] `references/archscribe-diagram.md` — 手绘/动态架构图、泳道图、系统拓扑、Excalidraw 交付；含布局选择、spec 流程、`archscribe/` 引擎命令；需要时再读 `archscribe/references/spec-format.md`
- [ ] `references/engineering-checklist.md` — 生产级表单/组件/页面时读；桌面主题（§十一）与 Android shell（§十二）交付硬门也在此文件
- [ ] `references/research-workbench-minimalism.md` — 科研/工作台页面读
- [ ] `references/vercel-precision-system.md` — 开发者工具、云服务、工作台、设置页需要极简精确；官方 Geist token/组件态机（https://vercel.com/design.md · design.dark.md）；或需用 Vercel 反向审视本体系时读
- [ ] `references/reader-surface-style-and-prose.md` — 自建页面读者表层 + 身份边界
- [ ] `references/divergence-playbook.md` — 多方向发散纪律 + **结构多样性**（§六：六轴指纹、同质反模式、域→三选宏结构；吸收自 Nutlope/hallmark structure，MIT）
- [ ] `references/design-systems-catalog.md` — 58 站设计系统索引 + 10 大原型表，需参考真实网站设计系统时读

**低频（出方案/选方向时读）：**
- [ ] `references/style-preview.md` — Phase 2 视觉方向预览和选择流程（含页面骨架模板）

## Diagram track (Archscribe, surface-owned)

When the deliverable is a **human-readable architecture/workflow diagram** (not a product page):

1. Read `references/archscribe-diagram.md` (narrow).
2. Run the vendored engine under `archscribe/` (Pillow default: PNG/GIF/Excalidraw; Chromium optional for SVG/MP4/HTML).
3. Prefer fixing the JSON **spec** over post-editing the raster.
4. Place durable figures under the owning project; keep non-preview scratch under `_tmp/<task-slug>/`. Any local preview must use a dedicated sanitized preview directory, never the project root or `_tmp` as its server root.

This is the same skill surface, not a second skill. Upstream MIT code lives in `archscribe/` with provenance in `archscribe/VENDOR.md`.

## Visual direction selection (when user needs to choose a style)

- Produce alternative previews only when the user requests a comparison or an unresolved material brand decision needs their choice. Use the smallest useful number of distinct mockups and mark a recommendation; follow `references/style-preview.md` on that route. Otherwise reuse the project style or select a reasonable default and complete the work without a visual-selection pause.
- Local preview gate: serve only the sanitized preview directory, bind to 127.0.0.1, record PID/port/directory ownership outside the served files, and stop/verify the process after use. Follow the privacy and cleanup gates in `references/style-preview.md`.
- Axis-level divergence is mandatory, scoped by Surface Mode; rules in `references/divergence-playbook.md` §六.
- Self-check: cover the colors — if you cannot tell the directions apart, redo.

## Anti-AI-slop prohibitions (high priority, enforced on every output)

Key bans (full list in references/ai-anti-patterns.md):
- ❌ 紫蓝渐变光晕 — use neutral base + single high-contrast accent
- ❌ 纯黑 #000000 as marketing/AI chrome — use Off-Black / Zinc-950 / Charcoal; Geist dark canvas `#000` is allowed for precision product shells (`references/vercel-precision-system.md`)
- ❌ 大标题渐变文字 (text-fill gradient)
- ❌ 全员玻璃拟态 — backdrop-filter only for genuine overlay semantics
- ❌ 居中 Hero as AI default — use split-screen, left-align + asymmetric whitespace, editorial grid; `brand` may center only when design read requires it
- ❌ 三等分卡片横排 — use 2-col zig-zag, unequal grid (2fr 1fr)
- ❌ 编号式 meta-label ("SECTION 01") — remove entirely
- ❌ 整数假数据 (99.99%, 50%) — use organic data (47.2%, ¥3,847)
- ❌ 创业烂梗名 (Acme, Nexus) — invent contextual brand names
- ❌ transition: all — declare per-property
- ❌ ease-in for UI — default cubic-bezier(0.23, 1, 0.32, 1); `shell`/`workbench` may use Geist cubic-bezier(0.175, 0.885, 0.32, 1.1); one ease family per view
- ❌ scale(0) entrance — start from scale(0.95) + opacity: 0
- ❌ italic in interface typography (CJK pseudo-italic renders ugly)

## Output behavior

- [ ] Diagnose the reader problem in concrete terms: what is visually too loud, duplicated, detached, or structurally confusing
- [ ] Prefer one primary work surface, one secondary rail, and one low-weight settings entry when applicable
- [ ] Keep recommendations executable: spacing, hierarchy, grouping, placement, and removal decisions
- [ ] When a page should preserve project shell consistency, do not invent a one-off global header language
- [ ] Mixed raster + Mermaid/SVG/canvas surfaces must use a shared visual scale: comparable content width, readable labels, and balanced visual weight. Verify rendered proportions on the declared target surfaces; use desktop and mobile only when responsive/mobile behavior is in scope. Static source checks are not visual verification.
- [ ] For a substantial new surface, redesign, or visual-quality claim, run the rendered re-review in `references/review-protocols.md` §十. Inspect the rendered image before accepting source-linter findings, then compare content kept, lost, or changed. A source reading or successful export is not this review.
- [ ] Visual expression should serve the page's purpose. Deliver when the functional, readability, layout, and agreed-style checks pass; a distinctive flourish or memorable point is optional.

## Verb / entry workflow

| Entry | Trigger | Flow |
|-------|---------|------|
| From scratch / redesign | new page, "重新设计", direction undetermined | Diagnose → use project style or choose a reasonable default → execute → relevant visual checks; add comparison and user selection only when requested or a material brand decision requires it |
| Polish mode | page exists and direction is settled ("打磨/优化这个页面", "反AI味", "加动效") | Do not overthrow; critique → polish → animate only if useful → harden → verify (`slop-gates` 适用项) → rendered re-review (`review-protocols.md` §十) |
| Audit (read-only) | "audit" / 打分 / 只审不改 / 列问题 | `references/review-protocols.md` §八：punch list only，**不改代码** |
| Study (DNA) | "study" / 抽 DNA / 参考截图或 URL 提取设计 | `references/review-protocols.md` §九：诊断 → 等确认 → 重建或锁定 `design.md`；禁止像素抄袭 |



## Self-evolution

Design preferences discovered during work (user corrections, confirmed victories) go to karma as feedback items, not a separate preference ledger. Karma triage routes design-specific feedback back to this skill for reference updates.

