export const onRequestGet: PagesFunction = async ({ request }) => {
  const url = new URL(request.url);
  const country = request.headers.get("CF-IPCountry") || "US";
  const TAG_US = "peteywee20";
  const targets: Record<string, string> = {
    US: `https://www.amazon.com/music/unlimited?tag=${encodeURIComponent(TAG_US)}`
    // GB: `https://www.amazon.co.uk/music/unlimited?tag=YOUR_UK_TAG`,
    // DE: `https://www.amazon.de/music/unlimited?tag=YOUR_DE_TAG`,
  };
  const dest = new URL(targets[country] || targets.US);
  for (const [k, v] of url.searchParams) if (k.startsWith("utm_")) dest.searchParams.set(k, v);
  return Response.redirect(dest.toString(), 302);
};
