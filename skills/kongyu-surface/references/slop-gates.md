# 交付前 Slop 门禁（Slop Gates）

> 吸收自 [Nutlope/hallmark](https://github.com/Nutlope/hallmark) `skills/hallmark/references/slop-test.md`（MIT），
> 重写为 surface 体系方言：保留可执行 yes/no 门禁，去掉 Hallmark 主题目录绑定与 stamp 品牌。
> 本文件是 **pre-emit 门禁表**，不是禁令叙述。禁令全文见 `ai-anti-patterns.md`；交付勾选见 `preflight.md`。

## 何时读

- Surface Mode = `brand` 的绿场页 / 落地页 / 营销页：交付前必跑
- 用户明确要「反 AI 味 / 打分 / audit」：必跑
- `shell` / `workbench` / `paper`：只跑 **通用门禁** + 本 mode 例外；不要把营销页宏结构硬套进工作台
- Micro polish：只查被改动轴相关的门（例如只改动效则只跑 Microinteractions）

**判断规则：** 按任务范围检查适用项。只有实际可读性、功能或约定风格未达验收要求时才阻断交付；主观分数或未约定的审美偏好不单独构成重做理由。只读审查报告发现，不自动转为修改任务。

---

## 六轴诊断（按需使用）

需要定位视觉问题或用户要求评分时，可按下列六轴打 1–5 分。评分只提供诊断线索；低分应对应具体观察及其影响，不设置最低分或强制重做次数。实际验收要求满足后即可交付，不为提高主观评分反复打磨。

| 轴 | 名 | 在问什么 |
|---|---|---|
| **P** | Philosophy | 有没有清晰立场，还是只是一副布局 |
| **H** | Hierarchy | 2 秒内能否分出主/次/辅 |
| **E** | Execution | 线宽、重音占比、换行、focus、对比是否到位 |
| **S** | Specificity | 像**这个 brief**，还是像谁都能套的通用页 |
| **R** | Restraint | 是否删掉了不赚位的装饰/重复/为 padding 而 padding |
| **V** | Variety | 与同项目上一页的**结构指纹**是否拉开（换色不算 variety） |

可选 CSS 戳记（便于同项目防同质；无强制路径依赖）：

```css
/* surface · macrostructure: Stat-Led · mode: brand
 * fingerprint: head-hanging / body-asymmetric / div-hairline
 * critique: P5 H4 E5 S4 R5 V5 */
```

---

## 通用门禁（所有 mode）

### 视觉

1. 展示字体是否是 Inter / Roboto / Open Sans / Poppins / Lato / 系统默认作为**营销页唯一**选择？（`shell`/`workbench`/`paper` 稳定中性字体豁免，但记忆点必须来自比例/边界/密度/focus，不是“换个安全英文字体就算个性”。）
2. 是否存在紫→蓝 / 青→品红渐变，**含** `background-clip: text` 渐变大标题？
3. 是否存在三等分卡片 + 上图标下标题的标准 feature 行？
4. 是否有卡片套卡片？
5. 卡片是否用粗彩色左右侧条（厚边条装饰）？
6. Hero 是否「全居中一条轴」：`min-height:100vh` 且 eyebrow + 标题 + lede + CTA **全部**叠在同一居中纵轴？（最多两个元素居中，其余必须破轴。`shell`/`workbench` 无营销 Hero 时本门 N/A。）
7. 营销/装饰面是否用纯 `#000` 或纯 `#fff` 作大面积底？（例外：`shell`/`workbench` 允许 Geist dark canvas `#000`；`paper` 允许 cool-white 纸面；`brand` 的 pure white 仅当明确 modern-minimal 纸感时。）

### 结构

8. 是否复用了通用 AI 模板 **Hero → 三 feature → CTA → footer**，或与同项目上一页**相同结构指纹**？
9. 各 section 是否只靠等距空白分隔、节奏完全同质（无线、无色阶、无节奏变化）？
10. 是否默认掉进「编辑式左栏编号 + 巨型衬线 + 非对称 span」而未被 brief 明确要求？（Specimen 坠落：默认禁止。）

### 微交互

11. 是否使用 `transition: all` / `transition-all`？
12. 是否对无关元素统一 `hover:scale-105`（或任意统一 hover-scale）？
13. UI 状态变化是否使用弹跳 overshoot easing？（overshoot 仅留给物理拖拽类交互。）
14. 同一元素是否叠了超过一种 hover 效果（translate + scale + shadow + color + rotate）？
15. 是否在动画 `width` / `height` / `top` / `left` / `margin` / `padding`？
16. focus ring 是否做成淡入动画？（focus 必须瞬时出现。）
17. 用户已能看见结果的操作，是否还弹庆祝式 success toast？
18. tooltip 的 hover delay 与 focus delay 是否相同？（hover 宜 800–1000ms；focus 应为 0。）
19. 自动轮播内容是否缺少 hover/focus 暂停？（WCAG 2.2.2）

### 内容

20. 是否出现 Jane Doe / John Smith / 张三，或 Acme / Nexus / Seamless / Unleash / 赋能 / 无缝 类陈词？

### 实现

21. 中性色是否完全零色度且读起来“塑料灰”？（极简 monochrome 产品壳可保留；营销页倾向给中性色极低 chroma 锚向。）
22. 重音色是否占据单视口面积约 >5%？（大色块填充不是重音。大气氛围页可放宽背景 bloom，但仍禁止渐变字与胶囊按钮渐变。）
23. padding/gap/margin 是否出现不在 4px 阶梯上的任意值（如 17px）？
24. 正文容器 `max-width` 是否明显偏离 45–75ch 可读区间？（工作台/表格全宽区 N/A，但说明文字列仍适用。）
25. 交互元素是否缺少 `:focus-visible` / `:active` / `:disabled` 中的任一？
26. 是否有 transform/animation 未覆盖 `@media (prefers-reduced-motion: reduce)`？
27. 是否用 `transition: all` 的同义词或未声明属性的大范围 transition 绕过第 11 门？

### 高频结构雷区

28. Section 眉批/编号是否与标题**同一行横排**（tag-left / header-right）？（禁止。眉批若用，只能同栏竖叠在标题之上；默认 eyebrow 配额仍见 `ai-anti-patterns.md`。）
29. 全大写展示标题是否 `line-height < 1.0`？（全大写下限 1.0，建议 1.02–1.08，防换行撞帽。）
30. 是否在已有 sticky 顶栏时，另有元素 `position:sticky; top:0` 与顶栏抢位？（次级 sticky 必须 `top: var(--banner-height)`，并分离 z-index。）
31. 是否每个 section 都有 eyebrow / “01 · FEATURES” 编号标签？
32. 是否所有 section 入场都是同一种 scroll fade-up？

### 中文叠加（含 CJK 时必查）

33. 是否对中文 UI 使用 italic / 伪斜体强调？
34. 是否加载未子集化的装饰中文 webfont 拖慢首屏？
35. 中文正文行宽/行高是否明显不可读（过宽长行、过紧行高）？（细则 `chinese-typography.md`）

---

## Mode 例外速记

| Mode | 放宽 | 收紧 |
|------|------|------|
| `shell` / `workbench` | 稳定中性字体；Geist `#000` canvas；无营销 Hero 时跳过 6/8 营销模板门 | 禁止营销 maximalism、禁止为 variety 而换花体字；记忆点来自精密边界 |
| `paper` | cool-white 纸面；阅读优先的单栏 | 禁止 Geist dark 装饰壳；禁止大动效秀 |
| `brand` | 大气氛围可允许背景径向 bloom | 强制结构多样性；强制跑满门禁；禁止 Specimen 默认坠落 |
| `diagram` | 本表大部分 N/A | 用 Archscribe 轨，不拿营销门禁套 SVG 图 |

---

## 与 preflight / review 的分工

| 工件 | 作用 |
|------|------|
| `ai-anti-patterns.md` | 禁令叙述 + 替代方案 |
| **本文件** | 交付前 yes/no 门禁扫表 |
| `preflight.md` | 总勾选（含功能契约、中文、身份） |
| `review-protocols.md` | 系统化审查流程 + **audit / study** 动词协议 |

`brand` 新页建议顺序：六轴自检 → 本表 → `preflight.md` 适用节 → 需要时 `review-protocols` polish-pass。
