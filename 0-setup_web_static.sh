#!/usr/bin/env bash
# Preparing my web servers - for web_static deployment
sudo apt-get update
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
sudo service nginx restart
