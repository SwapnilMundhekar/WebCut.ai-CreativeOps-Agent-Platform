from pathlib import Path
import subprocess
import sys

repo = Path(r"D:\AI\WebCut.ai-CreativeOps-Agent-Platform")
readme_path = repo / "README.md"

if not repo.exists():
    print(f"Repo path does not exist: {repo}")
    sys.exit(1)

if not (repo / ".git").exists():
    print(f"This folder is not a Git repository: {repo}")
    print("Clone the GitHub repo first, then run this script again.")
    sys.exit(1)

readme = r"""<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=245&color=0:060716,28:15102E,55:6D28D9,78:00E5FF,100:00F5A0&text=WebCut.ai&fontColor=FFFFFF&fontSize=74&fontAlignY=38&desc=AI%20CreativeOps%20%7C%20Media%20Intelligence%20%7C%20Agentic%20Automation%20on%20AWS&descSize=20&descAlignY=58&animation=fadeIn" alt="WebCut.ai banner" />

<br />

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=700&size=24&duration=2600&pause=700&color=00E5FF&center=true&vCenter=true&width=980&lines=One+Stop+Online+Content+Creation+Platform;AWS+Native+Generative+AI+Engineering;Bedrock+Agents+%7C+RAG+%7C+Guardrails+%7C+Step+Functions;Text+to+Speech+%7C+Speech+to+Text+%7C+Video+Enhancement;Built+as+a+Job+Ready+Full+Stack+AI+Portfolio+Project" alt="Animated project subtitle" />

<br />
<br />

<img src="https://img.shields.io/badge/AWS-Bedrock-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white" alt="AWS Bedrock" />
<img src="https://img.shields.io/badge/AI-Bedrock_Agents-6D28D9?style=for-the-badge" alt="Bedrock Agents" />
<img src="https://img.shields.io/badge/RAG-Knowledge_Bases-00E5FF?style=for-the-badge" alt="Knowledge Bases" />
<img src="https://img.shields.io/badge/API-FastAPI-00C7A7?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
<img src="https://img.shields.io/badge/Web-Next.js-111827?style=for-the-badge&logo=nextdotjs&logoColor=white" alt="Next.js" />
<img src="https://img.shields.io/badge/Agents-LangGraph-FF2D95?style=for-the-badge" alt="LangGraph" />
<img src="https://img.shields.io/badge/Automation-n8n-EA4B71?style=for-the-badge&logo=n8n&logoColor=white" alt="n8n" />
<img src="https://img.shields.io/badge/Tools-MCP-00F5A0?style=for-the-badge" alt="MCP" />

<br />
<br />

<h3>One platform to create, enhance, automate, govern, and export AI powered content.</h3>

</div>

---

# WebCut.ai CreativeOps Agent Platform

**WebCut.ai CreativeOps Agent Platform** is an AWS native full stack AI system for **one stop online content creation**, **AI media intelligence**, and **agentic creative automation**.

It is designed as a serious portfolio grade engineering project that demonstrates how a modern AI product can combine full stack development, Python backend engineering, Retrieval Augmented Generation, agent orchestration, cloud native workflows, security, observability, media processing, and production deployment.

WebCut.ai helps users turn brand context, product data, campaign briefs, images, audio, and video into polished creative assets and automated content workflows.

---

## What WebCut.ai Does

WebCut.ai is being built as a creative operating system for modern content teams.

| Capability | What the platform provides |
|---|---|
| Online content creation | Create social posts, banners, thumbnails, ecommerce assets, ads, and campaign packs |
| AI media intelligence | Analyse, enhance, transform, and prepare image, audio, and video assets |
| Brand grounded generation | Use brand guides, product data, campaign history, and policies through RAG |
| Agentic automation | Use agents to plan, retrieve, generate, validate, revise, and export content |
| Speech AI | Text to Speech, Speech to Text, transcripts, captions, and voiceover scripts |
| Video enhancement | Denoising, sharpening, 4K enhancement, captions, short form exports |
| Image enhancement | Background removal, smart crop, object cleanup, product cutouts, upscaling |
| Workflow automation | Approval flows, scheduled jobs, notifications, publishing drafts |
| Governance | Guardrails, human approval, audit logs, cost tracking, and compliance checks |

---

## Why This Project Exists

This project has two clear goals.

### 1. Job readiness

WebCut.ai is designed to prove practical capability for roles such as:

- AI Engineer
- Generative AI Developer
- Agentic AI Engineer
- Full Stack AI Engineer
- Python Backend Engineer
- AWS AI Engineer
- Automation Engineer
- Applied Machine Learning Engineer
- Creative AI Engineer

### 2. AWS Generative AI Developer Professional preparation

The project maps directly to important AWS Generative AI Developer Professional concepts:

- Amazon Bedrock model invocation
- Bedrock Agents and action groups
- Bedrock Knowledge Bases for RAG
- Bedrock Guardrails for safety and governance
- AWS Lambda tool execution
- Step Functions workflow orchestration
- S3 based asset and document storage
- OpenSearch Serverless vector search
- IAM, KMS, Secrets Manager, Cognito, CloudWatch, and X-Ray
- Cost, latency, reliability, and troubleshooting patterns

---

## Nebula Flux Design Identity

WebCut.ai uses a futuristic visual identity called **Nebula Flux**.

| Token | Hex | Meaning |
|---|---:|---|
| Void Black | `#060716` | Deep product background |
| Deep Space Navy | `#15102E` | Platform depth and structure |
| Nebula Purple | `#6D28D9` | AI reasoning and orchestration |
| Electric Cyan | `#00E5FF` | Speed, cloud, automation |
| Signal Pink | `#FF2D95` | Creative energy and media generation |
| Quantum Green | `#00F5A0` | Validation, success, trusted output |
| AWS Amber | `#FF9900` | AWS infrastructure and cost awareness |

---

## Product Architecture

```mermaid
flowchart TB
    USER[User] --> WEB[Next.js Web App]
    WEB --> API[FastAPI Backend]

    API --> AUTH[Amazon Cognito]
    API --> WORKFLOW[AWS Step Functions]
    WORKFLOW --> AGENT[Amazon Bedrock Agent]

    AGENT --> KB[Bedrock Knowledge Base]
    KB --> S3DOCS[S3 Brand and Product Documents]
    KB --> VECTOR[OpenSearch Serverless Vector Store]

    AGENT --> TOOLS[Lambda Action Groups]
    TOOLS --> IMAGE[Image Intelligence Service]
    TOOLS --> SPEECH[Speech Intelligence Service]
    TOOLS --> VIDEO[Video Enhancement Service]
    TOOLS --> EXPORT[Export Service]
    TOOLS --> SHOPIFY[Shopify Draft Publishing]

    AGENT --> GUARD[Bedrock Guardrails]
    GUARD --> OUTPUT[Validated Creative Package]

    OUTPUT --> DB[DynamoDB or Aurora PostgreSQL]
    OUTPUT --> ASSETS[S3 Generated Assets]
    OUTPUT --> EDITOR[Editable Online Content Editor]

    API --> OBS[CloudWatch, X-Ray, OpenTelemetry]

    classDef user fill:#060716,stroke:#00E5FF,color:#FFFFFF,stroke-width:2px;
    classDef app fill:#15102E,stroke:#00E5FF,color:#FFFFFF,stroke-width:2px;
    classDef ai fill:#1B0B3A,stroke:#6D28D9,color:#FFFFFF,stroke-width:2px;
    classDef media fill:#260018,stroke:#FF2D95,color:#FFFFFF,stroke-width:2px;
    classDef data fill:#001F2A,stroke:#00F5A0,color:#FFFFFF,stroke-width:2px;
    classDef ops fill:#2A1800,stroke:#FF9900,color:#FFFFFF,stroke-width:2px;

    class USER user;
    class WEB,API,AUTH,WORKFLOW app;
    class AGENT,KB,GUARD ai;
    class IMAGE,SPEECH,VIDEO,EXPORT,SHOPIFY media;
    class S3DOCS,VECTOR,DB,ASSETS,OUTPUT,EDITOR data;
    class OBS ops;
```

---

## First Working Workflow

```mermaid
sequenceDiagram
    actor User
    participant Web as Next.js App
    participant API as FastAPI Backend
    participant SFN as AWS Step Functions
    participant Agent as Bedrock Agent
    participant KB as Knowledge Base
    participant Tool as Lambda Action Tool
    participant Guard as Bedrock Guardrails
    participant Store as S3 and Database

    User->>Web: Enter campaign brief and upload assets
    Web->>API: Submit generation request
    API->>SFN: Start creative workflow
    SFN->>Agent: Plan content generation
    Agent->>KB: Retrieve brand and product context
    KB-->>Agent: Return grounded context
    Agent->>Tool: Generate editable design JSON
    Tool-->>Agent: Return structured creative layout
    Agent->>Guard: Validate safety and compliance
    Guard-->>Agent: Return approved response
    Agent->>Store: Save output and audit record
    Store-->>API: Return generated package
    API-->>Web: Show editable creative output
    Web-->>User: Preview, revise, export, or approve
```

---

## Core User Story

> As a content creator or ecommerce operator, I want to enter a campaign brief and upload product media so that WebCut.ai can generate brand aligned creative assets, improve media quality, produce copy, validate compliance, and prepare export ready content.

Example input:

```text
Create a premium launch campaign for a black leather handbag.
Generate an Instagram post, ecommerce hero banner, product caption, voiceover script, and short video plan.
Use a minimal luxury tone and prepare the assets for review before publishing.
```

Example output:

```json
{
  "campaign_name": "Luxury Handbag Launch",
  "status": "ready_for_review",
  "assets": [
    {
      "type": "instagram_post",
      "format": "1080x1080",
      "headline": "Designed for Everyday Luxury",
      "description": "Minimal product focused layout with premium spacing and refined typography"
    },
    {
      "type": "ecommerce_hero_banner",
      "format": "1920x720",
      "headline": "The New Standard in Everyday Luxury",
      "description": "Wide hero layout with product cutout, neutral background, and clear call to action"
    },
    {
      "type": "voiceover_script",
      "duration_seconds": 15,
      "script": "Meet the everyday essential designed with a premium finish and timeless detail."
    },
    {
      "type": "short_video_plan",
      "duration_seconds": 12,
      "scenes": [
        "Product reveal with clean background",
        "Close up material detail",
        "Offer and call to action"
      ]
    }
  ],
  "compliance": {
    "brand_aligned": true,
    "unsupported_claims_detected": false,
    "human_approval_required": true
  }
}
```

---

## Agentic System Design

```mermaid
mindmap
  root((WebCut.ai Agent System))
    CreativeOps Orchestrator
      Plans workflow
      Selects tools
      Tracks state
      Routes approval
    Brand RAG Agent
      Retrieves brand rules
      Reads product documents
      Grounds generation
      Provides citations
    Design Agent
      Creates editable JSON
      Chooses layout structure
      Manages asset sizes
      Produces visual hierarchy
    Copy Agent
      Captions
      Product descriptions
      SEO text
      Ad copy
    Image Intelligence Agent
      Background removal
      Smart crop
      Object cleanup
      Product cutout
      Upscaling
    Speech Agent
      Text to Speech
      Speech to Text
      Transcript generation
      Voiceover scripts
    Video Enhancement Agent
      Denoising
      Sharpening
      4K enhancement
      Captions
      MP4 export
    Compliance Agent
      Brand checks
      Guardrails
      Claim validation
      Human approval gate
    Evaluation Agent
      Quality score
      RAG relevance
      Latency
      Cost
```

---

## AWS Services

| Layer | AWS Service | Purpose |
|---|---|---|
| Foundation models | Amazon Bedrock | Generate creative plans, copy, structured JSON, scripts |
| Agents | Amazon Bedrock Agents | Orchestrate tools, actions, and creative workflows |
| RAG | Bedrock Knowledge Bases | Retrieve brand guides, product data, policies, campaign examples |
| Vector search | OpenSearch Serverless | Store and search embeddings |
| Safety | Bedrock Guardrails | Apply safety, privacy, and compliance controls |
| Workflow | AWS Step Functions | Durable workflow orchestration, retries, catch states, approvals |
| Tools | AWS Lambda | Action group execution and lightweight service tools |
| Backend compute | ECS Fargate or App Runner | Host FastAPI backend |
| Storage | Amazon S3 | Store documents, media uploads, exports, generated assets |
| Auth | Amazon Cognito | User authentication and workspace access |
| Database | DynamoDB | Campaigns, jobs, outputs, agent traces |
| Relational option | Aurora PostgreSQL | Optional relational data model |
| Queue | Amazon SQS | Async jobs for heavy media processing |
| Events | EventBridge | Trigger automations and system events |
| Secrets | Secrets Manager | Store integration keys and tokens |
| Encryption | KMS | Encrypt data, assets, and secrets |
| Monitoring | CloudWatch | Logs, metrics, alarms, dashboards |
| Tracing | X-Ray | Distributed request tracing |
| Infrastructure | AWS CDK | Infrastructure as Code deployment |

---

## Modern AI Frameworks

The production backbone is AWS native. Additional tools are integrated through controlled adapters.

```mermaid
flowchart LR
    CORE[AWS Native Core] --> LC[LangChain Adapter]
    CORE --> LG[LangGraph Agent Workflow]
    CORE --> MCP[MCP Tool Server]
    CORE --> N8N[n8n Automation]
    CORE --> LI[LlamaIndex RAG Lab]
    CORE --> CREW[CrewAI Lab]
    CORE --> AUTOGEN[AutoGen Lab]
    CORE --> SK[Semantic Kernel Lab]
    CORE --> DSPY[DSPy Prompt Optimisation]
    CORE --> LOCAL[Ollama and vLLM Lab]

    LC --> EVAL[Shared Evaluation Layer]
    LG --> EVAL
    MCP --> EVAL
    N8N --> EVAL
    LI --> EVAL
    CREW --> EVAL
    AUTOGEN --> EVAL
    SK --> EVAL
    DSPY --> EVAL
    LOCAL --> EVAL
```

| Tool | Use in WebCut.ai |
|---|---|
| LangChain | Tool wrappers, retrievers, prompt templates, model abstraction |
| LangGraph | Stateful multi agent workflow comparison |
| n8n | Visual business automation and approval workflows |
| MCP | External tool server for agent interoperability |
| LlamaIndex | Alternative RAG implementation lab |
| CrewAI | Multi agent role based experimentation |
| AutoGen | Conversational multi agent experimentation |
| Semantic Kernel | Enterprise orchestration comparison |
| DSPy | Prompt optimisation and evaluation |
| Pydantic AI | Typed Python agent experiments |
| LiteLLM | Multi provider model gateway experiments |
| Ollama | Local model experimentation |
| vLLM | Local inference serving lab |

---

## Media Intelligence Pipeline

```mermaid
flowchart TB
    UPLOAD[Media Upload] --> TYPE{Media Type}

    TYPE --> IMG[Image Pipeline]
    TYPE --> AUD[Audio Pipeline]
    TYPE --> VID[Video Pipeline]

    IMG --> IMG1[Background Removal]
    IMG --> IMG2[Smart Crop]
    IMG --> IMG3[Object Cleanup]
    IMG --> IMG4[Product Cutout]
    IMG --> IMG5[Image Upscaling]

    AUD --> AUD1[Speech to Text]
    AUD --> AUD2[Text to Speech]
    AUD --> AUD3[Transcript Summary]
    AUD --> AUD4[Voiceover Generation]

    VID --> VID1[Video Denoising]
    VID --> VID2[Video Sharpening]
    VID --> VID3[4K Enhancement]
    VID --> VID4[Caption Generation]
    VID --> VID5[Short Form Export]

    IMG5 --> PACKAGE[Creative Asset Package]
    AUD4 --> PACKAGE
    VID5 --> PACKAGE
```

---

## Security and Governance

```mermaid
flowchart TB
    USER[User] --> COG[Cognito Authentication]
    COG --> TOKEN[JWT Token]
    TOKEN --> GATEWAY[API Gateway Authorizer]
    GATEWAY --> RBAC[FastAPI RBAC Middleware]
    RBAC --> IAM[IAM Least Privilege Roles]
    IAM --> S3[S3 Presigned URLs]
    IAM --> SECRETS[Secrets Manager]
    IAM --> KMS[KMS Encryption]
    IAM --> BEDROCK[Bedrock Guardrails]
    RBAC --> AUDIT[Audit Logs and Agent Trace Records]
```

| Concern | Control |
|---|---|
| User access | Cognito and role based access control |
| AWS access | IAM least privilege |
| File security | S3 presigned URLs and bucket policies |
| Secrets | Secrets Manager |
| Encryption | KMS |
| AI safety | Bedrock Guardrails |
| Publishing risk | Human approval before external publishing |
| Prompt injection | Input validation and isolated context retrieval |
| Auditability | Agent runs, tool calls, workflow execution records |

---

## Observability

```mermaid
flowchart LR
    REQ[Request] --> TRACE[Trace ID]
    TRACE --> API[FastAPI Logs]
    API --> SFN[Step Functions History]
    SFN --> BEDROCK[Bedrock Metrics]
    BEDROCK --> TOOLS[Tool Call Logs]
    TOOLS --> DASH[CloudWatch Dashboard]
    DASH --> XRAY[X-Ray Trace Map]
    DASH --> COST[Cost and Token Report]
    DASH --> EVAL[Quality Evaluation Report]
```

Tracked metrics:

| Metric | Why it matters |
|---|---|
| Request latency | User experience |
| Model latency | AI performance |
| Token usage | Cost control |
| RAG retrieval score | Grounding quality |
| Tool failure rate | Agent reliability |
| Guardrail interventions | Safety monitoring |
| Human revision rate | Output quality |
| Export failure rate | Media pipeline reliability |
| Cost per campaign | Business viability |

---

## Repository Structure

```text
WebCut.ai-CreativeOps-Agent-Platform/
│
├── README.md
├── docs/
│   ├── 00_project_vision.md
│   ├── 01_aws_exam_mapping.md
│   ├── 02_architecture.md
│   ├── 03_agent_workflows.md
│   ├── 04_rag_design.md
│   ├── 05_security_guardrails.md
│   ├── 06_evaluation_strategy.md
│   ├── 07_deployment.md
│   └── 08_tool_comparison.md
│
├── apps/
│   ├── web/
│   └── api/
│
├── services/
│   ├── image-service/
│   ├── speech-service/
│   ├── video-service/
│   ├── export-service/
│   ├── shopify-service/
│   └── eval-service/
│
├── agents/
│   ├── aws-bedrock-agent/
│   ├── langgraph-agent/
│   ├── langchain-agent/
│   ├── n8n-workflows/
│   ├── mcp-server/
│   └── local-model-lab/
│
├── infra/
│   ├── cdk/
│   ├── docker/
│   └── diagrams/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── e2e/
│   └── evals/
│
├── docker-compose.yml
└── .github/
    └── workflows/
```

---

## Implementation Roadmap

```mermaid
gantt
    title WebCut.ai Build Roadmap
    dateFormat  YYYY-MM-DD

    section Foundation
    Project identity and README           :done, r1, 2026-05-18, 1d
    Repo structure and backend starter    :r2, 2026-05-18, 1d
    Campaign generation API               :r3, 2026-05-19, 1d

    section AWS GenAI Core
    Bedrock provider wrapper              :r4, 2026-05-20, 1d
    Guardrails integration                :r5, 2026-05-21, 1d
    Knowledge Base RAG                    :r6, 2026-05-22, 2d
    Step Functions workflow               :r7, 2026-05-24, 2d

    section Agentic AI
    Bedrock Agent action groups           :r8, 2026-05-26, 2d
    LangGraph workflow                    :r9, 2026-05-28, 2d
    MCP server                            :r10, 2026-05-30, 2d
    n8n workflows                         :r11, 2026-06-01, 2d

    section Product Experience
    Next.js dashboard                     :r12, 2026-06-03, 3d
    Online content editor                 :r13, 2026-06-06, 4d
    Export workflow                       :r14, 2026-06-10, 2d

    section Media Intelligence
    Image intelligence service            :r15, 2026-06-12, 3d
    Speech AI service                     :r16, 2026-06-15, 2d
    Video enhancement service             :r17, 2026-06-17, 4d

    section Production
    CI/CD and tests                       :r18, 2026-06-21, 2d
    AWS CDK deployment                    :r19, 2026-06-23, 3d
    Observability and cost dashboard      :r20, 2026-06-26, 2d
```

---

## Build Phases

### Phase 1: Foundation

- Create project folder structure
- Add FastAPI backend
- Add campaign request and response schemas
- Add mock Bedrock compatible provider
- Add first campaign generation endpoint
- Add tests
- Commit and push cleanly

### Phase 2: AWS Bedrock Core

- Add Amazon Bedrock runtime integration
- Add prompt templates
- Add structured output validation
- Add model configuration
- Add token and latency tracking

### Phase 3: Retrieval Augmented Generation

- Add S3 document storage
- Add Bedrock Knowledge Base integration
- Add OpenSearch Serverless vector store
- Add citations and retrieval scores
- Add RAG evaluation tests

### Phase 4: Agents and Tools

- Create CreativeOps Orchestrator Agent
- Add Lambda action groups
- Define tool schemas
- Add tool call tracing
- Add failure handling and retries

### Phase 5: Workflow Orchestration

- Add Step Functions workflow
- Add retry, catch, and timeout states
- Add human approval state
- Add workflow status API
- Add EventBridge triggers

### Phase 6: Frontend Product Experience

- Add Next.js dashboard
- Add campaign brief form
- Add generated asset preview
- Add editable online content editor
- Add export panel

### Phase 7: Media Intelligence

- Add background removal
- Add product cutout
- Add Text to Speech
- Add Speech to Text
- Add video denoising
- Add video sharpening
- Add 4K enhancement
- Add captions and export workflow

### Phase 8: Advanced Automation and Labs

- Add LangGraph workflow version
- Add LangChain adapter
- Add n8n workflow automations
- Add MCP server
- Add LlamaIndex, CrewAI, AutoGen, Semantic Kernel, DSPy, Ollama, and vLLM labs

---

## Local Development

Backend setup:

```bash
cd apps/api
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Frontend setup:

```bash
cd apps/web
npm install
npm run dev
```

Docker setup planned:

```bash
docker compose up --build
```

---

## Example Design JSON

WebCut.ai produces editable structured creative layouts.

```json
{
  "campaign_name": "Nebula Launch Campaign",
  "assets": [
    {
      "type": "social_post",
      "format": "1080x1080",
      "layout": {
        "background": {
          "type": "gradient",
          "colors": ["#060716", "#6D28D9", "#00E5FF"]
        },
        "layers": [
          {
            "type": "text",
            "name": "headline",
            "text": "Create the Future of Your Brand",
            "x": 80,
            "y": 160,
            "font_size": 64,
            "font_weight": "bold",
            "color": "#FFFFFF"
          },
          {
            "type": "image",
            "name": "product_cutout",
            "x": 620,
            "y": 180,
            "width": 360,
            "height": 520
          },
          {
            "type": "text",
            "name": "call_to_action",
            "text": "Explore the launch",
            "x": 80,
            "y": 760,
            "font_size": 32,
            "color": "#00E5FF"
          }
        ]
      }
    }
  ],
  "compliance": {
    "brand_aligned": true,
    "human_approval_required": true
  }
}
```

---

## Interview Pitch

> I built WebCut.ai CreativeOps Agent Platform as an AWS native full stack AI system for one stop online content creation and AI media intelligence. The platform uses Amazon Bedrock, Bedrock Agents, Knowledge Bases, Guardrails, Lambda action groups, Step Functions, S3, OpenSearch Serverless, FastAPI, Next.js, and modern agent framework adapters such as LangGraph, LangChain, n8n, and MCP. It supports brand grounded creative generation, editable design JSON, Text to Speech, Speech to Text, image enhancement, video denoising, video sharpening, 4K enhancement, human approval workflows, observability, and production deployment patterns.

---

## Current Status

| Area | Status |
|---|---|
| Project identity | In progress |
| AWS architecture | Planned |
| FastAPI backend | Next |
| Bedrock integration | Planned |
| RAG integration | Planned |
| Agent workflow | Planned |
| Frontend | Planned |
| Media services | Planned |
| Deployment | Planned |

---

## Final Statement

<div align="center">

<h2>WebCut.ai is a one stop online content creation, AI media intelligence, and creative automation platform powered by AWS native generative AI architecture.</h2>

<img src="https://capsule-render.vercel.app/api?type=rect&height=110&color=0:060716,35:6D28D9,70:FF2D95,100:00E5FF&text=Create%20%7C%20Enhance%20%7C%20Automate%20%7C%20Govern%20%7C%20Scale&fontColor=FFFFFF&fontSize=24&animation=twinkling" alt="Create Enhance Automate Govern Scale" />

</div>
"""

readme_path.write_text(readme, encoding="utf-8", newline="\n")
print(f"Wrote README: {readme_path}")

commands = [
    ["git", "status"],
    ["git", "add", "README.md"],
    ["git", "commit", "-m", "Redesign README with premium WebCut platform identity"],
    ["git", "push", "origin", "main"],
]

for command in commands:
    print("\n> " + " ".join(command))
    result = subprocess.run(command, cwd=repo, text=True)
    if result.returncode != 0:
        if command[1] == "commit":
            print("No commit created. There may be no README changes.")
            continue
        sys.exit(result.returncode)

print("\nDone.")
