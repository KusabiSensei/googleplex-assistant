FROM python:3.9-alpine
LABEL org.opencontainers.image.source=https://github.com/KusabiSensei/googleplex-assistant
WORKDIR /app
ADD Pipfile* /app/
ADD *.py /app/
ADD googleplex_assistant /app/googleplex_assistant/
RUN apk add --no-cache acme.sh miniupnpc bind-tools nginx make gcc musl-dev linux-headers && pip install pipenv && pipenv install --ignore-pipfile && apk del --no-cache make gcc musl-dev linux-headers
ADD nginx/nginx.conf /etc/nginx/nginx.conf
ADD nginx/default.conf /etc/nginx/conf.d/default.conf
#ADD nginx/app.key /app/app.key
#ADD nginx/app.cer /app/app.cer
ADD start_server.sh /app/
CMD ["/app/start_server.sh",""]
