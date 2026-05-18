import Link from "next/link";

const metrics = [
  { label: "Creative jobs", value: "128" },
  { label: "Human approvals", value: "14" },
  { label: "Enhanced assets", value: "342" },
  { label: "Policy checks", value: "98%" },
];

export default function DashboardPage() {
  return (
    <main className="page-shell compact">
      <Link href="/" className="back-link">← Back to home</Link>
      <p className="eyebrow">Operations Dashboard</p>
      <h1>Creative intelligence overview</h1>
      <div className="metric-grid">
        {metrics.map((metric) => (
          <div className="metric-card" key={metric.label}>
            <span>{metric.label}</span>
            <strong>{metric.value}</strong>
          </div>
        ))}
      </div>
    </main>
  );
}
