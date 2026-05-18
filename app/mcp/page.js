import Link from "next/link";

const tools = [
  "asset.search",
  "media.enhance",
  "brief.generate",
  "approval.request",
  "audit.write",
];

export default function McpPage() {
  return (
    <main className="page-shell compact">
      <Link href="/" className="back-link">← Back to home</Link>
      <p className="eyebrow">MCP Ready Surface</p>
      <h1>Future tool registry</h1>
      <div className="endpoint-list">
        {tools.map((tool) => (
          <div key={tool}>
            <strong>{tool}</strong>
            <span>Placeholder for safe agent tool execution.</span>
          </div>
        ))}
      </div>
    </main>
  );
}
