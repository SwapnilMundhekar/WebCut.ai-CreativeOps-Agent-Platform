# WebCut.ai CreativeOps Agent Platform

WebCut.ai is an AI creative operations, media intelligence and automation platform for modern content teams.
It combines design workspace foundations, AI media enhancement, human approval, governance and future agent orchestration in one production style full stack project.

## Part 1 status

This repository now contains the first working development foundation:

| Area | Included in Part 1 |
| --- | --- |
| Web app | Next.js App Router landing page and product modules |
| Studio shell | Browser studio placeholder for future editor workflows |
| AI Lab | Placeholder for text to speech, speech to text, enhancement and generation workflows |
| API Lab | Health check and creative brief endpoint |
| MCP surface | Placeholder for future Model Context Protocol tools |
| Governance | Human approval and audit trail concepts in UI copy |

## Local setup

Run these commands from the repository root:

```cmd
npm install
npm run dev
```

Open:

```text
http://localhost:3000
```

Health check:

```cmd
curl http://localhost:3000/api/health
```

Creative brief test:

```cmd
curl -X POST http://localhost:3000/api/ai/creative-brief -H "Content-Type: application/json" -d "{\"brand\":\"WebCut.ai\",\"goal\":\"Create an AI media enhancement campaign\",\"audience\":\"content creators\"}"
```

## Development roadmap

1. Part 1: Foundation, routes, design system and mock API endpoints.
2. Part 2: Real creative workspace with canvas, uploads and asset library.
3. Part 3: AI media intelligence API layer for text to speech, speech to text, video denoising, sharpening, 4K enhancement and image enhancement.
4. Part 4: Agent orchestration with adapters for LangChain, LangGraph, Model Context Protocol, LlamaIndex, CrewAI, AutoGen, Semantic Kernel, DSPy, LiteLLM, Ollama and vLLM.
5. Part 5: AWS native production architecture with storage, queues, approvals, observability, governance and deployment workflows.
