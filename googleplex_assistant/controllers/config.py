from flask import Blueprint, request
from googleplex_assistant.helpers import upnpclient
from googleplex_assistant.config import token, credentials
from . import request_rejected

bp = Blueprint('config', __name__, url_prefix='/config')


@bp.route('/')
def dump_config():
    if request.headers.get("x-googleplex-authentication", type=str) != token and \
            request.headers.get("Authorization") != credentials:
        return request_rejected()
    external_ip_config = upnpclient.map_port()
    return {'external_ip_configuration': external_ip_config}


@bp.route('/chromecasts')
def dump_chromecasts():
    if request.headers.get("x-googleplex-authentication", type=str) != token and \
            request.headers.get("Authorization") != credentials:
        return request_rejected()
    return {'chromecasts': 'List of Chromecasts will be here'}
