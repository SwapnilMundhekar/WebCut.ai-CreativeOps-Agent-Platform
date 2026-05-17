<!--
WebCut.ai CreativeOps Agent Platform
Modern GitHub README
-->

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=220&color=0:0F172A,45:2563EB,100:7C3AED&text=WebCut.ai%20CreativeOps%20Agent%20Platform&fontColor=FFFFFF&fontSize=34&fontAlignY=38&desc=AWS%20Native%20Full%20Stack%20AI%20Agent%20Platform%20for%20Creative%20Automation&descAlignY=58&animation=fadeIn" alt="WebCut.ai CreativeOps Agent Platform animated header" />

<br />

<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=700&size=24&duration=2600&pause=700&color=38BDF8&center=true&vCenter=true&width=900&lines=Amazon+Bedrock+Agents+%2B+Knowledge+Bases+%2B+Guardrails;FastAPI+%2B+Next.js+%2B+Python+AI+Services;LangGraph+%2B+LangChain+%2B+n8n+%2B+MCP+Adapters;Canva-style+CreativeOps+SaaS+for+Ecommerce+Teams;Built+for+AWS+GenAI+Developer+Professional+Revision" alt="Animated technology summary" />

<br />

<p>
  <img src="https://img.shields.io/badge/AWS-Bedrock-orange?style=for-the-badge&logo=amazonaws&logoColor=white" alt="AWS Bedrock" />
  <img src="https://img.shields.io/badge/Agents-Tool%20Calling-7C3AED?style=for-the-badge" alt="Agents" />
  <img src="https://img.shields.io/badge/RAG-Knowledge%20Bases-2563EB?style=for-the-badge" alt="RAG" />
  <img src="https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Frontend-Next.js-111111?style=for-the-badge&logo=nextdotjs&logoColor=white" alt="Next.js" />
  <img src="https://img.shields.io/badge/Orchestration-LangGraph-00A67E?style=for-the-badge" alt="LangGraph" />
</p>

<p>
  <img src="https://img.shields.io/badge/Status-Architecture%20First-blue?style=flat-square" alt="Status" />
  <img src="https://img.shields.io/badge/Goal-Job%20Portfolio%20%2B%20AWS%20Exam-success?style=flat-square" alt="Goal" />
  <img src="https://img.shields.io/badge/Design-Production%20Grade-critical?style=flat-square" alt="Design" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square" alt="License" />
</p>

</div>

---

## Executive Summary

**WebCut.ai CreativeOps Agent Platform** is an AWS native, full stack, agentic AI platform for generating brand compliant ecommerce and social media creative assets.

The project combines a **Canva style design experience** with **Amazon Bedrock powered AI agents**, **Retrieval Augmented Generation**, **image processing**, **workflow automation**, **cloud security**, **observability**, and **modern AI framework adapters**.

It is designed as a flagship portfolio project for:

- AI Engineer roles
- Generative AI Developer roles
- Agentic AI Engineer roles
- Full Stack AI Engineer roles
- Python Backend Engineer roles
- AWS AI Engineer roles
- Automation Engineer roles

It is also designed to support practical revision for the **AWS Certified Generative AI Developer Professional** exam by mapping every major product module to real AWS generative AI architecture patterns.

---

## Product Vision

WebCut.ai turns this:

> Create an Instagram post, Shopify hero banner, and Google Ads creative for this product. Use my brand guide, keep the design premium, remove the background, generate ecommerce copy, and prepare everything for approval.

Into this:

- Editable Instagram post
- Editable Shopify banner
- Product cutout with background removed
- Campaign concept
- Product description
- Search Engine Optimisation copy
- Social captions
- Voiceover script
- Brand compliance report
- Agent trace summary
- Export package
- Optional Shopify draft update

The key principle is simple:

> **Do not generate only a flat image. Generate an editable, auditable, brand grounded creative workflow.**

---

## Why This Project Exists

Modern AI jobs are no longer asking for only notebooks or chatbot demos.

They expect engineers who can build systems with:

- Cloud native generative AI services
- Agent orchestration
- Tool calling
- Retrieval Augmented Generation
- Model safety and guardrails
- Full stack application design
- Background jobs
- Workflow orchestration
- API integration
- Observability
- Cost control
- Security
- Testing
- Deployment

This repository is built to demonstrate those skills in one coherent end to end platform.

---

## The Gigasaurus Principle

This project intentionally touches a wide modern AI ecosystem, but it does **not** put every tool in the critical path.

### Bad Pattern

```mermaid
flowchart TD
    A[User Request] --> B[LangChain]
    B --> C[LangGraph]
    C --> D[n8n]
    D --> E[Random Agent Framework]
    E --> F[Bedrock Agent]
    F --> G[Unclear Tool]
    G --> H[Fragile Output]
```

### Correct Pattern

```mermaid
flowchart TD
    A[AWS Production Core] --> B[Stable Application APIs]
    B --> C[Framework Adapters]
    C --> D[Optional Labs]
    D --> E[Measured Experiments]
    E --> F[Documented Trade Offs]
```

The production backbone is AWS native. Other frameworks are implemented as adapters or labs.

---

## High Level Platform Architecture

```mermaid
flowchart TB
    U[User] --> FE[Next.js Frontend<br/>Creative Studio UI]
    FE --> APIGW[Amazon API Gateway]
    APIGW --> API[FastAPI Backend<br/>Python Application Layer]
    API --> AUTH[Amazon Cognito<br/>Authentication and User Pools]
    API --> SFN[AWS Step Functions<br/>Durable Creative Workflow]
    SFN --> AGENT[Amazon Bedrock Agent<br/>CreativeOps Orchestrator]
    AGENT --> KB[Amazon Bedrock Knowledge Bases<br/>Brand and Product RAG]
    AGENT --> LAMBDA[AWS Lambda Action Groups<br/>Tool Execution]
    LAMBDA --> S3[Amazon S3<br/>Images, Brand Docs, Exports]
    LAMBDA --> DB[(DynamoDB or Aurora PostgreSQL<br/>Projects, Jobs, Assets)]
    KB --> OSS[Amazon OpenSearch Serverless<br/>Vector Search]
    AGENT --> GR[Amazon Bedrock Guardrails<br/>Safety and Policy Controls]
    SFN --> SQS[Amazon SQS<br/>Async Jobs]
    SFN --> EB[Amazon EventBridge<br/>Business Events]
    API --> CW[Amazon CloudWatch<br/>Logs and Metrics]
    API --> XR[AWS X-Ray and OpenTelemetry<br/>Distributed Tracing]
    API --> SEC[AWS Secrets Manager and KMS<br/>Secrets and Encryption]
```

---

## Core User Workflow

```mermaid
sequenceDiagram
    actor User
    participant Web as Next.js Studio
    participant API as FastAPI Backend
    participant SFN as Step Functions
    participant Agent as Bedrock Agent
    participant KB as Bedrock Knowledge Base
    participant Tool as Lambda Action Group
    participant Guard as Bedrock Guardrails
    participant Store as S3 and Database

    User->>Web: Enter campaign brief and upload product assets
    Web->>API: Submit creative generation request
    API->>SFN: Start creative workflow
    SFN->>Agent: Ask orchestrator to plan next actions
    Agent->>KB: Retrieve brand and product context
    KB-->>Agent: Return grounded context and citations
    Agent->>Tool: Call image, copy, design, or export tools
    Tool-->>Agent: Return structured tool results
    Agent->>Guard: Validate prompt and generated output
    Guard-->>Agent: Allow, block, mask, or flag output
    Agent-->>SFN: Return final structured campaign package
    SFN->>Store: Save output, assets, status, and trace
    Store-->>API: Return saved project reference
    API-->>Web: Send editable design JSON and status
    Web-->>User: Show preview, editor, and approval controls
```

---

## AWS Native Service Map

| Capability | AWS Service | Purpose in WebCut.ai |
|---|---|---|
| Foundation model access | Amazon Bedrock | Generate campaign plans, copy, design instructions, and summaries |
| Agentic orchestration | Amazon Bedrock Agents | Coordinate tools, RAG, image operations, compliance, and publishing |
| Tool execution | AWS Lambda | Execute action groups for image tools, exports, Shopify, and database operations |
| Long running workflow | AWS Step Functions | Run durable, observable, retryable creative generation workflows |
| Visual GenAI workflow | Amazon Bedrock Flows | Optional visual workflow for prompt, model, Lambda, and Knowledge Base nodes |
| Retrieval Augmented Generation | Amazon Bedrock Knowledge Bases | Ground outputs in brand guides, product data, policy docs, and previous campaigns |
| Vector search | Amazon OpenSearch Serverless | Store and retrieve embeddings for semantic search |
| Object storage | Amazon S3 | Store uploads, source documents, generated images, and exports |
| Safety controls | Amazon Bedrock Guardrails | Filter unsafe content, sensitive information, denied topics, and policy violations |
| Authentication | Amazon Cognito | User sign up, sign in, identity, and workspace access |
| REST API boundary | Amazon API Gateway | Secure public API entry point |
| App data | DynamoDB or Aurora PostgreSQL | Store users, projects, jobs, assets, agent runs, and audit records |
| Async queue | Amazon SQS | Queue long running creative, video, and image processing jobs |
| Event automation | Amazon EventBridge | Trigger automations such as report generation and workflow notifications |
| Secrets | AWS Secrets Manager | Store provider keys, Shopify tokens, and integration secrets |
| Encryption | AWS Key Management Service | Encrypt assets, secrets, database records, and sensitive outputs |
| Logging and metrics | Amazon CloudWatch | Monitor logs, latency, failures, throughput, and costs |
| Distributed tracing | AWS X-Ray and OpenTelemetry | Trace API requests, model calls, tools, and workflow steps |
| Infrastructure as Code | AWS CDK | Deploy repeatable AWS infrastructure |
| Frontend hosting | AWS Amplify or CloudFront with S3 | Host the web application |

---

## AWS Exam Mapping

```mermaid
mindmap
  root((AWS GenAI Developer Professional Revision))
    Amazon Bedrock
      Model invocation
      Inference parameters
      Prompt engineering
      Structured outputs
      Cost and latency
    Agents
      Action groups
      Lambda tools
      OpenAPI schemas
      Tool failure handling
      Agent traces
    Knowledge Bases
      Retrieval Augmented Generation
      Chunking
      Embeddings
      Vector stores
      Citations
    Guardrails
      Content filters
      Denied topics
      Sensitive information filters
      Contextual grounding
      Agent and knowledge base integration
    Workflow
      Step Functions
      Retry and Catch
      Timeout
      Human approval
      EventBridge
    Security
      IAM least privilege
      Cognito
      KMS
      Secrets Manager
      S3 policies
    Operations
      CloudWatch
      X-Ray
      OpenTelemetry
      Cost tracking
      Evaluation
```

---

## Agent Architecture

```mermaid
flowchart LR
    ORCH[CreativeOps Orchestrator Agent] --> BRAND[Brand RAG Agent]
    ORCH --> PROD[Product Intelligence Agent]
    ORCH --> CD[Creative Director Agent]
    ORCH --> DESIGN[Design Agent]
    ORCH --> COPY[Copywriting Agent]
    ORCH --> IMG[Image Editing Tool Agent]
    ORCH --> COMP[Compliance Agent]
    ORCH --> SHOP[Shopify Publishing Agent]
    ORCH --> EVAL[Evaluation Agent]
    ORCH --> ANA[Analytics Agent]

    BRAND --> KB[Bedrock Knowledge Bases]
    PROD --> S3[S3 Product Assets]
    DESIGN --> JSON[Editable Design JSON]
    IMG --> CV[OpenCV, Pillow, PyTorch, FFmpeg]
    COMP --> GR[Bedrock Guardrails]
    SHOP --> API[Shopify Admin API]
    EVAL --> METRICS[Quality, Cost, Latency, Safety]
```

---

## Agent Responsibilities

| Agent or Tool | Responsibility |
|---|---|
| CreativeOps Orchestrator Agent | Plans the workflow and decides which tools to call |
| Brand RAG Agent | Retrieves brand rules, tone, visual identity, product facts, and citations |
| Product Intelligence Agent | Extracts useful product information from image, CSV, or Shopify input |
| Creative Director Agent | Defines creative concept, target audience, asset set, and messaging angle |
| Design Agent | Produces editable layout JSON for the Canva style editor |
| Copywriting Agent | Generates headlines, captions, descriptions, and search engine copy |
| Image Editing Tool Agent | Runs background removal, crop, enhancement, object cleanup, and export tools |
| Compliance Agent | Checks brand consistency, safety, unsupported claims, and policy risk |
| Shopify Publishing Agent | Prepares ecommerce draft content and product asset packages |
| Evaluation Agent | Scores output quality, retrieval relevance, safety, and schema validity |
| Analytics Agent | Reports cost, latency, tool calls, failures, and improvement suggestions |

---

## Framework Adapter Strategy

```mermaid
flowchart TB
    CORE[WebCut.ai Core API] --> AWS[AWS Native Runtime<br/>Bedrock + Step Functions + Lambda]
    CORE --> LG[LangGraph Runtime<br/>Stateful Agent Workflows]
    CORE --> LC[LangChain Adapter<br/>Tools, Retrievers, Prompt Templates]
    CORE --> N8N[n8n Adapter<br/>Visual Business Automation]
    CORE --> MCP[MCP Server<br/>Standard Tool Interface]
    CORE --> LLI[LlamaIndex Lab<br/>Alternative RAG]
    CORE --> CREW[CrewAI Lab<br/>Role Based Multi Agent Experiments]
    CORE --> AUTO[AutoGen Lab<br/>Conversational Agent Experiments]
    CORE --> SK[Semantic Kernel Lab<br/>Enterprise Agent Comparison]
    CORE --> DSPY[DSPy Lab<br/>Prompt Optimisation]
    CORE --> LOCAL[Local Model Lab<br/>Ollama, vLLM, Transformers]
```

---

## Technology Matrix

| Layer | Primary Stack | Alternative or Lab Stack |
|---|---|---|
| Frontend | Next.js, React, TypeScript, Tailwind CSS, shadcn/ui | Vite, React Native later |
| Editor | Fabric.js or Konva.js | SVG rendering, Canvas API |
| Backend | Python, FastAPI, Pydantic | Django REST Framework |
| AI Core | Amazon Bedrock | LiteLLM gateway, Anthropic, OpenAI, local models |
| AWS Agent Runtime | Bedrock Agents, Lambda action groups | LangGraph, CrewAI, AutoGen |
| RAG | Bedrock Knowledge Bases, OpenSearch Serverless | LlamaIndex, LangChain, pgvector, Qdrant |
| Workflow | Step Functions | n8n, LangGraph, Temporal later |
| Image Processing | OpenCV, Pillow, rembg, PyTorch | ONNX Runtime, Segment Anything style models |
| Video Processing | FFmpeg, MoviePy, Remotion | AWS Elemental MediaConvert later |
| Data | DynamoDB, Aurora PostgreSQL | PostgreSQL with pgvector |
| Storage | S3 | Local MinIO for development |
| Auth | Cognito | Auth.js or Clerk for local prototype |
| Events | EventBridge, SQS | Redis Queue or Celery locally |
| Observability | CloudWatch, X-Ray, OpenTelemetry | LangSmith optional |
| Infrastructure | AWS CDK | Terraform optional |
| Testing | Pytest, Playwright | DeepEval, RAGAS, Locust |

---

## Design JSON as the Core Output

WebCut.ai does not only return text. It returns structured design instructions that can be edited by the user.

```json
{
  "campaign_name": "Luxury Handbag Launch",
  "assets": [
    {
      "type": "instagram_post",
      "size": {
        "width": 1080,
        "height": 1080
      },
      "layers": [
        {
          "id": "background",
          "type": "shape",
          "shape": "rectangle",
          "fill": "#F7F1EA",
          "x": 0,
          "y": 0,
          "width": 1080,
          "height": 1080
        },
        {
          "id": "headline",
          "type": "text",
          "text": "The Winter Edit",
          "x": 80,
          "y": 160,
          "font_size": 72,
          "font_weight": "bold",
          "color": "#111827"
        },
        {
          "id": "product_image",
          "type": "image",
          "source": "s3://webcut-assets/product-cutout.png",
          "x": 520,
          "y": 210,
          "width": 420,
          "height": 520
        }
      ]
    }
  ],
  "brand_compliance_notes": [
    "Uses premium tone",
    "Keeps product claim conservative",
    "Uses neutral luxury palette"
  ]
}
```

---

## First Working Vertical Slice

```mermaid
flowchart TD
    A[Campaign Brief Input] --> B[FastAPI Endpoint]
    B --> C[Validate Request with Pydantic]
    C --> D[Call Amazon Bedrock Model]
    D --> E[Generate Structured Campaign JSON]
    E --> F[Validate JSON Schema]
    F --> G[Save Result Locally First]
    G --> H[Return Preview to Frontend]
    H --> I[Prepare S3, Knowledge Base, Guardrail, and Step Functions Integration]
```

### First User Story

As a user, I want to enter a campaign brief so that WebCut.ai can generate a brand aligned creative plan and editable design layout for social media and ecommerce.

### Example Input

```text
Create an Instagram post and Shopify hero banner for a black leather handbag.
Use a premium luxury tone, keep the design minimal, and include a launch offer.
```

### Example Output

```json
{
  "campaign_name": "Luxury Handbag Launch",
  "assets": [
    {
      "type": "instagram_post",
      "size": "1080x1080",
      "headline": "The Winter Edit",
      "subheadline": "Premium leather. Minimal elegance.",
      "call_to_action": "Shop the launch offer",
      "layout": {
        "background": "warm neutral gradient",
        "product_position": "right center",
        "text_position": "left center",
        "style": "minimal luxury ecommerce"
      }
    },
    {
      "type": "shopify_hero_banner",
      "size": "1920x720",
      "headline": "Designed for Everyday Luxury",
      "subheadline": "Launch offer available for a limited time",
      "call_to_action": "Shop Now"
    }
  ],
  "brand_compliance_notes": [
    "Uses a premium tone",
    "Avoids unsupported product claims",
    "Keeps text suitable for ecommerce use"
  ]
}
```

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
├── packages/
│   ├── shared-types/
│   └── design-schema/
│
├── services/
│   ├── image-service/
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
│   └── openclaw-style-assistant/
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
└── docker-compose.yml
```

---

## Delivery Roadmap

```mermaid
gantt
    title WebCut.ai Build Roadmap
    dateFormat  YYYY-MM-DD
    axisFormat  %b %d

    section Phase 1 AWS Foundation
    README and architecture                 :done, p1a, 2026-05-18, 1d
    FastAPI starter backend                 :p1b, 2026-05-19, 2d
    Bedrock model invocation wrapper        :p1c, 2026-05-21, 2d
    Structured design JSON endpoint         :p1d, 2026-05-23, 2d

    section Phase 2 RAG and Guardrails
    S3 document upload                      :p2a, 2026-05-25, 2d
    Bedrock Knowledge Base                  :p2b, 2026-05-27, 3d
    OpenSearch Serverless vector store      :p2c, 2026-05-30, 3d
    Bedrock Guardrails integration          :p2d, 2026-06-02, 2d

    section Phase 3 Agents and Workflow
    Bedrock Agent action groups             :p3a, 2026-06-04, 3d
    Lambda tools                            :p3b, 2026-06-07, 3d
    Step Functions workflow                 :p3c, 2026-06-10, 3d
    Agent run tracing                       :p3d, 2026-06-13, 2d

    section Phase 4 Product Experience
    Next.js dashboard                       :p4a, 2026-06-15, 4d
    Canva style editor                      :p4b, 2026-06-19, 5d
    Export service                          :p4c, 2026-06-24, 3d

    section Phase 5 Advanced Integrations
    LangGraph adapter                       :p5a, 2026-06-27, 3d
    n8n workflows                           :p5b, 2026-06-30, 3d
    MCP server                              :p5c, 2026-07-03, 3d
    Shopify connector                       :p5d, 2026-07-06, 4d
```

---

## System State Machine

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> ValidatingInput
    ValidatingInput --> RetrievingBrandContext
    RetrievingBrandContext --> PlanningCampaign
    PlanningCampaign --> GeneratingDesignJSON
    GeneratingDesignJSON --> RunningGuardrails
    RunningGuardrails --> HumanReview
    HumanReview --> Approved
    HumanReview --> NeedsRevision
    NeedsRevision --> PlanningCampaign
    Approved --> ExportingAssets
    ExportingAssets --> PublishedDraft
    PublishedDraft --> [*]

    ValidatingInput --> Failed: Invalid request
    RetrievingBrandContext --> Failed: RAG failure
    PlanningCampaign --> Failed: Model failure
    RunningGuardrails --> Blocked: Safety or policy issue
    Blocked --> NeedsRevision
    Failed --> [*]
```

---

## Data Model Overview

```mermaid
erDiagram
    USER ||--o{ WORKSPACE : owns
    WORKSPACE ||--o{ PROJECT : contains
    PROJECT ||--o{ ASSET : generates
    PROJECT ||--o{ AGENT_RUN : tracks
    AGENT_RUN ||--o{ TOOL_CALL : includes
    PROJECT ||--o{ BRAND_DOCUMENT : uses
    BRAND_DOCUMENT ||--o{ RAG_CHUNK : chunked_into
    PROJECT ||--o{ EXPORT_JOB : produces

    USER {
        string id
        string email
        string name
        datetime created_at
    }

    WORKSPACE {
        string id
        string name
        string owner_id
        string plan
    }

    PROJECT {
        string id
        string workspace_id
        string campaign_name
        string status
        datetime created_at
    }

    ASSET {
        string id
        string project_id
        string asset_type
        string s3_uri
        string design_json
    }

    AGENT_RUN {
        string id
        string project_id
        string runtime
        string status
        float cost_usd
        int latency_ms
    }

    TOOL_CALL {
        string id
        string agent_run_id
        string tool_name
        string status
        string input_hash
        string output_hash
    }

    BRAND_DOCUMENT {
        string id
        string workspace_id
        string s3_uri
        string document_type
    }

    RAG_CHUNK {
        string id
        string document_id
        string chunk_text
        string embedding_ref
    }

    EXPORT_JOB {
        string id
        string project_id
        string format
        string status
    }
```

---

## Quality Gates

```mermaid
flowchart LR
    A[Generated Output] --> B{Valid JSON Schema?}
    B -- No --> R1[Reject and Retry]
    B -- Yes --> C{Brand Grounded?}
    C -- No --> R2[Retrieve More Context]
    C -- Yes --> D{Guardrail Passed?}
    D -- No --> R3[Block or Revise]
    D -- Yes --> E{Human Approved?}
    E -- No --> R4[Send for Revision]
    E -- Yes --> F[Export or Publish Draft]
```

---

## Evaluation Strategy

| Evaluation Type | What It Checks | Example Metric |
|---|---|---|
| Schema evaluation | Output matches expected JSON structure | Pass or fail |
| RAG relevance | Retrieved context matches user request | Relevance score |
| Faithfulness | Generated output does not invent unsupported brand claims | Groundedness score |
| Safety evaluation | Prompt and response pass safety filters | Guardrail result |
| Design quality | Layout is usable, readable, and brand aligned | Human or rubric score |
| Agent reliability | Correct tool selected and called successfully | Tool success rate |
| Latency | Time from request to usable preview | Milliseconds |
| Cost | Token and infrastructure cost per generation | Estimated dollars |
| Regression | Old prompts still produce valid outputs | Test suite pass rate |

---

## Local Development Target

The local version should run without requiring every AWS resource immediately.

```mermaid
flowchart TD
    A[Developer Machine] --> B[Docker Compose]
    B --> C[FastAPI API]
    B --> D[Next.js Web App]
    B --> E[Local PostgreSQL]
    B --> F[Redis Queue]
    C --> G[Mock Bedrock Provider]
    C --> H[Optional Real Bedrock Provider]
    C --> I[Local File Storage]
```

This allows fast development first, then AWS integration module by module.

---

## Planned API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| `POST` | `/api/v1/campaigns/generate` | Generate campaign plan and design JSON |
| `POST` | `/api/v1/assets/upload` | Upload product images and brand documents |
| `GET` | `/api/v1/projects/{project_id}` | Read project details |
| `GET` | `/api/v1/projects/{project_id}/runs` | Read agent run history |
| `POST` | `/api/v1/exports` | Export design to PNG, JPG, PDF, or MP4 |
| `POST` | `/api/v1/rag/query` | Query brand knowledge base |
| `POST` | `/api/v1/guardrails/check` | Run safety and brand compliance check |
| `POST` | `/api/v1/shopify/draft` | Create Shopify draft update |
| `GET` | `/api/v1/health` | Health check |
| `GET` | `/api/v1/version` | Version metadata |

---

## AWS Production Deployment View

```mermaid
flowchart TB
    subgraph Edge
        CF[CloudFront]
        WAF[AWS WAF]
    end

    subgraph Frontend
        S3WEB[S3 Static Hosting or Amplify]
    end

    subgraph API
        APIGW[API Gateway]
        ECS[ECS Fargate or App Runner<br/>FastAPI]
        LBD[AWS Lambda Tools]
    end

    subgraph AI
        BR[Amazon Bedrock]
        BA[Bedrock Agents]
        BK[Bedrock Knowledge Bases]
        BG[Bedrock Guardrails]
        BF[Bedrock Flows]
    end

    subgraph Data
        S3DATA[S3 Assets Bucket]
        DDB[DynamoDB]
        AUR[Aurora PostgreSQL]
        OSS[OpenSearch Serverless]
        SEC[Secrets Manager]
        KMS[KMS]
    end

    subgraph Ops
        CW[CloudWatch]
        XR[X-Ray]
        OTEL[OpenTelemetry]
    end

    CF --> WAF
    WAF --> S3WEB
    WAF --> APIGW
    APIGW --> ECS
    ECS --> BA
    BA --> LBD
    BA --> BK
    BA --> BG
    ECS --> BF
    BK --> OSS
    LBD --> S3DATA
    LBD --> DDB
    ECS --> AUR
    ECS --> SEC
    SEC --> KMS
    ECS --> CW
    ECS --> XR
    ECS --> OTEL
```

---

## Security Architecture

```mermaid
flowchart TD
    A[User Login] --> B[Amazon Cognito]
    B --> C[JWT Access Token]
    C --> D[API Gateway Authorizer]
    D --> E[FastAPI Auth Middleware]
    E --> F[Workspace Role Check]
    F --> G[IAM Scoped AWS Calls]
    G --> H[S3 Presigned URL Access]
    G --> I[Bedrock Invocation Permission]
    G --> J[Secrets Manager Access]
    J --> K[KMS Decryption]
    E --> L[Audit Log]
```

Security controls include:

- Identity based access with Amazon Cognito
- Workspace level access control
- IAM least privilege policies
- S3 presigned URLs
- KMS encryption
- Secrets Manager for external API credentials
- Bedrock Guardrails for safety and privacy
- Audit logs for agent actions
- Human approval before external publishing

---

## Observability Dashboard Goals

```mermaid
pie title Observability Focus Areas
    "Model latency" : 25
    "Tool execution" : 20
    "RAG retrieval quality" : 20
    "Guardrail blocks" : 15
    "Infrastructure errors" : 10
    "Cost tracking" : 10
```

The platform will track:

- Request latency
- Token usage
- Estimated model cost
- Tool call count
- Tool failure count
- Retry count
- RAG retrieval scores
- Guardrail decisions
- Export job duration
- User approval rate

---

## n8n Automation Examples

```mermaid
flowchart LR
    A[New Shopify Product] --> B[n8n Workflow]
    B --> C[Call WebCut.ai API]
    C --> D[Generate Creative Pack]
    D --> E[Human Approval]
    E --> F[Create Shopify Draft]
    E --> G[Send Slack or Email Summary]
```

Example workflows:

- New Shopify product triggers creative pack generation
- Approved campaign sends assets to marketing channel
- Failed generation creates a GitHub issue
- High cost event notifies admin
- New brand guide upload triggers knowledge base ingestion
- Weekly creative performance summary is generated automatically

---

## MCP Tool Server Plan

The WebCut.ai Model Context Protocol server will expose controlled tools for agents.

```text
search_brand_guide
generate_campaign_plan
generate_design_json
remove_background
smart_crop
export_asset
check_brand_compliance
get_shopify_product
create_shopify_draft
calculate_generation_cost
run_quality_evaluation
```

Permission principle:

> External agents can draft, inspect, and request generation, but cannot publish or delete without explicit human approval.

---

## Build Phases

### Phase 1: AWS Foundation

- Replace legacy README
- Create project structure
- Build FastAPI backend
- Add Bedrock model invocation wrapper
- Add structured campaign output schema
- Add local project persistence
- Add unit tests

### Phase 2: RAG and Guardrails

- Upload brand documents to S3
- Create Bedrock Knowledge Base
- Connect OpenSearch Serverless vector store
- Add retrieval citations
- Add Bedrock Guardrails
- Add RAG quality tests

### Phase 3: Bedrock Agents and Step Functions

- Create CreativeOps Orchestrator Agent
- Add Lambda action groups
- Define tool schemas
- Add Step Functions workflow
- Add retry, catch, timeout, and approval states
- Add agent trace logging

### Phase 4: Web Studio

- Build Next.js dashboard
- Add creative generation form
- Add editable design preview
- Add Canva style editor
- Add asset history
- Add export buttons

### Phase 5: Media Tools

- Add background removal
- Add product cutout
- Add smart crop
- Add image enhancement
- Add video timeline generation
- Add MP4 export

### Phase 6: Ecommerce Automation

- Add Shopify product import
- Generate product descriptions
- Generate SEO metadata
- Generate product image packs
- Create draft product updates
- Add approval workflow

### Phase 7: Framework Labs

- Add LangGraph implementation
- Add LangChain adapter
- Add n8n workflows
- Add MCP server
- Add LlamaIndex RAG comparison
- Add CrewAI, AutoGen, Semantic Kernel, DSPy labs
- Add local model experiments with Ollama, vLLM, and Hugging Face Transformers

---

## Recruiter Positioning

This project demonstrates:

| Job Requirement | How WebCut.ai Proves It |
|---|---|
| Full stack engineering | Next.js frontend, FastAPI backend, editor, APIs, authentication |
| Python engineering | FastAPI, Pydantic, workers, AI services, tests |
| Cloud AI development | Amazon Bedrock, Agents, Knowledge Bases, Guardrails, Lambda |
| Agentic AI | Orchestrator agent, tool calling, action groups, workflows |
| RAG | Brand guide retrieval, citations, vector search, evaluation |
| Automation | Step Functions, EventBridge, SQS, n8n |
| Security | Cognito, IAM, KMS, Secrets Manager, Guardrails |
| Observability | CloudWatch, X-Ray, OpenTelemetry, cost tracking |
| DevOps | Docker, GitHub Actions, CDK, deployment |
| Product thinking | Real ecommerce creative workflow with approval and publishing |

---

## Resume Bullet

> Built WebCut.ai CreativeOps Agent Platform, an AWS native full stack AI SaaS system for generating ecommerce and social media creative assets using Amazon Bedrock, Bedrock Agents, Knowledge Bases, Guardrails, Lambda action groups, Step Functions, S3, OpenSearch Serverless, FastAPI, Next.js, and CloudWatch. Designed agentic workflows for campaign planning, brand grounded RAG, editable design JSON generation, compliance validation, image processing, export automation, and Shopify draft publishing.

---

## Interview Pitch

> WebCut.ai is my flagship full stack AI engineering project. It is a Canva style creative automation platform where ecommerce teams upload product data and brand guides, then AWS powered AI agents generate editable, brand compliant creative assets. The production backbone uses Amazon Bedrock, Bedrock Agents, Knowledge Bases, Guardrails, Lambda action groups, Step Functions, S3, OpenSearch Serverless, FastAPI, Next.js, and CloudWatch. Around that core, I built adapters for LangGraph, LangChain, n8n, MCP, and local model experimentation so I can compare orchestration patterns and production trade offs.

---

## Current Status

```mermaid
flowchart LR
    A[Project Vision] --> B[Modern README]
    B --> C[Repository Structure]
    C --> D[FastAPI Starter]
    D --> E[Bedrock Wrapper]
    E --> F[RAG and Guardrails]
    F --> G[Agents and Step Functions]
    G --> H[Frontend Studio]
    H --> I[Production Deployment]

    A:::done
    B:::active

    classDef done fill:#16a34a,color:#ffffff,stroke:#166534;
    classDef active fill:#2563eb,color:#ffffff,stroke:#1e3a8a;
```

---

## Next Engineering Step

Create the first working backend vertical slice:

```text
apps/api
  app/main.py
  app/config.py
  app/models/campaign.py
  app/services/bedrock_client.py
  app/routes/campaigns.py
  tests/test_campaigns.py
```

The first backend endpoint will accept a campaign brief and return structured campaign JSON.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=120&section=footer&color=0:7C3AED,55:2563EB,100:0F172A" alt="Footer wave" />

**WebCut.ai CreativeOps Agent Platform**  
**AWS native. Agentic. Full stack. Production shaped. Portfolio ready.**

</div>
