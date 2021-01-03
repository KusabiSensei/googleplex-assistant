import logging
import miniupnpc
from pychromecast import get_chromecasts
from .plex import server as plex_server



def cc_discovery_callback(chromecast):
    chromecasts[chromecast.device.friendly_name] = chromecast


logger = logging.getLogger(__name__)
logger.info("Now initializing helper objects...")
chromecasts = {}
upnp_client = miniupnpc.UPnP()
devices = upnp_client.discover()
gateway = upnp_client.selectigd()
get_chromecasts(blocking=False, callback=cc_discovery_callback)

