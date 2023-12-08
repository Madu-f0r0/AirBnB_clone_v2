#!/usr/bin/env bash
# Initial config of my web servers

#Install Nginx if not installed already
apt-get -y update
apt-get -y install nginx

# Make the following directories if they do not exist
mkdir -p "/data/web_static/releases/test"
mkdir -p "/data/web_static/shared"

# Create fake html file to test Nginx config
echo "my config works well" > "/data/web_static/releases/test/index.html"

# Create symlink of /data/web_static/current to /data/web_static/releases/test/
# Delete and recreate link if already exists
ln -sf "/data/web_static/releases/test/" "/data/web_static/current"

# Change /data/ ownership to ubuntu
chown -R ubuntu:ubuntu "/data/"

# Add location block to Nginx default server block for hbnb_static
if ! grep -q "location /hbnb_static {" "/etc/nginx/sites-available/default";
then
	add_block="server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
	sed -i "s|server_name _;|$add_block|" "/etc/nginx/sites-available/default"
fi

#Reload Nginx
nginx -s reload
