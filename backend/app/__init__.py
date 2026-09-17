import os

from flask import Flask, jsonify
from flask_cors import CORS

from .config import Config
from .extensions import db
from .routes import api
from .seed import seed_destinations


def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    CORS(
        app,
        resources={r"/api/*": {"origins": os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")}},
    )
    app.register_blueprint(api)

    @app.after_request
    def add_security_headers(response):
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Content-Security-Policy"] = "default-src 'none'; frame-ancestors 'none'"
        return response

    @app.errorhandler(404)
    def not_found(_error):
        return jsonify(error="not_found"), 404

    with app.app_context():
        db.create_all()
        seed_destinations()

    return app

