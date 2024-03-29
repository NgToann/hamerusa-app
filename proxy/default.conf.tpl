server {
    listen ${LISTEN_PORT};
    
    charset utf-8;
    client_max_body_size    50M;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
    }
}