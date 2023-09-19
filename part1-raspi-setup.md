# Part 1: Getting your Raspberry Pi (rpi) Setup

Time Allotment:
- 1hr to order parts (if you don't have it). Estimate ~$200 USD.
- 1hr-3hr to execute (depending on skill level and snags)

![rpi-bare-front-view.jpeg](/images/rpi-bare-front-view.jpeg)

![full-kit-hardware](/images/rpi-finished-seperate-top-view.jpeg)

## Full Kit Equipment
1. Micro SD card 8Gb+ & Adapter, [Recommend: Amazon 32gb card ~$15](https://www.amazon.com/s?k=micro+sd+card&rh=n%3A516866%2Cp_n_feature_two_browse-bin%3A6518304011&crid=YXIYMGJA97E7&nav_sdd=aps&rnid=6518301011&sprefix=micro+sd+card&ref=nb_sb_ss_w_sbl-tr-t1_micro-sd-card_k0_1_13_2)
    - See rpi docs for sd cards [here](https://www.raspberrypi.com/documentation/computers/getting-started.html#sd-cards-for-raspberry-pi)
    - Check your computer for an SD Flash Drive slot (else you'll need to buy an external usb [loader](https://www.amazon.com/Reader-uni-Adapter-Aluminum-Memory/dp/B08P1T8R46/ref=sr_1_2?crid=2DL6CI2GH2MEM&keywords=sd%2Bcard%2Bexternal%2Bloader&qid=1694879165&sprefix=sd%2Bcard%2Bexternal%2Bloade%2Caps%2C121&sr=8-2&th=1)).
2. Raspberry Pi 3b+ or 4 (tutorial is on a 3b+), [Pi Shop](https://www.raspberrypi.com/products/), [Recommend: Amazon Pi 4 ~$70](https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TC2BK1X/ref=sr_1_3?crid=3KZWTBP69R65N&keywords=raspberry%2Bpi&qid=1694884282&sprefix=raspberry%2Bpi%2Caps%2C138&sr=8-3&ufe=app_do%3Aamzn1.fos.18ed3cb5-28d5-4975-8bc7-93deae8f9840&th=1)
    - I would probably go with a Pi 4 and 4-to-8GB RAM. The 4s also seem like they are in stock, 3b+ have been sold out.
    - You might need a [1ft USB cord](https://www.amazon.com/s?k=ethernet+cord+1ft&i=computers&rh=n%3A172463%2Cp_n_feature_ten_browse-bin%3A23555330011&dc&ds=v1%3AIBQGTMGU7%2BnNpwAG01LyZDeAYOOPSm0prjnrjrhh%2ByM&crid=1Z6K45XA6F1R4&qid=1694885121&rnid=23555276011&sprefix=ethernet+cord+1f%2Ccomputers%2C124&ref=sr_nr_p_n_feature_ten_browse-bin_2) if the rpi is close to your router, recommend hard line connection, though wifi is okay too 
4. External Solid State Drive (SSD) memory, [Recommend: Amazon SATA SSD 1Tb ~$80](https://www.amazon.com/Crucial-MX500-NAND-SATA-Internal/dp/B078211KBB/ref=d_pd_sim_sccl_4_1/147-8461889-8258503?pd_rd_w=58YeQ&content-id=amzn1.sym.2351c4aa-bb60-45da-95b0-d52caf1c26f1&pf_rd_p=2351c4aa-bb60-45da-95b0-d52caf1c26f1&pf_rd_r=PJW12MM5M27HTY3TJ7VH&pd_rd_wg=FyYif&pd_rd_r=46296c39-6582-4147-9883-869c83e46687&pd_rd_i=B078211KBB&th=1)
5. SSD Case & Cord, [Recommend: Amazon ORICO 2.5'' External Hard Drive Enclosure ~$7](https://www.amazon.com/ORICO-External-Enclosure-Support-Tool-Free/dp/B01LY97QE8/ref=d_pd_sim_sccl_4_26/147-8461889-8258503?pd_rd_w=v30UK&content-id=amzn1.sym.2351c4aa-bb60-45da-95b0-d52caf1c26f1&pf_rd_p=2351c4aa-bb60-45da-95b0-d52caf1c26f1&pf_rd_r=CR5YJYDZ5K5ZMD98S98P&pd_rd_wg=t811H&pd_rd_r=b3838bb0-cdd9-45fa-81ff-c03d3fbba4cb&pd_rd_i=B01LY97QE8&th=1)
6. Raspberry Pi Power Cord, [Pi 4 Shop recommended ~$8](https://www.raspberrypi.com/products/type-c-power-supply/)
    - Be careful! The Pi 3b+ has a different power cord than the Pi 4! The Pi 4 requires more power.
    - However, the Pi 4 power has a USB-C that can be used on the 3b+, I use it and works fine.
7. Raspberry Pi Case, [Recommend Amazon Flirc metal case](https://www.amazon.com/Flirc-Raspberry-Case-Gen2-Model/dp/B07349HT26/ref=sr_1_15?crid=355HS8YRL4UE8&keywords=raspberry%2Bpi%2Bcase%2Bmetal&qid=1694885842&s=pc&sprefix=raspberry%2Bpi%2Bcase%2Bmetal%2Ccomputers%2C124&sr=1-15&th=1)
    - Just make sure the case is a good heat sink, has a fan, or airflow.


## Setup & Configuration


### SD Card Flashing Setup
This part covers "flashing" (writing) the SD Card with the Operating System (OS) into firmware memory.

Download the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) (I used macbook pro which has an SD Flash drive).

You could follow the [Raspberry Pi Documentation: Installing the Operating System](https://www.raspberrypi.com/documentation/computers/getting-started.html#installing-the-operating-system), however I found watching the following youtube video much more helpful and easier:

[Youtube: Headless Raspberry Pi Zero Setup](https://youtu.be/wQJqwGVNHTM?si=GzJZh4_am2cLS1gL)

- Choose Raspberry Pi OS Lite 32bit
- Choose SD Card to write to
- Bottom right click gear for advanced settings options
- Rename raspberrypi (used "headless")
- Ssh enable with password
    - Select password auth. Use custom password (to be used to get in via ssh later as 2 factor authentication)
- Update username (used "pi")
- Enable it to connec to the wifi
    - Note SSID is "wifi name"

### Hardware Assembly & Checking Pi IP Address
Assembly the rpi and connect it to your router.

**⚠️ WARNING: For external SSD USB storage, do not plug it in yet, it freezes your pi on power up. Setup for this is later.**
- Put the pi in the case
- Put the micro SD card in in rpi
- Connect it to power
- Connect it to your Internet Router hardlined via ethernet connection (easier to troubleshoot, can do wifi later)
- Put the SSD Drive into the case, but do not connect it to the rpi yet!
- Pi takes about 5 minutes to boot up. Wait 5 minutes before trying to ssh in.

### Getting into your rpi
Now this part can be daunting, but let's dive in.
- Open terminal (use your mac or windows search, type in terminal)
    - Unfamilar? Youtube "command line terminal tutorial <your_operating_system_here>" (e.g. command line terminal tutorial macos) 

Secure shell into the rpi, if setup correctly this should work.
```bash
ssh pi@headless.local
```
- if there were failed attempts, in terminal:
    - cd //to home folder (directory)
    - cd .ssh //directories with a dot in front are hidden
    - nano known_hosts //to check ssh connections
    - (need to troubleshoot further...)
    - ssh? [Article: What is SSH?](https://www.makeuseof.com/what-is-ssh/)

Update the pi packages
```bash
sudo apt-get update  
```

Upgrade the pi with updates
```bash
sudo apt-get upgrade 
```

This is where most of the configuration is done for the rpi. Feel free to explore it.
```bash
sudo raspi-config
```

### External Hardware Mounting
This is to allow the external SSD drive memory to be attached and not freeze the rpi. This does not come default in Lite.

For external storage configuration, we'll need to follow the rpi documentation: 

https://www.raspberrypi.com/documentation/computers/configuration.html#external-storage-configuration

Follow the directions for the following sections:
- Mounting
- Auto Mounting
- Unmounting

Note, my external storage looked like the following:

From running 

```bash
sudo lsblk -o UUID,NAME,FSTYPE,SIZE,MOUNTPOINT,LABEL,MODEL
```

My storage was the following:
- 67E3-17ED //external storage partition ID
- vfat      //type of storage

This is what my line looks like in the `sudo nano /etc/fstab` file.

`UUID=67E3-17ED /mnt/mydisk vfat defaults,auto,users,rw,nofail 0 0`





