# Rasberry Pi Client Scripts
scripts running on raspberry pi

### UpdateCoypos.sh - a script for updating coypos-ui from the official repository
### rfid_write.py - a test script for writing information to a card
### rfid_read.py - a script used to read the UID from an RFID card and push it to the frontend

## Install required packages for rfid

```sh
sudo apt install python3 python3-dev python3-pip 
sudo pip3 install mfrc522 RPi.GPIO
sudo pip3 install pi-rc522
```
## Insstall required packages for Coypos-ui
```sh
sudo apt install docker.io
sudo apt install docker-compose
cd /home/pi
git clone https://github.com/coypos/coypos-ui
```

## Autostart browser and script in rasberry pi:

### edit autostart file:
```sh
sudo nano ~/.config/lxsession/LXDE-pi/autostart
```
### add two lines to end of file:
```sh
@chromium-browser --start-fullscreen --start-maximized http://localhost:8080/
sudo python3 /home/pi/Desktop/rfid_read.py &
```
