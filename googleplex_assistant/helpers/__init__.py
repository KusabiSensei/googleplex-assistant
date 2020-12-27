import logging
import miniupnpc

logger = logging.getLogger(__name__)
logger.warning("Now initializing helper objects...")
upnp_client = miniupnpc.UPnP()
devices = upnp_client.discover()
gateway = upnp_client.selectigd()

