#!/usr/bin/env bash
# Preparing my web servers - for web_static deployment
sudo apt-get update
sudo apt-get install nginx -y
suod mkdir -p /data/web_static/shared /data/web_static/releases/test
echo "This is a sample html file" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -Rh ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
