#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

sudo apt-get -y update;
sudo apt-get -y install nginx;
sudo ufw allow 'Nginx HTTP';
sudo sh -c 'echo "Hello World!" > /var/www/html/index.nginx-debian.html';
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
file="/data/web_static/releases/test/index.html"
[[ -f "$file" ]] || touch "$file"
ln -s "/data/web_static/current" "/data/web_static/releases/test/"
chown ubuntu:ubuntu "/data/"

sudo service nginx start;
