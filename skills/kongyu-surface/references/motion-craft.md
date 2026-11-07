# 动效工艺规范（Motion Craft）

> 蒸馏自 Emil Kowalski 的设计工程哲学（Sonner / Vaul 作者，13M+ 周下载）。
> 核心信念：用户注意不到的细节会复利叠加成"说不出为什么但就是好用"的体验。
> 第六节为手势物理切片：只服务 sheet/drawer/drag/swipe，不把 Apple 营销视觉并入本 skill。

## 一、动画决策框架（写任何动画代码前按序回答）

### 1. 该不该动？——看使用频率

| 频率 | 决定 |
|------|------|
| 每天 100+ 次（键盘快捷键、命令面板开关） | **永不动画** |
| 每天几十次（hover、列表导航） | 移除或大幅缩短 |
| 偶尔（弹窗、抽屉、Toast） | 标准动画 |
| 稀有/首次（onboarding、成功庆祝） | 可以给惊喜 |

**键盘触发的操作永不动画。** Raycast 的开关没有动画，那就是每天用几百次的东西的最优体验。

### 2. 为什么动？——必须有明确目的

合法目的：空间一致性（Toast 从哪进就从哪出）、状态指示、反馈（按压缩放确认"我听到了"）、
防突变（元素凭空出现/消失感觉像坏了）。
如果答案只是"看起来酷"而且用户会经常看到——不要动。

### 3. 用什么缓动？

```
入场/出场？        → ease-out（起步快，感觉响应及时）
屏幕上移动/变形？  → ease-in-out
hover/颜色变化？   → ease
匀速运动（跑马灯）？→ linear
默认               → ease-out
```

**内置 CSS 缓动太弱，必须用自定义曲线：**

```css
--ease-out:    cubic-bezier(0.23, 1, 0.32, 1);   /* UI 交互强化 ease-out */
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);  /* 屏上移动 */
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);   /* iOS 式抽屉 */
/* Geist 开发者壳可选：cubic-bezier(0.175, 0.885, 0.32, 1.1)；0ms 优先，150/200/300ms — 见 vercel-precision-system.md */
```

开发者壳 / 设置 / 工作台的短交互可选用官方 Geist motion（`vercel-precision-system.md`）；sheet/drawer/drag/swipe 仍用本节手势物理。同一视图不要混两条招牌 ease。

**永不用 ease-in**：起步慢会让界面在用户盯得最紧的瞬间显得迟钝。

### 4. 多快？

| 元素 | 时长 |
|------|------|
| 按钮按压反馈 | 100-160ms |
| Tooltip、小型 popover | 125-200ms |
| 下拉、select | 150-250ms |
| 弹窗、抽屉 | 200-500ms |
| 营销/叙事动画 | 可以更长 |

**UI 动效上限 300ms。** 180ms 的下拉比 400ms 的感觉响应更快；转得快的 spinner
让加载显得更短（感知性能与真实性能同等重要）。

## 二、组件动效原则

### 按钮必须有按压感
```css
.button { transition: transform 160ms var(--ease-out); }
.button:active { transform: scale(0.97); }
```
适用于 `brand` 与需要触感确认的表达型控件，缩放幅度 0.95-0.98。

**Surface Mode 绑定：** `shell` / `workbench` 不用按压缩放炫技；优先改 `background-color` / `color` / `box-shadow`，动效跟 Geist（0ms 优先，见 `vercel-precision-system.md`）。`paper` 默认少动或不动。手势/抽屉仍用本节后文。

### 永不从 scale(0) 入场
现实世界没有东西凭空出现。从 `scale(0.95) + opacity: 0` 起步。

### Popover 要感知触发源
`transform-origin` 设为触发器位置（Radix: `var(--radix-popover-content-transform-origin)`）。
**例外：Modal 保持居中 origin**——它不锚定任何触发器。

### Tooltip 二次悬停跳过延迟
第一个 tooltip 有延迟防误触；打开后相邻 tooltip 即时出现、无动画。

### 快速触发的 UI 用 transition 不用 keyframes
transition 可中断可重定向；keyframes 每次从零重播。Toast、开关这类会被连点的
组件必须用 transition。

### 入场用 @starting-style（现代 CSS）
```css
.toast {
  opacity: 1; transform: translateY(0);
  transition: opacity 400ms ease, transform 400ms ease;
  @starting-style { opacity: 0; transform: translateY(100%); }
}
```

### 不对称进出时序
系统响应要快：退出比进入快（enter 400ms / exit 250ms）。
用户决策要慢：hold-to-delete 按住 2s linear，松手 200ms ease-out 弹回。

### crossfade 不顺就加微模糊
两状态交叉时叠影不自然，过渡期加 `filter: blur(2px)` 骗过眼睛。模糊 < 20px（Safari 开销大）。

## 三、Stagger（交错入场）

多元素同时入场时，每项延迟 30-80ms 依次出现：

```css
.item { opacity: 0; transform: translateY(8px); animation: fadeIn 300ms var(--ease-out) forwards; }
.item:nth-child(2) { animation-delay: 50ms; }
.item:nth-child(3) { animation-delay: 100ms; }
```

延迟过长会显得慢。stagger 是装饰——播放期间绝不阻塞交互。

## 四、性能铁律

- **只动 `transform` 和 `opacity`**（跳过 layout/paint，跑 GPU）
- 拖拽时直接改元素 `style.transform`，不要改父级 CSS 变量（会触发全子树重算）
- CSS 动画跑合成线程，主线程繁忙时也不掉帧；JS 动画（rAF）会掉。
  预定动画用 CSS，动态可中断的用 JS
- 需要 JS 控制又要 CSS 性能时用 WAAPI：`element.animate([...], { easing: 'cubic-bezier(...)' })`

## 五、无障碍

```css
@media (prefers-reduced-motion: reduce) {
  /* 保留有助理解的 opacity/color 过渡，移除位移类动画 */
}
@media (hover: hover) and (pointer: fine) {
  /* hover 动效只在真指针设备生效，防触屏误触发 */
}
```

reduced-motion 是"更少更温和"，不是"全部归零"。

## 六、手势物理（仅 sheet / drawer / drag / swipe 时读）

> 切片自流体接口原则（WWDC Designing Fluid Interfaces 脉络；与本节作者同源）。
> **门闩：** 仅当任务含 bottom sheet、drawer、可拖面板、swipe-to-dismiss、carousel 甩动、可打断手势过渡时完整执行本节。
> 普通按钮/hover/Toast/列表入场只看前面章节，不要把 spring 物理默认套到工作台。
> **不是视觉风格包：** 不引入毛玻璃、SF Pro、Apple 营销白空间；`backdrop-filter` 仍服从 `ai-anti-patterns.md`（只用于真有浮层语义的 chrome）。

### 1. 可打断（Interruptibility）— 手势路径第一原则

思想与手势并行发生。任何手势驱动动画必须随时可抓回、可反向，且不锁输入。

- 过渡进行中**永不锁输入**。
- **永远从 presentation（当前屏幕）值开新动画**，不要从逻辑 target 重播；中断时读 live transform，避免跳变。
- 手势主路径优先 spring / 可重定向的 JS 动画；纯 CSS transition / `@keyframes` 难在中途被平滑抓回。
- 反向时**携带速度**，禁止 hard-cut 速度（“砖墙感”）。
- 2D 运动拆成独立 X / Y spring，避免单距离 spring 在轴向速度不同时失步。

### 2. 直操与响应

- **pointer-down 即时反馈**，不要等到 click / touch-up 才高亮。
- 拖动 **1:1 跟踪**，并尊重 grab offset（从哪里抓住就从哪里跟，禁止一抓就跳到元素中心）。
- 用 Pointer Events + `setPointerCapture`；拖动中忽略新增触点，防多指跳位。
- 方向提交前加 ~10px hysteresis；允许拖离再拖回取消。

### 3. 速度交接与动量投影

释放瞬间动画必须接住手指速度，拖动与动画之间无可见接缝。

```text
relativeVelocity = gestureVelocity / (targetValue − currentValue)   # 需要相对初速的 API
# Framer Motion / Motion 通常直接吃绝对 px/s：velocity = releaseVelocity
```

不要只按释放点 snap。用速度**投影落点**，再选最近 snap：

```js
// Apple 流体接口样本的指数衰减投影；不是教科书 v^2/(2a)
function project(initialVelocity /* px/s */, decelerationRate = 0.998) {
  return (initialVelocity / 1000) * decelerationRate / (1 - decelerationRate);
}
const projected = current + project(releaseVelocity);
const target = nearestSnapPoint(projected);
animateSpringTo(target, { velocity: releaseVelocity });
```

快速一甩即可 dismiss：可与简单阈值并用。粗判可用 `velocity = |dragDistance| / elapsedTime`，> 0.11 常足够；精细场景以投影 + 速度符号为准（commit / reverse 看速度方向，不只看位置过半）。

### 4. 空间一致性

- **进出同路径**：从右侧滑入的面板必须退回右侧；禁止 in-right / out-bottom。
- **锚定触发源**：menu / popover / sheet 的 `transform-origin` 对准触发器（Modal 仍可居中）。
- **可逆曲线镜像**：往返用互为逆的 cubic-bézier，空间轨迹可预期。
- 中间帧应**朝结果方向提示**，不要无意义插值。

### 5. Rubber-band（软边界）

越过边界时递进阻尼，硬停像死机：

```js
function rubberband(overshoot, dimension, constant = 0.55) {
  return (overshoot * dimension * constant) / (dimension + constant * Math.abs(overshoot));
}
```

### 6. Spring 快速参数（仅手势 settle）

**作用域：** 下表只用于用户直接操控且可中断的 sheet/drawer/drag/swipe settle；不得当作页面、列表、Toast、工作台常规过渡的默认配方。常规 UI 仍用第一节 ease 曲线与时长表。

| 需要 | 形态 | 参考 |
|------|------|------|
| 手势释放后 settle | critically damped，几乎无 overshoot | damping ~1.0，response 0.3–0.4 |
| 轻甩 / 动量 | 轻微 under-damped | damping ~0.8，response 0.3–0.4 |
| reduced-motion | 交叉淡入淡出，不用大位移 spring | `@media (prefers-reduced-motion)` |

工作台/高频壳层仍服从第一节频率表：可动不等于该动。

### 7. 手势验收清单

- [ ] 中途可抓回并反向，无跳变、无锁输入
- [ ] 释放速度接到 spring / settle，无接缝
- [ ] dismiss / snap 用投影或速度符号，不只位置过半
- [ ] 边界 rubber-band，非硬撞
- [ ] 进出路径对称；origin 锚定触发源（Modal 例外）
- [ ] reduced-motion 有位移降级
- [ ] 未借机加全页玻璃拟态或营销级 spring 轰炸

## 七、动效一致性（Cohesion）

动效风格必须匹配组件人格：玩具感的产品可以弹一点，专业仪表盘必须干脆利落。
缓动、时长、视觉设计、命名要在同一个气质里。隔天用新鲜眼睛慢放复查动画——
全速下看不见的时序问题在慢放里无所遁形。

## 审查对照表

| 问题 | 修复 |
|------|------|
| `transition: all` | 逐属性声明 |
| `scale(0)` 入场 | `scale(0.95) + opacity: 0` |
| `ease-in` | `ease-out` 或自定义曲线 |
| popover 居中 origin | origin 对准触发器（modal 除外） |
| 键盘操作有动画 | 删除动画 |
| UI 时长 > 300ms | 降到 150-250ms |
| hover 无媒体查询 | 包 `@media (hover: hover)` |
| 连点组件用 keyframes | 换 transition |
| 进出同速 | 出场更快 |
| 全员同时出现 | 加 30-80ms stagger |
| 手势动画中途锁输入 / 从 target 重播 | 从 live 值重定向，允许抓回 |
| 拖放释放后速度接不上 | 交接 release velocity；必要时动量投影 |
| 进出路径不对称 | 同路径进出；origin 锚定触发源 |
