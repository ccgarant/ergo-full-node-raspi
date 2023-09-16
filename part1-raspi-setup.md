# Part 1: Getting your Pi Setup

Time Allotment:
- 1hr to order parts (if you don't have it)
- 1hr-3hr to execute (depending on skill level and snags)

## Full Kit Equipment
- Micro SD card 8Gb+ & Adapter [Recommend: Amazon SanDisk 32gb](https://www.amazon.com/s?k=micro+sd+card&rh=n%3A516866%2Cp_n_feature_two_browse-bin%3A6518304011&crid=YXIYMGJA97E7&nav_sdd=aps&rnid=6518301011&sprefix=micro+sd+card&ref=nb_sb_ss_w_sbl-tr-t1_micro-sd-card_k0_1_13_2)
    - See rpi docs for sd cards [here](https://www.raspberrypi.com/documentation/computers/getting-started.html#sd-cards-for-raspberry-pi)
    - Check your computer for an SD Flash Drive slot (else you'll need to buy an external usb [loader](https://www.amazon.com/Reader-uni-Adapter-Aluminum-Memory/dp/B08P1T8R46/ref=sr_1_2?crid=2DL6CI2GH2MEM&keywords=sd%2Bcard%2Bexternal%2Bloader&qid=1694879165&sprefix=sd%2Bcard%2Bexternal%2Bloade%2Caps%2C121&sr=8-2&th=1)).
- Raspberry Pi (tutorial is on a 3b+)
    - You might need a 1ft USB cord if the rpi is close to your router, recommend hard line connection, though wifi is okay too 
- External Solid State Drive (SSD) memory (I personnally bought this [SATA SSD 1Tb](https://www.amazon.com/Reader-uni-Adapter-Aluminum-Memory/dp/B08P1T8R46/ref=sr_1_2?crid=2DL6CI2GH2MEM&keywords=sd%2Bcard%2Bexternal%2Bloader&qid=1694879165&sprefix=sd%2Bcard%2Bexternal%2Bloade%2Caps%2C121&sr=8-2&th=1) which is actually ~$80)
    - [SSD Case & Cord](https://www.amazon.com/ORICO-External-Enclosure-Support-Tool-Free/dp/B01LY97QE8/ref=d_pd_sim_sccl_4_26/147-8461889-8258503?pd_rd_w=v30UK&content-id=amzn1.sym.2351c4aa-bb60-45da-95b0-d52caf1c26f1&pf_rd_p=2351c4aa-bb60-45da-95b0-d52caf1c26f1&pf_rd_r=CR5YJYDZ5K5ZMD98S98P&pd_rd_wg=t811H&pd_rd_r=b3838bb0-cdd9-45fa-81ff-c03d3fbba4cb&pd_rd_i=B01LY97QE8&th=1)

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





