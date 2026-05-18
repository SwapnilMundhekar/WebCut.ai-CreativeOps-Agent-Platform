import Link from "next/link";

const labs = [
  "Text to speech campaign voiceovers",
  "Speech to text transcript intelligence",
  "Video denoising and sharpening",
  "4K enhancement and image restoration",
  "Brand safe generative creative briefs",
];

export default function AiLabPage() {
  return (
    <main className="page-shell compact">
      <Link href="/" className="back-link">← Back to home</Link>
      <p className="eyebrow">AI Lab</p>
      <h1>Media intelligence experiments</h1>
      <div className="card-grid">
        {labs.map((lab) => (
          <article className="feature-card" key={lab}>
            <span className="card-icon">✦</span>
            <h3>{lab}</h3>
            <p>Part 1 placeholder prepared for real model integration in later development parts.</p>
          </article>
        ))}
      </div>
    </main>
  );
}
