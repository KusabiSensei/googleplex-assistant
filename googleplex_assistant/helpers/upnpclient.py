from googleplex_assistant.helpers import upnp_client
import logging
import atexit

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def init_app():
    """
    Initialize the application by adding in the shutdown call hook.
    """
    atexit.register(shutdown_handler)


def map_port(port=40000):
    """
    This will attempt to map the given port out via uPNP. Maybe it will work, maybe it won't.
    :param port: The external port to attempt to map. Defaults to 40000
    :return: A dictionary with the external IP and port, amongst other values, to give you the URI to be able to pass to IFTTT
    """
    local_ip = upnp_client.lanaddr
    external_ip = upnp_client.externalipaddress()
    existing_mapping = upnp_client.getspecificportmapping(port, 'TCP')
    if existing_mapping != None:
        raise RuntimeError('The selected port is being held by another mapping')
    logger.warning("Now attempting to map the port")
    bool_addport = upnp_client.addportmapping(port, 'TCP', local_ip, port, 'IFTTT Handler', '')
    if bool_addport:
        logger.warning("Port mapped.")
    else:
        raise RuntimeError("Port mapping failed. The application should be restarted.")
    return {'lan_ip': local_ip,
            'lan_port': port,
            'external_ip': external_ip,
            'port': port}


def shutdown_handler():
    """
    This is a bit heavyhanded of a way to unmap the port at server shutdown, but eh, I'm not worried about it.
    Mainly because there are two threads, therefore this will get called twice, and since the unmapping doesn't work
    the second time around, it will throw an Exception of some class, but we no-op our way right past it on our way
    out the door.
    """
    logger.critical("Stopping the server now! Unmapping the port first!")
    try:
        unmap_port()
    except Exception:
        pass


def unmap_port(port=40000):
    """
    This will be called as part of the cleanup during application context teardown to release the port mapping.
    :param port: The external port to attempt to release. Defaults to 40000
    :return: Probably nothing, but we'll see
    """
    bool_result = upnp_client.deleteportmapping(port, 'TCP')
    if bool_result:
        logger.warning("Removed the port mapping")
    else:
        logger.critical("Failed to remove the port mapping")
