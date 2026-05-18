export async function GET() {
  return Response.json({
    status: "ok",
    platform: "WebCut.ai CreativeOps Agent Platform",
    phase: "part-1-foundation",
    timestamp: new Date().toISOString(),
    modules: [
      "studio",
      "dashboard",
      "ai-lab",
      "api-lab",
      "mcp-surface"
    ]
  });
}
