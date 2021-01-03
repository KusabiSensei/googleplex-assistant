from flask import (Blueprint, request, Response)
from googleplex_assistant.config import credentials, token
from . import request_rejected, request_accepted
import logging

bp = Blueprint('dialogflow', __name__, url_prefix='/dialogflow')
logger = logging.getLogger(__name__)


@bp.route('/command', methods=["POST"])
def accept_command():
    logger.debug(request.headers.keys())
    logger.debug("The authorization header is:")
    logger.debug(request.headers.get("x-googleplex-authentication", type=str))
    logger.debug("or alternatively the basic auth header:")
    logger.debug(request.headers.get("Authorization"))
    if request.headers.get("x-googleplex-authentication", type=str) != token and \
            request.headers.get("Authorization") != credentials:
        logger.debug(request.get_json())
        return request_rejected()
    body = request.get_json()
    logger.debug("The body sent is %s", body)

    return request_accepted()


@bp.route('/hello', methods=["POST"])
def say_hello():
    if request.headers.get("x-googleplex-authentication", type=str) != token:
        logger.warning(request.get_json())
        return request_rejected()
    logger.warning("The authorization header is:")
    logger.warning(request.headers.get("x-googleplex-authentication", type=str))
    logger.warning("The body of the request is:")
    logger.warning(request.get_json())
    return request_accepted()
