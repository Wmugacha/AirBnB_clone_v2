#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

if ! [ -x "$(command -v nginx)" ]; then
  # Nginx is not installed
  echo "Nginx is not installed. Installing now..."
  sudo apt-get update

  sudo apt-get install nginx -y
else
  # Nginx is installed
  echo "Nginx is already installed."
fi

#create folders
if [ ! -d "./data" ]
then
    mkdir ./data
fi

if [ ! -d "./data/web_static/" ]
then
    mkdir ./data/web_static/
fi

if [ ! -d "./data/web_static/releases/" ]
then
    mkdir ./data/web_static/releases/
fi

if [ ! -d "./data/web_static/shared/" ]
then
    mkdir ./data/web_static/shared/
fi

if [ ! -d "./data/web_static/releases/test/" ]
then
    mkdir ./data/web_static/releases/test/
fi

#creating a dummy html page
echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee ./data/web_static/releases/test/index.html

# Create a symbolic link and it should be recreated everytime script is run
ln -snf ./data/web_static/releases/test/ ./data/web_static/current

# Transfer ownership of /data/ to Ubuntu user and Group
sudo chown -R ubuntu:ubuntu ./data/

#setting up the page to be served
sudo sed -i '/server_name _;/a \ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-available/default

#restart the server
sudo service nginx restart
