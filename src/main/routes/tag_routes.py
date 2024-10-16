from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=["POST"])
def create_tags():
    http_request = HttpRequest(body = request.json)
    return jsonify({ "resp": "ok"}), 200