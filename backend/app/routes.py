import re

from flask import Blueprint, jsonify, request
from sqlalchemy import or_

from .extensions import db
from .models import ContactMessage, Destination

api = Blueprint("api", __name__, url_prefix="/api")
EMAIL_PATTERN = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")


def clean_text(value, maximum):
    return " ".join(str(value or "").strip().split())[:maximum]


@api.get("/health")
def health():
    return jsonify(status="healthy", version="0.2.0")


@api.get("/destinations")
def destinations():
    query = clean_text(request.args.get("q"), 80)
    statement = db.select(Destination).order_by(Destination.country, Destination.city)
    if query:
        term = f"%{query}%"
        statement = statement.where(
            or_(Destination.city.ilike(term), Destination.country.ilike(term))
        )
    results = db.session.scalars(statement).all()
    return jsonify(data=[destination.to_dict() for destination in results])


@api.post("/contact")
def create_contact_message():
    payload = request.get_json(silent=True) or {}
    fields = {
        "name": clean_text(payload.get("name"), 100),
        "email": clean_text(payload.get("email"), 254).lower(),
        "subject": clean_text(payload.get("subject"), 120),
        "message": clean_text(payload.get("message"), 2000),
    }
    errors = {}
    for field in ("name", "subject", "message"):
        if not fields[field]:
            errors[field] = "This field is required."
    if not EMAIL_PATTERN.fullmatch(fields["email"]):
        errors["email"] = "Enter a valid email address."
    if errors:
        return jsonify(error="validation_error", fields=errors), 400

    contact = ContactMessage(**fields)
    db.session.add(contact)
    db.session.commit()
    return jsonify(id=contact.id, message="Your message has been received."), 201

