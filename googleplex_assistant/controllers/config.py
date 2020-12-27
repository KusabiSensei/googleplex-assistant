from flask import Blueprint
from googleplex_assistant.helpers import upnpclient

bp = Blueprint('config', __name__, url_prefix='/config')


@bp.route('/')
def dump_config():
    external_ip_config = upnpclient.map_port()
    return {'external_ip_configuration': external_ip_config}
