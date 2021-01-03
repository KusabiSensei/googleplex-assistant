import logging
import os
import secrets
import string

logger = logging.getLogger("configuration __init__")
logger.setLevel(logging.DEBUG)

if os.getenv('GOOGLEPLEX_TOKEN') is not None:
    token = os.getenv('GOOGLEPLEX_TOKEN')
else:
    token = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(16))

if os.getenv('GOOGLEPLEX_CREDENTIALS') is not None:
    credentials = os.getenv('GOOGLEPLEX_CREDENTIALS')
else:
    credentials = None