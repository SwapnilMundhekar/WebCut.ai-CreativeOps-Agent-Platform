import Link from "next/link";
import { platformModules, launchSteps, agentStack } from "@/lib/platformData";

export default function HomePage() {
  return (
    <main className="page-shell">
      <section className="hero-grid">
        <div className="hero-copy">
          <p className="eyebrow">Nebula Flux Interface · Part 1 Foundation</p>
          <h1>WebCut.ai CreativeOps Agent Platform</h1>
          <p className="hero-text">
            A futuristic AI creative operations and media intelligence platform for design workflows, media enhancement, human approvals and agentic automation.
          </p>
          <div className="button-row">
            <Link href="/studio" className="primary-button">Open Studio</Link>
            <Link href="/api-lab" className="secondary-button">Test API Lab</Link>
          </div>
        </div>
        <div className="hero-panel">
          <div className="orb orb-one" />
          <div className="orb orb-two" />
          <div className="glass-card">
            <span>Live Architecture</span>
            <strong>Creative agents · media tools · governance</strong>
            <p>Prepared for AWS native workloads, Azure AI placeholders and Model Context Protocol style tool surfaces.</p>
          </div>
        </div>
      </section>

      <section className="section">
        <div className="section-heading">
          <p className="eyebrow">Core Platform Modules</p>
          <h2>One operating layer for AI powered creative work</h2>
        </div>
        <div className="card-grid">
          {platformModules.map((module) => (
            <article className="feature-card" key={module.title}>
              <span className="card-icon">{module.icon}</span>
              <h3>{module.title}</h3>
              <p>{module.description}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="split-section">
        <div>
          <p className="eyebrow">Agent Stack</p>
          <h2>Built for multi agent creative automation</h2>
          <p className="muted">Part 1 adds a clean surface. Later parts will connect real model calls, asset pipelines, approval workflows and observability.</p>
        </div>
        <div className="stack-list">
          {agentStack.map((item) => (
            <div className="stack-item" key={item.name}>
              <strong>{item.name}</strong>
              <span>{item.role}</span>
            </div>
          ))}
        </div>
      </section>

      <section className="section">
        <div className="section-heading">
          <p className="eyebrow">Build Sequence</p>
          <h2>Development path from foundation to production architecture</h2>
        </div>
        <div className="timeline">
          {launchSteps.map((step) => (
            <div className="timeline-item" key={step.phase}>
              <span>{step.phase}</span>
              <div>
                <h3>{step.title}</h3>
                <p>{step.detail}</p>
              </div>
            </div>
          ))}
        </div>
      </section>
    </main>
  );
}
