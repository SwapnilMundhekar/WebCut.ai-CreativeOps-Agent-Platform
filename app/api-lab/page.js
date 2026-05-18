import Link from "next/link";

export default function ApiLabPage() {
  return (
    <main className="page-shell compact">
      <Link href="/" className="back-link">← Back to home</Link>
      <p className="eyebrow">API Lab</p>
      <h1>Backend route surface</h1>
      <div className="endpoint-list">
        <div>
          <strong>GET /api/health</strong>
          <span>Checks whether the WebCut.ai foundation is running.</span>
        </div>
        <div>
          <strong>POST /api/ai/creative-brief</strong>
          <span>Returns a deterministic mock creative brief for later AI replacement.</span>
        </div>
        <div>
          <strong>GET /api/agents</strong>
          <span>Returns the planned creative agent map.</span>
        </div>
      </div>
    </main>
  );
}
