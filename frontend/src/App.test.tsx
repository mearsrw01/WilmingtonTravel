import { render, screen, waitFor } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";

import App from "./App";


const destinationResponse = {
  data: [
    {
      id: 1,
      slug: "berlin-germany",
      city: "Berlin",
      country: "Germany",
      summary: "Historic landmarks and unforgettable food.",
      durationDays: 4,
      priceFrom: 157,
      rating: 4.7,
      image: "/images/germany.jpg",
    },
  ],
};


describe("App", () => {
  afterEach(() => vi.restoreAllMocks());

  it("renders destinations returned by the API", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn().mockResolvedValue({ ok: true, json: async () => destinationResponse }),
    );

    render(<App />);

    await waitFor(() => expect(screen.getByRole("heading", { name: "Berlin" })).toBeVisible());
    expect(screen.getByText("Germany")).toBeVisible();
  });

  it("renders a recoverable API error state", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue({ ok: false }));
    render(<App />);
    expect(await screen.findByRole("alert")).toHaveTextContent("could not load trips");
  });
});

