# docu.md Diagram Reference

Source: [docu.md](https://docu.md) / [markdown-viewer-extension](https://github.com/markdown-viewer/markdown-viewer-extension) (GPL-3.0, v5.1.0)

docu.md bridges the gap between AI-generated Markdown and finished deliverables. Its core thesis aligns with this skill's Dual Reader architecture: the agent produces `.md` (source layer), docu.md renders it into DOCX/PDF/HTML (human reader layer).

## Supported Diagram Engines

docu.md renders 7 diagram engines from fenced code blocks. No configuration needed — write the diagram code in Markdown, docu.md renders it live.

| Engine | Code block language | File extensions | Best for |
|---|---|---|---|
| Mermaid | `mermaid` | `.mermaid`, `.mmd` | Flowcharts, sequence, gantt, class, state, pie, ER, git graph, mindmap, timeline, quadrant, sankey, xychart, kanban, architecture, radar, treemap, packet |
| PlantUML | `plantuml`, `puml`, `wsd` | `.plantuml`, `.puml` | UML class, sequence, activity, state, use case, deployment, object diagrams |
| Vega-Lite | `vega-lite`, `vegalite` | `.vl`, `.vega-lite` | Declarative statistical charts (bar, scatter, line, area, stacked, grouped) |
| Vega | `vega` | `.vega` | Low-level visualization grammar, complex interactive charts |
| Graphviz DOT | `dot`, `graphviz` | `.gv`, `.dot` | Directed/undirected graphs, network topology, architecture diagrams |
| drawio | `drawio` | `.drawio` | Diagram.net style diagrams |
| Infographic | `infographic` | `.infographic` | @antv/infographic charts |
| Canvas | `canvas` | `.canvas` | JSON Canvas format (Obsidian compatible) |

Plus: LaTeX math formulas (via KaTeX/MathJax), 100+ language syntax highlighting.

## Work-flow Alignment with Dual Reader Architecture

```text
agent produces .md (source layer, source of truth)
  → docu.md renders to .docx / .pdf / .html (human reader layer)
  → diagrams rendered as high-resolution images
  → LaTeX rendered as editable Word equations (DOCX) or KaTeX (HTML)
```

Rules:
- The `.md` file is the agent source layer. Fix claims there first.
- docu.md output is the human reader layer, regenerated from source.
- Never hand-edit docu.md output to override source truth.
- Keep `.md` and exported `.docx`/`.pdf`/`.html` as sibling files.

## Mermaid Quick Templates

### Flowchart

```mermaid
flowchart TD
    A[开始] --> B{检查条件}
    B -->|条件满足| C[执行操作 A]
    B -->|条件不满足| D[执行操作 B]
    C --> E[记录日志]
    D --> E
    E --> F{是否继续}
    F -->|是| A
    F -->|否| G[结束]
```

### Sequence Diagram

```mermaid
sequenceDiagram
    participant U as 用户
    participant B as 浏览器
    participant S as 服务器
    U->>B: 打开 .md 文件
    B->>S: 请求数据
    S-->>B: 返回数据
    B-->>U: 显示内容
```

### Gantt Chart

```mermaid
gantt
    title 项目开发时间线
    dateFormat YYYY-MM-DD
    section 需求阶段
    需求分析           :done,    des1, 2024-01-01, 7d
    原型设计           :done,    des2, 2024-01-08, 5d
    section 开发阶段
    前端开发           :active,  dev1, 2024-01-15, 20d
    后端开发           :active,  dev2, 2024-01-20, 25d
    section 发布阶段
    部署上线           :         deploy, after dev2, 2d
```

### State Diagram

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Loading : 打开文件
    Loading --> Ready : 渲染完成
    Ready --> [*]
    Loading --> Error : 渲染失败
    Error --> Idle : 重试
```

### ER Diagram

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    CUSTOMER {
        string name
        string email
    }
    ORDER {
        int orderNumber
        date orderDate
    }
```

### Architecture Diagram

```mermaid
architecture-beta
    group api(cloud)[API]
    service db(database)[Database] in api
    service server(server)[Server] in api
    db:L -- R:server
```

### Data Flow (custom graph)

```mermaid
graph LR
    A[用户下单] --> B[支付系统]
    B --> C[订单确认]
    C --> D[库存扣减]
    D --> E[仓库发货]
    E --> F[用户签收]
    F --> G[交易完成]
```

### Comparison (subgraph)

```mermaid
flowchart LR
    subgraph 传统方案["传统方案"]
        direction TB
        A1["人工处理"] --> A2["线下审批"] --> A3["纸质存档"]
    end
    subgraph 数字化方案["数字化方案"]
        direction TB
        B1["自动化处理"] --> B2["在线审批"] --> B3["电子存档"]
    end
    传统方案 -.升级.-> 数字化方案
```

## PlantUML Quick Templates

### Class Diagram

```plantuml
@startuml
class Animal {
  +String name
  +int age
  +makeSound()
}
class Dog {
  +String breed
  +fetch()
}
Animal <|-- Dog
@enduml
```

### Sequence Diagram

```plantuml
@startuml
actor 用户
participant "前端" as Frontend
participant "API 网关" as Gateway
database "数据库" as DB
用户 -> Frontend : 登录请求
Frontend -> Gateway : POST /api/login
Gateway -> DB : 查询用户
DB --> Gateway : 用户数据
Gateway --> Frontend : JWT Token
Frontend --> 用户 : 登录成功
@enduml
```

### Activity Diagram (with swimlanes)

```plantuml
@startuml
|客户|
start
:提交需求;
|产品经理|
:分析需求;
:编写 PRD;
|开发团队|
:技术评审;
if (可行?) then (是)
  :编码实现;
  :单元测试;
else (否)
  |产品经理|
  :调整需求;
endif
|客户|
:验收确认;
stop
@enduml
```

### Deployment Diagram

```plantuml
@startuml
node "负载均衡器" as LB
node "Web 服务器" as Web {
  component [Nginx]
  component [Node.js App]
}
node "数据层" as Data {
  database "PostgreSQL" as DB
  database "Redis" as Redis
}
LB --> Web
Web --> DB
Web --> Redis
@enduml
```

## Vega-Lite Quick Template

### Bar Chart

```vega-lite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "description": "A simple bar chart with embedded data.",
  "data": {
    "values": [
      {"category": "A", "value": 28},
      {"category": "B", "value": 55},
      {"category": "C", "value": 43}
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "category", "type": "nominal"},
    "y": {"field": "value", "type": "quantitative"}
  }
}
```

### Stacked Bar Chart

```vega-lite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {
    "values": [
      {"category": "A", "group": "x", "value": 10},
      {"category": "A", "group": "y", "value": 20},
      {"category": "B", "group": "x", "value": 15},
      {"category": "B", "group": "y", "value": 25}
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "category", "type": "nominal"},
    "y": {"field": "value", "type": "quantitative"},
    "color": {"field": "group", "type": "nominal"}
  }
}
```

## Graphviz DOT Quick Templates

### Directed Graph

```dot
digraph G {
    rankdir=LR;
    node [shape=box, style=filled, fillcolor=lightblue];
    Start [shape=ellipse, fillcolor=lightgreen];
    End [shape=ellipse, fillcolor=lightcoral];
    Start -> "Step 1" -> "Step 2" -> End;
    "Step 1" -> End [style=dashed, label="skip"];
}
```

### Architecture with Subgraphs

```dot
digraph G {
    compound=true;
    subgraph cluster_frontend {
        label="Frontend";
        style=filled; color=lightgrey;
        React -> Redux -> Router;
    }
    subgraph cluster_backend {
        label="Backend";
        style=filled; color=lightblue;
        NodeJS -> Express -> MongoDB;
    }
    Redux -> NodeJS;
}
```

## LaTeX Math (KaTeX)

Inline: `$E = mc^2$`

Block:

```markdown
$$
E = mc^2
$$
```

Matrix:

```markdown
$$
\begin{pmatrix} a & b \\ c & d \end{pmatrix}
$$
```

## Choosing an Engine

| Need | Recommended engine |
|---|---|
| Flowchart / process diagram | Mermaid `flowchart` or PlantUML activity |
| Sequence / interaction diagram | Mermaid `sequenceDiagram` or PlantUML sequence |
| Data charts (bar, line, scatter) | Vega-Lite |
| Complex UML (class, deployment, use case) | PlantUML |
| Network topology / graph theory | Graphviz DOT |
| Gantt / project timeline | Mermaid `gantt` |
| State machine | Mermaid `stateDiagram-v2` or PlantUML state |
| Architecture / cloud topology | Mermaid `architecture-beta` |
| Priority matrix / quadrant | Mermaid `quadrantChart` |
| User journey | Mermaid `journey` |
| Mindmap | Mermaid `mindmap` |

## Local Assets for Offline HTML Reports

This skill does not bundle Mermaid or KaTeX runtimes. Do not generate links to imaginary `assets/scripts/` files or use a CDN as a hidden runtime dependency.

- For a self-contained report, render a diagram to inline SVG or build the diagram directly as SVG after the content and relations are settled. For equations, use readable text or an inline SVG produced by an available local renderer.
- If the owning project supplies an actual local Mermaid/KaTeX runtime, copy only the required files (including KaTeX fonts and auto-render support when used) into the dedicated preview bundle. Reference those verified files from the HTML; do not assume a skill-relative path is served.
- Open the final offline HTML in the declared target environment. Confirm that each diagram/equation is visible and that no local asset request fails. A source code block or a successful file export is not a rendered diagram.
- If neither static rendering nor a local runtime is available, keep the source notation and explain the rendering limitation instead of delivering a broken diagram.

## Export via docu.md

When the reader needs DOCX/PDF (not just HTML):

1. Agent produces `.md` source layer with diagram code blocks.
2. User opens `.md` in docu.md (browser extension / Obsidian / VS Code).
3. One-click export to DOCX (editable equations), PDF (print-ready), or HTML (self-contained).
4. Diagrams exported as high-resolution images.
5. LaTeX exported as editable Word equations in DOCX.

Platforms: Chrome, Edge, Firefox, Obsidian, VS Code, Mobile (iOS/Android). All processing is local; documents never leave the device.

## Boundaries

- docu.md is a rendering/export tool, not a methodology. It does not replace Cold-Start Gate, judgment-first ordering, or cognitive-entropy rules.
- A beautifully rendered report that fails the first-screen check is still a failure.
- XiaoLab-facing output must follow the current project visual contract owned by `kongyu-surface`; do not let docu.md's default theme silently replace it.
- The `.md` source layer is authoritative. docu.md output is derived.

## Functional Diagram Prompting

When generating images for reports, the prompt must specify concrete diagram elements, not abstract concepts. Name the components, connections, data flow direction, boundary labels, steps, decision branches, and terminal states. Do NOT generate abstract unlabeled or decorative images (rings, orbs, gradients) and present them as functional diagrams. If the image model cannot produce a labeled diagram, use Mermaid or SVG instead. karma #184.
