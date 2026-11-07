# 审查协议库（Review Protocols）

> 来源：Trystan-SA/claude-design-system-prompt 的 7 个审查/流程 skill（accessibility-audit、interaction-states-pass、hierarchy-rhythm-review、polish-pass、discovery-questions、frontend-aesthetic-direction、content principles）。
> 本文件只吸收我们已有 references 未覆盖的结构化审查协议骨架，不重复 ai-anti-patterns / engineering-checklist / motion-craft / color-palette-roles / preflight 已有的具体规则。
> 这些协议的差异点：它们是**全表面设计审查流程**（按 phase 走、聚合发现、逐条修复），而 preflight 是交付前门禁清单（勾选式），engineering-checklist 是代码审查（file:line 式）。三者互补：preflight 管"能不能交"，engineering-checklist 管"代码对不对"，本文件管"设计好不好"。

## 何时读

- 需要对一个已有页面做系统化设计审查（不只是反 AI 味、不只是工程验收）时
- 新项目 kickoff 需要结构化提问协议时
- 无品牌/无设计系统的 greenfield 需要承诺美学方向时
- 交付前需要跑一轮 umbrella 审查（polish-pass）而非只过 preflight 时
- 审查发现"层次散/节奏乱"但 preflight 的逐条勾选无法定位问题时

不用于：单个组件微调（读 preflight 相关节即可）、纯代码审查（用 engineering-checklist）、配色审查（用 color-palette-roles）。

---

## 一、发现提问协议（Discovery Questions）

> 用于新/模糊设计任务的 kickoff。坏设计来自缺失上下文，不是缺失技能。

### 先读已有材料

提问前读所有附件：代码库、截图、品牌指南、链接的设计系统、brief。用户刚附了品牌指南你还问"有品牌指南吗"是最快失去信任的方式。

### 是否该问

该问：已有材料无法解决、且会改变交付目标或实质品牌决策的问题。新页面、未指定风格或变体数量本身不要求提问。
不该问：用户给全了；小调整或后续跟进；范围/受众/约束明确；"照着这个原样复制"。
常规、可逆的视觉选择使用项目风格或合理默认；只有必须由用户决定的问题才等待回复。

### 问题集构成

**按实际缺口选用的问题示例，不是必问清单：**
- 起始点：先检查已有 UI kit、设计系统、品牌指南或截图。没有参考时可选择合理默认，不为从零设计额外请求确认。
- 变体：整体要几个？在哪些轴上（视觉/布局/交互/文案/语气）？特定元素要几个变体（"几个 hero？"）？
- 新颖度：循规蹈矩、创意突破、还是混合？
- 微调：最终设计里什么要可实时调整（颜色/文案/布局/组件）？
- 聚焦轴：流程、文案、还是视觉——探索精力放哪？

**特定问题示例**（仅在答案影响交付时选择）：
- 幻灯片：受众和知识水平；时间预算/页数；语气；演讲者备注；现有源材料？
- 落地页：期望用户动作；主要 persona；欣赏/拒绝的参考；移动优先还是桌面优先？
- 原型：流程和屏幕；hi-fi 还是 mid-fi；设备框；目标态；样例数据？
- 品牌/美学：三个形容词；欣赏的设计（及具体欣赏什么）；禁区；行业上下文？

不设问题数量配额。已有信息足够完成任务时直接执行。

### 格式

如果当前工具支持 request_user_input：用它，渲染原生表单组件。按最重要优先排序——表单流式加载，用户可以在其余加载前开始回答。标题简短；副标题可选。
不支持时：在对话中一次性提出所有问题（分批不超过 10-15 个），不要逐轮问。

### 反模式

- 别跳过实质决策缺口，也别把普通设计任务变成访谈
- 只问阻碍当前交付的最少问题，不以问题数量衡量对齐质量
- 别问能推导的东西——品牌指南里有主色就别问主色

---

## 二、美学方向承诺（Frontend Aesthetic Direction）

> 用于无品牌/无设计系统的 greenfield。在 hi-fi 之前承诺美学方向，否则 hi-fi 从零开始是最快通往 AI 模板的路。

### Phase 1：确认确实没有已有上下文

再查一遍：没有品牌指南、没有已有 app/产品要匹配、没有用户想模仿的参考站、代码库里没有部分设计系统。有任何一个 -> 停下来用它。美学方向只给真正的 greenfield。

### Phase 2：发现意图

问用户（或确认已说的）：**三个形容词**描述期望感觉；**受众**；**行业上下文**；**欣赏的参考设计**（及具体欣赏什么——字体/间距/颜色/语气/密度？）；**禁区**美学或套路。
用户要求比较或实质品牌决策需要选择时，给出少量方向及推荐；其它情况下由代理选择合理默认并继续。

### Phase 3：逐轴承诺——具体化

"现代简洁"这种模糊声明产出通用设计。在每条轴上具体承诺：

**字体**：挑**具体的**字体——标题、正文（常同族）、需要的等宽——带字重和字号阶梯。1-2 族最多。避开用滥的默认（Inter/Roboto/Arial/Fraunces/裸系统栈）。有意地选：humanist sans（Sohne、Suisse）、modern serif（Tiempos、GT Sectra）、editorial classic、typewriter mono、geometric sans。付费字体够不着时命名最近的免费替代。

**色彩**：选色调——暖（奶油/金/陶土）、冷（灰/石板/冰/蓝）、中性（混凝土/炭/灰白）。然后选：主品牌色（带明暗变体）、至多一个 accent、语义色（success/warning/error/info）、对应色调的 5-10 级灰阶。从零建时用 oklch() 保持和谐。微妙调白/黑——纯 #FFFFFF/#000000 刺眼。

**密度**：选间距阶梯（4px 或 8px base）和密度——紧（紧凑仪表盘、密集数据 UI）、正常（典型产品 UI）、松（编辑式、营销、高端、慷慨留白）。密度是感受到的，不只是看到的。

**圆角和阴影**：锋利（0-2px——实用/粗野/编辑式）、柔和（4-8px——典型现代产品）、或 pill/全圆（活泼/友好/消费级）。阴影同理：锋利/柔和/无。一套 elevation 系统，不混。

**组件风格**：filled/ghost/outlined/elevated。选默认，用次要风格做层次。

**图像和图标**：真实摄影、专业插画、来自成熟集的图标（Feather/Material/Phosphor/Heroicons）、或诚实占位符。避免手绘 SVG 插画。

**动效**：安静（只状态切换，200ms ease）、表达（入场动画、滚动驱动揭示）、或活泼（弹簧、hover 微交互）。承诺一种模式——混合动效显得无意。

### Phase 4：记录方向

需要保留的设计决策写在相关源码注释或项目已有设计文档中，简要记录字体、色彩、密度及必要取舍。仅当用户明确需要时，才在页面上展示“设计系统摘要”；普通产品页面不自动添加设计过程或实现说明，也不为该摘要单独新建文档。

### Phase 5：应用、测试、保持一致

用选定方向实现并检查实际表面。仅在用户要求比较或仍有实质品牌决策时暂停选择；普通交付继续完成，收到新反馈再修订相关部分。

后续设计引用方向的 token，不引用新的 inline 值。新设计需要未定义的值时，**先加到方向里**，再用。

---

## 三、内容原则——无填充（No Filler）

> 每个元素必须赢得自己的位置。不传达本质信息、不推进叙事、不创造必要视觉结构的，删掉。一千个 no 换一个 yes。

### 什么算填充

**占位/假内容**：Lorem ipsum 放在真实文案位置。编造的统计（"47% 的用户"）。没有目标的"了解更多"按钮。无功能装饰性分割线。并不真的要来的"即将推出"区块。

**不必要区块**：deck 已经覆盖了收益还加"为什么选我们"slide。只有两条弱证言却加"精选证言"。团队不相关的页面加"认识团队"。导航重复。

**冗余元素**：标题 + 副标题 + 段落说同一件事。三个"注册"按钮做同一动作。图标重复文字已说的。

**装饰性杂物**：无目的背景图案。纯为色彩的 emoji。感觉像拖延而非呼吸的大块留白。不改善设计的渐变遮罩。

**数据填充**：不支持信息的无意义数字（"Since 2019"、"99.9% uptime"）。数据点过多的图表。没人读的列的表格。10 项的 bullet list 而 3 项就够。

### 五问测试

对页面上每个元素问：
1. 它回答用户实际有的问题吗？（否 -> 删）
2. 它推进叙事吗？（否 -> 删）
3. 没有它用户能理解页面吗？（能 -> 删）
4. 有更清晰简洁的方式说这个吗？（有 -> 这样做，删其余）
5. 它服务用户还是服务设计师？（设计师 -> 删）

### 加之前先问

如果觉得额外区块/文案/内容会改善设计，**先问用户**。他们比你更懂受众和目标。不要单方面扩大范围。
区块感觉空是布局问题，不是内容问题。用构图解决，不是发明内容。空白不是失败——是呼吸空间。

---

## 四、层次与节奏审查（Hierarchy and Rhythm Review）

> 层次引导视线（什么先看、第二看、第三看）；节奏让设计显得有意（重复 + 策略性变化）。两者对了，设计扫描起来毫不费力。

### Phase 1：识别审查表面

审查用户刚编辑/问起的 HTML/CSS 文件；否则本 session 修改过的文件；不清则问。读文件和引用的样式，记录媒介（slide/page/mobile/dashboard）——规则因上下文而异。

### Phase 2：两轮审查

**Pass 1：层次审查**（每个屏幕/slide/主要区块）：

1. 主/次/三。什么该先看、第二看、第三看？说不出来 = 层次破了。
2. 字号。标题明显大于正文；primary CTA 大于次要操作。标记相似内容在差异很大的字号（不一致）和不同重要性的内容在相似字号（扁平）。
3. 颜色。主操作在饱和品牌色，次要在中性，弱化在浅灰。标记全同色（无信号）和不重要元素最亮（错误信号）。
4. 字重。标题 bold，正文 regular，说明 light。标记全 bold 和全 regular。
5. 位置。LTR 语言视线从左上开始；最重要的内容在黄金位置。标记主元素被埋在右下。
6. 密度。松间距信号"注意这里"，紧间距信号"辅助内容"。标记重要内容被挤而填充内容在呼吸——反了。
7. 五秒测试。新用户应在 5 秒内知道看什么、做什么。

**Pass 2：节奏审查**（整个文档）：

1. 间距阶梯。所有 padding/margin/gap 值对齐到一致阶梯（4px 或 8px 倍数）。列出隐式使用的阶梯，标记离群值（padding: 7px、gap: 13px）。
2. 字号阶梯。标记任意尺寸（16/20/24 设计里的 17px、23px）。
3. 重复。网格中的卡片、列表项、特性块共享 padding、gap、尺寸、结构。标记微妙不同的近似重复——要么一致要么故意不同，没有中间地带。
4. 策略性变化。长页面/deck 偶尔打破模式（背景切换、更宽区块、居中 CTA）。标记完全统一（单调）和每区块都不同（混乱）。
5. 调色板纪律。3-5 色加 tint/shade。标记 8+ 独立色，或不同地方微妙不同的蓝/灰。
6. 区块结构。区块视觉可辨（背景变化、分割线、padding 切换）但一致地如此。标记无分隔和分隔样式过多。
7. 对齐。标记偏离网格几像素的元素——不一致 margin 而非有意偏移。

### Phase 3：聚合修复

聚合两轮发现，直接修复：
- 随机间距/字号 -> 对齐到文件的阶梯（缺失则定义一个——4px 或 8px 倍数）
- 扁平层次 -> 引入对比（更大标题、更突出 primary CTA、一致中性正文）
- 反转层次 -> 交换信号（压低吵闹的不重要元素，重新定位被埋的主元素）
- 单调 -> 引入一次策略性中断；混乱 -> 收束到最强的模式

模糊情况倾向更激进的层次——太强比太弱更容易调回来。

---

## 五、交互态审查（Interaction States Pass）

> 验证每个交互元素有完整的状态集（default/hover/active/disabled/focus/loading）加过渡和反馈。无状态反馈的交互元素感觉坏了——没 hover 的按钮像标签；删了 focus ring 的锁死键盘用户。

> 注：engineering-checklist 的"组件行为标准"节已覆盖 Modal/Toast/Slider 等具体组件的交互行为。本节聚焦**状态完整性**——每个元素是否六个状态都在。两者互补：这里查"有没有"，engineering-checklist 查"对不对"。

### Phase 1：盘点交互元素

走一遍设计，列出每个交互元素：按钮（含 role="button" 和任何有 click handler 的）、链接、表单输入、toggle（checkbox/radio/switch）、可点卡片或行、导航项（tab/侧边栏链接/面包屑）、自定义控件（下拉/手风琴/弹窗/popover）。

### Phase 2：逐元素状态验证

检查六个方面：

1. **Default**。静止时明显可交互：按钮有填充或边界区别于正文；链接像链接；输入有可见边界或填充。标记只在 hover 时才暴露交互性的元素——触屏和键盘用户永远不 hover。
2. **Hover**。光标悬停时视觉变化——至少颜色切换；更好是颜色 + 阴影 + 轻微 transform（translateY(-2px)）。不要用降透明度做 hover——读起来像 disabled。
3. **Active / pressed**。更深颜色、轻微缩小（transform: scale(0.98)）、或回基线——确认点击已注册。
4. **Disabled**。降透明度（~0.6）、无 hover 效果、cursor: not-allowed、与 default 和 hover 都可辨。如果因等待条件而 disabled（"填写所有必填项"），说明**为什么**——tooltip、inline message 或 title 属性。
5. **Focus**。用 :focus-visible（非裸 :focus）的可见环：3:1 对比度、至少 2px 厚带 2px offset。outline: none **永不**无替代使用。
6. **Loading**（触发异步工作的元素）。点击时 disable 防止重复提交，标签换成 spinner 或"加载中…"，完成后恢复。渲染时获取的数据给 skeleton、spinner 或进度指示。

### Phase 3：验证过渡

每个状态变化平滑过渡，不跳（transition: background 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease）：
- 状态切换 0.15-0.3s；入场/出场 0.3-0.5s（弹窗/抽屉/Toast）
- 避免微交互超过 0.5s（滞后）和 0s / 无过渡（坏了）
- motion-heavy 过渡包在 @media (prefers-reduced-motion: reduce) 里

> 缓动曲线、时长上限、stagger 等具体动效工艺见 motion-craft.md，不在此重复。

### Phase 4：验证动作反馈

每个动作显示可见结果：提交成功（Toast、inline message 或带确认的重定向）、提交失败（清晰错误，字段特定则绑到字段）、校验错误（blur 或 submit 时出现，修复时清除）、状态变化（即时视觉更新）。标记静默成功和静默失败——都感觉坏了。

当前状态也要可见：激活的页面或 tab、选中项、激活的筛选或排序视觉可辨。

### Phase 5：修复并总结

用设计系统的 token 加每个缺失的状态或反馈元素。系统未定义时用：hover 深 10-15%（或 color-mix）；active 再深 10% 或 scale(0.98)；disabled opacity 0.6 + cursor: not-allowed；focus outline: 2px solid var(--color-primary); outline-offset: 2px；transition 0.2s ease。不确定时做判断并标记。

---

## 六、无障碍审查（Accessibility Audit）

> 全面无障碍审查：对比度、语义 HTML、键盘导航、动效、表单。**好的无障碍是好的设计**——它惠及所有人。

> 注：engineering-checklist 第一节"无障碍"已覆盖代码级要点（aria-label、语义 HTML、focus ring、skip-link）。本节是**全表面审查流程**——按 phase 走、四轮 pass、聚合修复。两者互补：engineering-checklist 是 file:line 审查，本节是设计审查。

### Phase 1：识别审查表面

审查用户刚编辑/问起的 HTML 文件；否则最近修改的设计文件；不清则问。通读，记录框架、期望级别（默认 WCAG AA）、用户声明的约束。

### Phase 2：四轮审查

顺序运行四轮（单 agent 循环），收集发现，不因第一个问题就停。

**Pass 1：对比度和颜色**
1. 文字对比度。正文（18px 以下）需 4.5:1；大字（18px+ bold 或 24px+）需 3:1；UI 组件（按钮/图标/focus ring）需 3:1。计算可解析的每对的实际比率；标记每个失败对。
2. 纯颜色信号。标记任何只靠颜色传达的状态——无图标的绿/红、无下划线的链接、无图例或标签的图表。
3. 困难组合。红+绿（最常见色盲）、相似亮度的蓝+黄、白上浅灰、相似亮度的有色底上有色字。
4. 白和黑。标记纯 #FFFFFF on #000000；微妙调色（#FAFAFA / #1A1A1A）优先。风格建议，非 WCAG。

**Pass 2：语义 HTML 和结构**
1. 标题层级。恰好一个 h1，不跳级；标题描述内容，非视觉大小。
2. 正确元素。button 非 div onclick；a href 非样式化 div；label for 关联输入；nav/main/article/section/aside 地标。
3. 每张有意义图片的 alt。装饰性用 alt=""；有意义的描述传达什么（alt="无线耳机，侧视图" 非 alt="product"）。
4. 表单 label。每个输入有关联的 label（或 aria-label）。占位符不是 label。
5. ARIA 只在语义 HTML 不够时。标记 div 上的 role="button"——应该是 button。

**Pass 3：键盘导航和焦点**
1. 键盘可达。所有可点的 Tab 可达——hover-only 菜单、鼠标-only 下拉、键盘不可达弹窗失败。
2. 合理 tab 顺序。跟随阅读顺序；标记大于 0 的 tabindex。
3. 交互模式。弹窗 Esc 关闭；下拉 Enter/Space 打开、方向键导航；表单字段 Enter 提交。
4. 可见 focus ring。标记无可见替代的 outline: none（需 3:1 对比度）。优先 :focus-visible。
5. skip link。有大量重复导航的页面推荐"跳到主内容"。

**Pass 4：动效、表单和其他**
1. prefers-reduced-motion 被尊重。超过几百毫秒的动画需要 reduce 块缩短或移除。
2. 无闪烁超过每秒 3 次（光敏性癫痫风险）；标记并要求暂停控件。
3. 表单错误具体（"邮箱地址无效"非"无效"），视觉和 aria-describedby 绑到字段。
4. 必填项用文字和/或图标加 required 属性标记，不只靠颜色。
5. 输入类型和 autocomplete。type="email"、type="tel"、autocomplete 用于自动填充和移动键盘。
6. 触控表面 hit target 至少 44x44px。

### Phase 3：聚合修复

四轮发现聚合去重，逐条直接修复。边界情况（如对比度 4.4:1）也修——无障碍是地板不是天花板。明确假阳性或范围外（如无法修改的第三方嵌入）标记并跳过。

---

## 七、交付前总审查（Polish Pass）

> 交付前全面质量门禁。**打磨和未打磨的设计是同一个想法在不同关怀层级上的执行——差距是人们实际看到的。** 这是四个窄审查 skill 的 umbrella；交付前作为最终门禁使用。

> 与 preflight 的关系：preflight 是**勾选式门禁清单**（适用项不过不交），polish-pass 是**按 phase 走的审查流程**（四轮 pass -> 聚合 -> 去重 -> 优先级 -> 修复 -> 再验证）。两者可叠加：preflight 管底线，polish-pass 管设计质量深度。

### Phase 1：确认范围

打磨用户刚完成/问起的 HTML 文件；否则项目主交付物；不清则问。读文件，记录媒介（slide/page/mobile/dashboard）、部署上下文（内部/客户面/营销）、声明的约束。

设计明显在进行中（布局碎、缺区块、占位内容还在迭代）时，说明并问是现在打磨还是结构稳定后再来。

### Phase 2：四轮审查

顺序运行（单 agent 循环），收集发现，不因第一个问题就停：

1. **无障碍审查**（本文件第六节）：对比度/颜色、语义 HTML/结构、键盘/焦点、动效/表单/hit-target。
2. **AI 味检查**（references/ai-anti-patterns.md）：渐变、emoji 装饰、左边界卡片、手绘 SVG、用滥默认字体、纯白/黑、发明颜色、离阶梯间距。
3. **层次与节奏审查**（本文件第四节）：主/次/三区分、间距/字号阶梯纪律、重复/策略性变化、调色板纪律、区块结构、对齐。
4. **交互态审查**（本文件第五节）：逐元素 default/hover/active/disabled/focus/loading、过渡时长、prefers-reduced-motion、动作反馈、状态可见性。

### Phase 3：聚合、去重、优先级

四轮发现聚合成一个列表。合并重复（如"focus ring 删除"同时来自无障碍和交互态）。分组：

1. **Blocker**——无障碍失败（对比度低于 WCAG、缺键盘支持、删了 focus ring、缺 label）。破坏真实用户的设计；全修。
2. **质量问题**——AI 味套路、层次破了、缺交互态。降低设计品质；全修。
3. **打磨建议**——更微妙的改善（色调偏移、间距阶梯收紧）。范围内时应用；范围外时标记。

### Phase 4：修复并再验证

直接修每个 blocker 和质量问题。模糊修复（如设计用 Inter 但无品牌字体声明）选可辩护的默认并标记让用户覆盖。明确假阳性标记并跳过。

然后复查高风险区：对比度修复是否冲淡了品牌色？新 focus ring 是否重叠相邻内容？primary CTA 现在实际感觉 primary 吗？修不对的地方；标记不确定的。

### Phase 5：最终总结

简洁报告——用户可以要细节：
- **结论**——"可交付" / "用户审查标记决策后可交付" / "polish 之前还需迭代"
- **修复的 blocker 和应用的打磨**——按类别计数
- **待定决策**——需签字的判断（字体选择、色调偏移、强调级别）
- **范围外**——注意到但未碰的（文案编辑、内容增加、新功能）

---

## 与已有 references 的关系

| Trystan skill | 我们的对应 | 差异 |
|---------------|-----------|------|
| ai-slop-check | references/ai-anti-patterns.md | 我们更细：中文伪斜体、眉批配额、Bento 空洞、文案陈词滥调；无需吸收 |
| accessibility-audit | 本文件第六节 + engineering-checklist 第一节 | engineering-checklist 是代码级 file:line；本节是全表面设计审查流程 |
| interaction-states-pass | 本文件第五节 + engineering-checklist 第三节 | engineering-checklist 管 Modal/Toast 等具体组件行为；本节管每个元素的状态完整性 |
| hierarchy-rhythm-review | 本文件第四节 | 全新——我们之前没有层次/节奏的系统化审查流程 |
| polish-pass | 本文件第七节 + preflight.md | preflight 是勾选门禁；polish-pass 是按 phase 走的深度审查 |
| discovery-questions | 本文件第一节 | 全新——我们之前没有结构化 kickoff 提问协议 |
| frontend-aesthetic-direction | 本文件第二节 | 全新——我们之前没有 greenfield 美学方向承诺的逐轴协议 |
| content principles (ch.5) | 本文件第三节 | 全新——我们之前没有"无填充"内容原则的显式参考 |
| color (ch.9) | references/color-palette-roles.md | 我们更细：五角色结构 + 6 套色板 + 极简精确折叠模式；无需吸收 |
| typography (ch.8) | references/chinese-typography.md | 我们更细：中文行高/字重/中西文间距/全角标点；无需吸收 |
| motion (ch.11) | references/motion-craft.md | 我们更细：频率决策框架/不对称时序/拖拽手势/WAAPI；无需吸收 |
| make-a-deck / make-a-prototype / make-tweakable / generate-variations / wireframe / design-system-extract / component-extract | 未吸收 | 生产类 skill——我们的 skill 聚焦审查和方向选择，不覆盖这些构建流程；按需在具体项目中用即可 |
---

## 八、只读审计（Audit）

> 吸收自 Nutlope/hallmark `audit` 动词（MIT）。**只评分、不改代码。**
> 与 polish-pass 区别：audit 输出 punch list；polish-pass 是审查后修复流程。用户说「audit / 打分 / 只审不改 / 列问题」时用本节。

### 协议

1. 读取用户指定目标（文件、目录、URL 渲染页、截图）。
2. 对照 `ai-anti-patterns.md` + `slop-gates.md`（及目标 mode 的正向语法）。
3. 每条发现必须包含：
   - **Tell** — 反模式/门禁名
   - **Where** — 路径 + 行号或截图区域
   - **Severity** — `critical`（已是 slop）/ `major`（明显 AI 生成感）/ `minor`（品味）
   - **Fix** — 一行可执行修正（仍不直接改）
4. 按 severity 分组。结尾一行：`N critical · M major · K minor`。
5. **禁止** edit / redesign / 顺手修。

### 额外结构检查

- 若页面对上 AI 模板（居中 hero + 三等分 feature + CTA + footer，无非对称或意外），即使配色还行，也记 **critical structural**。
- 若存在 `/* surface · macrostructure: ... */`（或历史 Hallmark stamp）：检查戳记与真实结构是否一致；不一致记 `critical: stamp lies`。
- 若项目根有 `design.md` / `DESIGN.md`：先读系统，再查 token/字体/宏结构族漂移；漂移记 critical/major。
- 无 `design.md` 时：同项目多页结构指纹撞车记 `minor: variety drift`。

### Mode 意识

`shell`/`workbench`/`paper` 审计时应用对应放宽/收紧（见 `slop-gates.md` Mode 例外），不要用营销页标准误杀精密壳。

---

## 九、设计 DNA 提取（Study）

> 吸收自 Nutlope/hallmark `study`（MIT）。从**截图或 URL**提取可迁移 DNA，**禁止像素级抄袭与付费模板整页搬迁**。
> 触发：用户说 `study` / 抽 DNA / 提取设计系统 / 锁定 design.md，或贴了参考图/URL 并确认是 study 而非直接当素材糊脸。

### 模式

| 源 | 能力 | 盲区 |
|----|------|------|
| **image** | 宏结构、层级、气质、大致配对 | 字体/色值只能估角色与候选，不可假装精确识别 |
| **URL** | 可读 HTML/CSS 时给精确字体与色值 | **节奏/呼吸感不可靠**；需在报告里写明；鉴权墙/纯 SPA 壳则改要截图 |

### 五步协议

1. **Surface** — 纸面/画布气质、明暗、材质感（纸、玻璃、终端、海报…）
2. **Type** — 展示/正文角色；URL 模式写确切族名；image 模式给 1–2 个真实候选
3. **Structure** — 宏结构名 + 六轴指纹（见 `divergence-playbook.md` §六）
4. **Motion** — 动或静、入场语法、是否物理
5. **Rhythm** — 疏密、分隔语言、重复节拍（URL 模式标 `rhythm: unknown` 若无截图）

### 输出

1. **诊断报告（一页）**：宏结构、原型件、字体策略、色锚、**不要带走**的反模式、mode 建议（shell/paper/brand…）。
2. **确认问句**（等用户）：
   - 原样采用 DNA 重建内容？
   - 改某一轴（例如保结构换色锚）？
   - `lock the DNA` / 给我 `design.md`？
   - 只要诊断？
3. **禁止**在未确认时直接开改生产代码。

### `design.md` 锁定（opt-in）

仅当用户明确要求锁定时写入项目 `design.md`（或用户指定路径）。建议最小字段：

- paper / ink / accent（值或 OKLCH）
- display / body 字体角色与候选
- macrostructure 家族与禁用结构
- motion 强度上限
- Surface Mode 默认
- Provenance：来源类型（own / public-reference / image）与日期

URL 模式写入前需用户确认来源是 **自有** 或 **为自有品牌作公开参考**；其它来源只给诊断，不写可搬运 design.md。Image 模式用户自带截图可直接锁。

### 重建规则

- 用用户自己的文案与 IA，不搬运源站文案/摄影。
- stamp 建议：`studied: yes · DNA-source: image|url`。
- 若对话里刚 study 过，重建却无故退回通用 catalog 气质且用户未要求改道 → 未过 `slop-gates`「DNA 被丢弃」类问题（按 major/critical 处理）。

### 拒绝边界

- 付费模板市场整页复制、明显侵权素材库、要求 1:1 像素克隆 → 拒绝克隆，可改为「结构级 DNA + 自有内容」。
- 鉴权墙/空白 SPA：说明限制并要截图，不假装读到了设计。

---

## 与已有 references 的关系（续）

| 外部源 | 我们的对应 | 差异 |
|--------|-----------|------|
| Nutlope/hallmark slop-test | `references/slop-gates.md` | 重写成 surface mode 方言；去掉 Hallmark 主题目录绑定 |
| Nutlope/hallmark structure/macrostructures | `divergence-playbook.md` §六 | 只吸收六轴 + 同质反模式 + 域三选；不整库 20 主题 |
| Nutlope/hallmark audit/study | 本文件 §八 / §九 | 动词挂在 surface 下；与 polish-pass / 中文 / audience gate 对齐 |
| Nutlope/hallmark 独立 skill | **不立 skill** | 展示层 owner 仍是 `kongyu-surface` |

## 十、渲染后复审（Rendered Re-review）

> 吸收 Hallmark 的渲染后复审原则（MIT）：先看渲染结果，再决定改什么；改完对照内容是否保持。不引入 Hallmark 的主题库、固定版式配额或 `sloplint`。

### 何时使用

新页面、实质改版、视觉质量交付，以及用户要求“看看实际效果”时使用。单行样式、纯文案或无法渲染的文本稿不跑完整流程。

### 流程

1. **改前记录。** 能打开页面时，在声明的目标尺寸截图，并列出必须保留的标题、正文事实、链接、表单字段、按钮和脚本钩子。不能打开时说明限制，不把源码阅读称为已看过页面。
2. **先看图。** 先看截图里的读者路径、主次、溢出、对比和真实破损，再看源码检查结果。源码告警不能单独决定视觉结论。
3. **改后对照。** 用同一尺寸重新截图。核对保留项是否还在，记录删改的内容和原因。视觉修复不得偷偷删除事实、链接、字段或交互。
4. **预算。** 一次集中检查、一批修复、一次确认。确认又引入新的可见问题时，只再修这一处并复看受影响区域。
5. **结论。** 报告目标尺寸、看过的图、保留项、丢弃项和未验证项。没有截图或实机渲染时，结论只能是“源码已查，渲染未验证”。

PPT、报告页和产品 UI 都走这四步。页面语义仍归各自的内容 skill，本节只判断渲染后的展示质量与内容保持。
