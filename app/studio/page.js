import Link from "next/link";

export default function StudioPage() {
  return (
    <main className="page-shell compact">
      <Link href="/" className="back-link">← Back to home</Link>
      <section className="workspace">
        <div className="workspace-sidebar">
          <p className="eyebrow">Browser Studio</p>
          <h1>Creative workspace shell</h1>
          <p className="muted">This is the first UI shell for future canvas editing, templates, brand kits, uploads and generated media layers.</p>
          <button className="primary-button button-reset">Generate concept</button>
        </div>
        <div className="canvas-shell">
          <div className="canvas-frame">
            <span>1080 × 1080</span>
            <h2>AI campaign visual</h2>
            <p>Drop assets, prompts and brand rules here in Part 2.</p>
          </div>
        </div>
      </section>
    </main>
  );
}
