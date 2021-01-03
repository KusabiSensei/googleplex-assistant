from flask import Flask
from googleplex_assistant.config import token
from logging.config import dictConfig


def create_app():
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'DEBUG',
            'handlers': ['wsgi']
        }
    })
    app = Flask(__name__, instance_relative_config=True)
    app.logger.debug("Parsing configuration...")

    app.logger.info("The token to include is")
    app.logger.info(token)
    from googleplex_assistant.controllers import hello, config, ifttt, dialogflow
    app.register_blueprint(hello.bp)
    app.register_blueprint(config.bp)
    app.register_blueprint(ifttt.bp)
    app.register_blueprint(dialogflow.bp)

    from googleplex_assistant.helpers import upnpclient
    upnpclient.init_app()
    upnpclient.map_port()

    return app


application = create_app()
