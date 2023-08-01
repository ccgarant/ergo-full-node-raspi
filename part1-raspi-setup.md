# Getting Started: Raspberry Pi Headless Setup for Running an Ergo Full Node

A quick tutorial on how to setup a raspberry pi (raspi, or raspberrypi) to be headless (that is remote into pi,
pi does not have a monitor or mouse plugged in). This is geared toward beginners who want to learn and hopefully get more Ergo nodes running.

# Part 1: Getting your Pi Setup
Time Allotment:
- 1hr to order parts (if you don't have it)
- 1hr-3hr to execute (depending on skill level and snags)

## Full Kit Equipment
- Macro holder and mini SD card
- Computer check for SD Flash Drive (else you'll need to buy a preloaded SD card)

## Setup & Configuration

ifconfig //see all the devices on your internet. find the rasp pi IP address
ping <ip_number> //or ping raspberrypi.local to see if the connection works

## Flashing Setup

https://www.raspberrypi.com/documentation/computers/getting-started.html#installing-the-operating-system
Raspberry Pi Imager (I used macbook pro which has an SD Flash drive)
Note: For external SSD USB storage, do not plug it in yet, it freezes your pi. Setup for this is later.
Follow this youtube video I found helpful:
- Video notes...

## Getting into your Pi
- bring

- flashing drive with rasp
    - rename raspberrypi (used "headless")
    - ssh enable with password
    - update username (used "pi")
    - use custom password
    - enable it to connecto to wifi

- ssh pi@headless.local //if there were failed attempts, cd / cd .ssh / nano known_hosts / ctrl+k on raspi lines
- sudo apt-get update  //update the pi packages
- sudo apt-get upgrade //upgrade the pi
- sudo raspi-config

## Raspi Configuration Setup
sudo raspi-config

### External Hardware Mounting
echo program_usb_boot_mode=1 | sudo tee -a /boot/config.txt

from: https://www.raspberrypi.com/documentation/computers/configuration.html#external-storage-configuration
sudo lsblk -o UUID,NAME,FSTYPE,SIZE,MOUNTPOINT,LABEL,MODEL
follow steps here
Mounting
Setting up Auto Mounting
Unmounting

//Notes

67E3-17ED
vfat
UUID=5C24-1453 /mnt/mydisk vfat defaults,auto,users,rw,nofail 0 0





