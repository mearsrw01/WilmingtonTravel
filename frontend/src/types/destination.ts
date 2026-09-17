export interface Destination {
  id: number;
  slug: string;
  city: string;
  country: string;
  summary: string;
  durationDays: number;
  priceFrom: number;
  rating: number;
  image: string;
}

export interface DestinationResponse {
  data: Destination[];
}

