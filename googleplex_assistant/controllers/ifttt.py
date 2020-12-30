from flask import (Blueprint, request)
import logging

bp = Blueprint('ifttt', __name__, url_prefix='/ifttt')
logger = logging.getLogger(__name__)


@bp.route('/command', methods=["POST"])
def accept_command():
    logger.warning(request)
