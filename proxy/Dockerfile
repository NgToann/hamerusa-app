FROM nginxinc/nginx-unprivileged:1-alpine
LABEL maintainer="ngtoann"

# COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh
# COPY ./default.conf /etc/nginx/default.conf
COPY ./hamerusavn.crt /etc/nginx/hamerusavn.crt
COPY ./hamerusavn.key /etc/nginx/hamerusavn.key

ADD ./hamerusavn.conf /etc/nginx/conf.d/

ENV LISTEN_PORT=8000
ENV APP_HOST=app
ENV APP_PORT=8000

USER root

RUN mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

VOLUME /vol/static

USER nginx

# CMD ["/run.sh"]