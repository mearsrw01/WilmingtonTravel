from .extensions import db
from .models import Destination

DESTINATIONS = [
    {
        "slug": "berlin-germany",
        "city": "Berlin",
        "country": "Germany",
        "summary": "Historic landmarks, creative neighborhoods and unforgettable food.",
        "duration_days": 4,
        "price_from": 157,
        "rating": 4.7,
        "image": "/images/germany.jpg",
    },
    {
        "slug": "sydney-australia",
        "city": "Sydney",
        "country": "Australia",
        "summary": "Harbor views, coastal walks and a vibrant dining scene.",
        "duration_days": 7,
        "price_from": 395,
        "rating": 4.5,
        "image": "/images/australia.jpg",
    },
    {
        "slug": "barcelona-spain",
        "city": "Barcelona",
        "country": "Spain",
        "summary": "Bold architecture, Mediterranean beaches and late-night tapas.",
        "duration_days": 5,
        "price_from": 163,
        "rating": 4.6,
        "image": "/images/spain.jpg",
    },
]


def seed_destinations():
    if db.session.scalar(db.select(db.func.count(Destination.id))):
        return
    db.session.add_all(Destination(**item) for item in DESTINATIONS)
    db.session.commit()

