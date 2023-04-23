#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

if ! [ -x "$(command -v nginx)" ]; then
# Nginx is not installed
echo "Nginx is not installed. Installing now..."
sudo apt-get update

sudo apt-get install nginx -y

sudo ufw allow 'Nginx HTTP'
else
  # Nginx is installed
  echo "Nginx is already installed."
fi

#create folders
sudo mkdir -p /data/

sudo mkdir -p /data/web_static/

sudo mkdir -p /data/web_static/releases/

sudo mkdir -p /data/web_static/shared/

sudo mkdir -p /data/web_static/releases/test/

sudo touch /data/web_static/releases/test/index.html

#creating a dummy html page
sudo echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link and it should be recreated everytime script is run
sudo rm -f /data/web_static/current

sudo ln -snf /data/web_static/releases/test/ /data/web_static/current

# Transfer ownership of /data/ to Ubuntu user and Group
sudo chown -R ubuntu:ubuntu /data/

#setting up the page to be served
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo sed -i '/server_name _;/a \ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-available/default

#restart the server
sudo service nginx restart
