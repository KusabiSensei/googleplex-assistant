from googleplex_assistant import application

if __name__ == '__main__':
    application.run(ssl_context=('app.cer', 'app.key'))
