from datetime import UTC, datetime

from .extensions import db


class Destination(db.Model):
    __tablename__ = "destinations"

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True, nullable=False, index=True)
    city = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(80), nullable=False, index=True)
    summary = db.Column(db.String(240), nullable=False)
    duration_days = db.Column(db.Integer, nullable=False)
    price_from = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(160), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "slug": self.slug,
            "city": self.city,
            "country": self.country,
            "summary": self.summary,
            "durationDays": self.duration_days,
            "priceFrom": self.price_from,
            "rating": self.rating,
            "image": self.image,
        }


class ContactMessage(db.Model):
    __tablename__ = "contact_messages"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(254), nullable=False, index=True)
    subject = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(UTC),
    )

