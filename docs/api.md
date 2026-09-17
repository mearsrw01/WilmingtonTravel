# API Reference

All API responses use JSON.

## Health

`GET /api/health`

Returns HTTP 200 with service status and application version.

## List destinations

`GET /api/destinations`

Optional query parameter: `q`, a city or country fragment with a maximum processed length of 80 characters.

Successful response:

```json
{
  "data": [
    {
      "id": 1,
      "slug": "berlin-germany",
      "city": "Berlin",
      "country": "Germany",
      "summary": "Historic landmarks, creative neighborhoods and unforgettable food.",
      "durationDays": 4,
      "priceFrom": 157,
      "rating": 4.7,
      "image": "/images/germany.jpg"
    }
  ]
}
```

## Create contact message

`POST /api/contact`

Required JSON fields: `name`, `email`, `subject`, and `message`.

The API trims and bounds text, normalizes the email address and returns field-specific validation errors with HTTP 400. A valid message returns HTTP 201.

