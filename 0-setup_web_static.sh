#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

sudo apt-get -y update;
sudo apt-get -y install nginx;

sudo mkdir -p "/data/web_static/releases/test/"
sudo mkdir -p "/data/web_static/shared/"

fake_file="/data/web_static/releases/test/index.html"
[[ -f "$fake_file" ]] || sudo touch "$fake_file"
echo "<h1>Testing</h1>" | sudo tee "$fake_file" > /dev/null

ln -sfT "/data/web_static/releases/test/" "/data/web_static/current"

sudo chown -R ubuntu:ubuntu /data/

cfg="\
server {
	listen 80 default_server;
	add_header X-Served-By \$hostname;
	listen [::]:80 default_server;
	server_name husam.tech;

	location /hbnb_static {
		alias /data/web_static/current/;
	}
}
"

echo "$cfg" | sudo tee "/etc/nginx/sites-available/default" > /dev/null;

sudo service nginx restart;
