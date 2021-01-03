from flask import (Blueprint, request)
from googleplex_assistant.config import credentials, token
from . import request_rejected
import logging

bp = Blueprint('ifttt', __name__, url_prefix='/ifttt')
logger = logging.getLogger(__name__)


@bp.route('/command', methods=["POST"])
def accept_command():
    if request.headers.get("x-googleplex-authentication", type=str) != token and \
            request.headers.get("Authorization") != credentials:
        return request_rejected()
    logger.warning(request.get_json())
    return {"status": "successful"}
