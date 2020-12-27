from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    from googleplex_assistant.controllers import hello, config
    app.register_blueprint(hello.bp)
    app.register_blueprint(config.bp)

    from googleplex_assistant.helpers import upnpclient
    upnpclient.init_app()
    return app
