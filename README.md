# Garbage Door Opener - Raspberry Pi
This simple script plays a sound when you open the door. Sorry about the poor quality docs - I'm going to try to document more effectively for future projects. [View the project on YouTube here.](https://www.youtube.com/watch?v=nlJdmeuDWis)


## Getting Started
I like to connect to my raspberry pi with SSH so I can work from my laptop. To install it use:

```bash
sudo apt-get update && sudo apt-get install openssh-server
sudo systemctl enable ssh
sudo service ssh start
```

and then run the following to get the IP.
```bash
ifconfig
```

You should now be able to run the following from your laptop to connect to it.
```bash
ssh pi@{the_ip_address}
# default password is raspberry
```

## Installing requirements
We use a subprocess call to mpg321 in this script, so we need to install it.

```bash
sudo apt-get update && sudo apt-get install -y mpg321
```

## Audio Config
Configuring a raspberry pi to play audio out of the 3.5mm output without an HDMI display connected is not a fun time - so here are a few things that I've needed to get it working out of the box.

```bash
# Configure default output to 3.5mm
sudo amixer cset numid=3 1

# Set volume to high
sudo amixer set PCM -- -100
```

Edit the /etc/rc.local file to run the script on boot. You'll also need to configure auto console login with raspi-config.
```bash
sudo nano /etc/rc.local
```

```bash
python /home/pi/app/opener.py &
```
