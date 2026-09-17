import { FormEvent, useEffect, useState } from "react";

import { getDestinations } from "./api";
import { DestinationCard } from "./components/DestinationCard";
import type { Destination } from "./types/destination";


export default function App() {
  const [draftQuery, setDraftQuery] = useState("");
  const [query, setQuery] = useState("");
  const [destinations, setDestinations] = useState<Destination[]>([]);
  const [status, setStatus] = useState<"loading" | "ready" | "error">("loading");

  useEffect(() => {
    const controller = new AbortController();
    setStatus("loading");
    getDestinations(query, controller.signal)
      .then(({ data }) => {
        setDestinations(data);
        setStatus("ready");
      })
      .catch((error: unknown) => {
        if (error instanceof DOMException && error.name === "AbortError") return;
        setStatus("error");
      });
    return () => controller.abort();
  }, [query]);

  function search(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setQuery(draftQuery);
  }

  return (
    <>
      <header className="site-header">
        <a className="brand" href="#top" aria-label="Wilmington Travel Agency home">
          <span className="brand__mark" aria-hidden="true">W</span>
          <span>Wilmington Travel</span>
        </a>
        <nav aria-label="Primary navigation">
          <a href="#destinations">Destinations</a>
          <a href="#about">Our approach</a>
          <a className="nav-action" href="mailto:hello@example.com">Plan a trip</a>
        </nav>
      </header>

      <main id="main-content">
        <section className="hero" id="top">
          <div className="hero__content">
            <p className="eyebrow">Curated journeys · Thoughtful details</p>
            <h1>Travel beyond the itinerary.</h1>
            <p className="hero__lede">
              Find memorable city breaks built around culture, food and the moments you did not plan.
            </p>
            <form className="search" role="search" onSubmit={search}>
              <label className="sr-only" htmlFor="destination-search">Search destinations</label>
              <input
                id="destination-search"
                value={draftQuery}
                onChange={(event) => setDraftQuery(event.target.value)}
                placeholder="Try Berlin, Sydney or Spain"
                maxLength={80}
              />
              <button type="submit">Search</button>
            </form>
          </div>
        </section>

        <section className="section" id="destinations" aria-labelledby="destinations-heading">
          <div className="section__heading">
            <div>
              <p className="eyebrow">Featured destinations</p>
              <h2 id="destinations-heading">Choose your next story</h2>
            </div>
            {status === "ready" && <p aria-live="polite">{destinations.length} trips found</p>}
          </div>

          {status === "loading" && <p className="state-message" role="status">Loading destinations…</p>}
          {status === "error" && <p className="state-message state-message--error" role="alert">We could not load trips. Please try again.</p>}
          {status === "ready" && destinations.length === 0 && <p className="state-message">No destinations match that search.</p>}
          <div className="destination-grid">
            {destinations.map((destination) => (
              <DestinationCard destination={destination} key={destination.id} />
            ))}
          </div>
        </section>

        <section className="story" id="about">
          <div>
            <p className="eyebrow">The Wilmington approach</p>
            <h2>Less rushing. More discovering.</h2>
          </div>
          <p>
            We pair focused itineraries with room to wander. Every trip balances iconic places,
            neighborhood favorites and practical planning support.
          </p>
        </section>
      </main>

      <footer>
        <p>Wilmington Travel Agency</p>
        <p>Modernized from a 2024 computer science capstone.</p>
      </footer>
    </>
  );
}

