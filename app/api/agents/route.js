import { agentStack } from "@/lib/platformData";

export async function GET() {
  return Response.json({
    platform: "WebCut.ai",
    agents: agentStack,
    note: "Part 1 exposes the agent map only. Real orchestration arrives in later parts."
  });
}
