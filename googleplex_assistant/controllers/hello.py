from flask import Blueprint, request
from googleplex_assistant.config import token, credentials
from . import request_rejected

bp = Blueprint('hello', __name__, url_prefix='/hello')


@bp.route('/')
def say_hello():
    if request.headers.get("x-googleplex-authentication", type=str) != token and \
            request.headers.get("Authorization") != credentials:
        return request_rejected()
    return {'message': 'Hello World'}
