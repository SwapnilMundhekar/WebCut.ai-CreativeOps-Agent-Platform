export async function POST(request) {
  let payload = {};

  try {
    payload = await request.json();
  } catch (error) {
    return Response.json({ error: "Invalid JSON body" }, { status: 400 });
  }

  const brand = payload.brand || "WebCut.ai";
  const goal = payload.goal || "Launch a creative campaign";
  const audience = payload.audience || "digital creators and marketing teams";

  return Response.json({
    brand,
    goal,
    audience,
    status: "mock-generated",
    creativeBrief: {
      headline: `${brand} turns raw media into campaign ready creative intelligence`,
      concept: `Create a premium futuristic campaign for ${audience} focused on ${goal}.`,
      channels: ["website hero", "social video", "short form ad", "email banner"],
      aiWorkflows: [
        "brand safe prompt generation",
        "speech to text asset understanding",
        "video denoising and sharpening",
        "human approval before publish"
      ],
      governance: "Human approval required before export or publication."
    }
  });
}
