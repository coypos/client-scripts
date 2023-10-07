cd /home/pi/coypos-ui
sudo git push
sudo git pull
sudo docker stop coypos-ui 
sudo docker rm coypos-ui
sudo docker image prune -af 
sudo docker build --no-cache -t=coypos-ui .
sudo docker run -p 8080:8080 --name coypos-ui -dit --restart always coypos-ui 