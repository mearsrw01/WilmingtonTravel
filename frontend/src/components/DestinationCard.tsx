import type { Destination } from "../types/destination";


interface DestinationCardProps {
  destination: Destination;
}


export function DestinationCard({ destination }: DestinationCardProps) {
  return (
    <article className="destination-card">
      <div className="destination-card__image-wrap">
        <img
          className="destination-card__image"
          src={destination.image}
          alt={`${destination.city}, ${destination.country}`}
        />
        <span className="destination-card__price">From ${destination.priceFrom}</span>
      </div>
      <div className="destination-card__body">
        <p className="eyebrow">{destination.country}</p>
        <h3>{destination.city}</h3>
        <p>{destination.summary}</p>
        <dl className="destination-card__facts">
          <div>
            <dt>Duration</dt>
            <dd>{destination.durationDays} days</dd>
          </div>
          <div>
            <dt>Rating</dt>
            <dd>{destination.rating.toFixed(1)} / 5</dd>
          </div>
        </dl>
        <a
          className="text-button"
          href={`mailto:hello@example.com?subject=${encodeURIComponent(`Planning a trip to ${destination.city}`)}`}
        >
          Ask about this trip <span aria-hidden="true">→</span>
        </a>
      </div>
    </article>
  );
}
