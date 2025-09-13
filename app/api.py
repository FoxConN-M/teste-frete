from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from .models import QuoteRequest
from .services import get_quotes, to_serializable

bp = Blueprint("api", __name__)

@bp.route("/")
def health():
    return jsonify({"status": "ok"}), 200

@bp.route("/shipping/quotes", methods=["POST"])
def create_shipping_quotes():
    try:
        payload = request.get_json(force=True, silent=False)
        req = QuoteRequest.model_validate(payload)
    except ValidationError as e:
        return jsonify({"eror": "Invalid payload", "details": e.errors}), 422
    except Exception:
        return jsonify({"error": "Malformed JSON"}), 400
    
    quotes = get_quotes(req)
    return jsonify([to_serializable(q) for q in quotes]), 200
