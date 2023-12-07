#!/usr/bin/env bash
# Bash script setting up the server for deployment of web_static

# updating system and installing nginx
apt-get update
apt-get -y install nginx

mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

echo "Bring me a Cup" > /data/web_static/releases/test/index.html

# Creating a symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# giving ownership
chown -R ubuntu /data/
chgrp -R ubuntu /data/

# Update the Nginx configuration
printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm index.nginx-debian.html;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 https://www.github.com/Jukunye/;
    }

    error_page 404 /404.html;
    location /404 {
      root /etc/nginx/html;
      internal;
    }

}" > /etc/nginx/sites-available/default

service nginx restart
