import "./globals.css";

export const metadata = {
  title: "WebCut.ai CreativeOps Agent Platform",
  description: "AI creative operations, media intelligence and automation platform.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
