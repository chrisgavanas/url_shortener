from flask import Blueprint, request, jsonify

from provider import Provider
from exceptions import InvalidUsage

api = Blueprint('api', __name__)


@api.route('/shortlinks', methods=['POST'])
def create_shortlink():
    return Provider(request).shorten()


@api.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


