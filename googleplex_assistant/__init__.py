from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    from googleplex_assistant.controllers import hello, config, ifttt
    app.register_blueprint(hello.bp)
    app.register_blueprint(config.bp)
    app.register_blueprint(ifttt.bp)

    from googleplex_assistant.helpers import upnpclient
    upnpclient.init_app()
    upnpclient.map_port()
    return app


application = create_app()
