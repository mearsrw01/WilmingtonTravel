import type { DestinationResponse } from "./types/destination";


export async function getDestinations(query = "", signal?: AbortSignal) {
  const parameters = new URLSearchParams();
  if (query.trim()) parameters.set("q", query.trim());
  const suffix = parameters.size ? `?${parameters.toString()}` : "";
  const response = await fetch(`/api/destinations${suffix}`, { signal });
  if (!response.ok) throw new Error("Unable to load destinations.");
  return (await response.json()) as DestinationResponse;
}

