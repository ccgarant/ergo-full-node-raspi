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


# Setup & Configuration


## SD Card Flashing Setup
This part covers "flashing" (writing) the SD Card with the Operating System (OS) into firmware memory.

Download the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) (I used macbook pro which has an SD Flash drive).

You could follow the [Raspberry Pi Documentation: Installing the Operating System](https://www.raspberrypi.com/documentation/computers/getting-started.html#installing-the-operating-system), however I found watching the following youtube video much more helpful and easier:

[Youtube: Headless Raspberry Pi Zero Setup](https://youtu.be/wQJqwGVNHTM?si=GzJZh4_am2cLS1gL)

- Choose Raspberry Pi OS **Lite** 32bit under "Raspberry Pi OS (other)"
    - 64-bit is faster and is also a good option. Just not tested.
    - Lite for headless (no Desktop GUIs)
- Choose SD Card to write to
- Bottom right click gear for advanced settings options
- Set hostname, rename raspberrypi to **"headless"**
    - you can use your own username but the headless is used in this tutorial
- Yes Enable SSH
- Yes "Use password authentication"
- Fill in username and password to login to the rpi.
- Update username to **"pi"**
- Yes Enable it to connec to the wifi
    - Note SSID is "wifi name"
    - Type in the password
- Save
- Write

The first time takes a few minutes

### Hardware Assembly & Checking Pi IP Address
Assembly the rpi and connect it to your router. Trust me this saves time because you'll check your router for headless.local IP address.

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
Recall `pi` is the username and `headless.local` is the IP address.

> ⚠️ If you get this warning "WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!" Odds are you already have known_hosts ssh keys into the pi. You'll need to delete them and basically start fresh.
>
>cd to home, then cd into the hidden `.ssh` folder
>
>```bash
>cd
>cd .ssh
>```
>
>Next you'll open the known_hosts folder which keeps the username public keys. You'll then delete all the former pi@headless.local logins
>
>```bash
>nano known_hosts
>```
>
>`Ctrl+k` on the lines with headless to wipe them out (nice little trick).
>
>If there are still ssh failed attempts, in terminal:
    - cd //to home folder (directory)
    - cd .ssh //directories with a dot in front are hidden
    - nano known_hosts //to check ssh connections
    - (need to troubleshoot further...)
    - ssh? [Article: What is SSH?](https://www.makeuseof.com/what-is-ssh/)


### Update the pi and config updates

Update & upgrade the pi packages

```bash
sudo apt-get update
sudo apt-get upgrade 
```
This is where most of the configuration is done for the rpi. Feel free to explore it.

```bash
sudo raspi-config
```

## External Hardware Mounting
This is to allow the external SSD drive memory to be attached and not freeze the rpi. This does not come default in Lite.

This is a little involved so prepare yourself for battle!

=====Mounting Hard Drive====

#### Find the external drive device name

**Plug in the SSD External Hard Drive!**

lists all memory disks and partitions. More on [fdisk](https://wiki.archlinux.org/title/Fdisk).

```bash
sudo fdisk -l
```

The SATA SSD external memory here is `Disk /dev/sda: 931.51 GiB`. It is identified as `/dev/sda`.

It is by default listed with two partitions:

    Device      Start        End    Sectors   Size Type
    /dev/sda1      40     409639     409600   200M EFI System
    /dev/sda2  409640 1953525127 1953115488 931.3G Apple APFS

Now we need to delete the partitions and create a new one with a desirable file storage type ext4

#### delete the default partitions

```bash
sudo fdisk /dev/sda
```

You should see "Welcome to fdisk (util-linus <version>)"

Type in `d` to delete the partitions (repeat until they are all gone). 

Hit enter to default select the partition to delete.

#### Create new partition with desired file type

Type in `n` to create a new partition.

Hit enter for default 3 times

You should see "Created a new partition 1 of type 'Linux filesystem' and of size 931.5 GiB."

To check, type in `p` for partition. Mine looks like this:

    Command (m for help): p
    Disk /dev/sda: 931.51 GiB, 1000204886016 bytes, 1953525168 sectors
    Disk model: 500SSD1         
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 4096 bytes
    I/O size (minimum/optimal): 4096 bytes / 4096 bytes
    Disklabel type: gpt
    Disk identifier: A59F918E-3EBE-445F-8E0D-951CD93129C8

    Device     Start        End    Sectors   Size Type
    /dev/sda1   2048 1953525134 1953523087 931.5G Linux filesystem

To confirm, type in `w` to write this to disk.

You should see "The partition table has been altered."

To check:

```bash
sudo fdisk -l
```

My final version looks like this. Note the `dev/sda1` Device name and `Disk identifier` number. We'll need those later:

    Disk /dev/sda: 931.51 GiB, 1000204886016 bytes, 1953525168 sectors
    Disk model: 500SSD1         
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 4096 bytes
    I/O size (minimum/optimal): 4096 bytes / 4096 bytes
    Disklabel type: gpt
    Disk identifier: A59F918E-3EBE-445F-8E0D-951CD93129C8

    Device     Start        End    Sectors   Size Type
    /dev/sda1   2048 1953525134 1953523087 931.5G Linux filesystem

#### create a new filesystem

What is a filesystem? [Arch Linux, filesystem, wiki](https://wiki.archlinux.org/title/File_systems#Create_a_file_system), a goto resource says:

    "In computing, a file system or filesystem controls how data is stored and retrieved. Without a file system, information placed in a storage medium would be one large body of data with no way to tell where one piece of information stops and the next begins. By separating the data into pieces and giving each piece a name, the information is easily isolated and identified." 

Let's make the filesystem of storage an `ext4` type compatible with rpi OS / linux.

```bash
sudo mkfs -t ext4 /dev/sda1
```

Where `dev/sda1` is the new partition name pointer.

#### mount the drive and ensure it mounts on restart
If not already create, make a "mount" /mnt directory, and name a file within, here hd1 for harddrive1.

```bash
sudo mkdir /mnt/hd1
```

Next, change the permissions or ownership of the folder from super user root to regular user. 

```bash
sudo chown $USER:$USER /mnt/hd1
```

Note: 
- [chmod](https://en.wikipedia.org/wiki/chown) is the command to "change owner" or access to file systems.
- pi:pi in this tutorial is specific for user:user, where user:user is the general case. If not sure, type in `users` in terminal.

```bash
sudo blkid
```

Where [blkid](https://man7.org/linux/man-pages/man8/blkid.8.html) locates or prints block devices. A [block device](https://unix.stackexchange.com/questions/259193/what-is-a-block-device) reads/writes to memory one "block" at a time.

Grab the `/dev/sda1` UUID #

Here's what my output looks like:

    pi@headless:/mnt $ sudo blkid
    /dev/mmcblk0p1: LABEL_FATBOOT="bootfs" LABEL="bootfs" UUID="9E81-4F92" BLOCK_SIZE="512" TYPE="vfat" PARTUUID="2ac7bef0-01"
    /dev/mmcblk0p2: LABEL="rootfs" UUID="cf2895ca-6dc2-4797-8040-f76ba1508f41" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="2ac7bef0-02"
    /dev/zram0: UUID="9ba6ae2f-9e71-4ee1-84f3-b5a32d78cf7f" TYPE="swap"
    /dev/sda1: UUID="38e049f5-e511-49a3-a784-f8dad186303c" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="17672728-73c0-ad44-b194-941fcccad345"
    
Specifically `38e049f5-e511-49a3-a784-f8dad186303c`

Time to mount. What is mounting a drive? [Stackexchange](https://unix.stackexchange.com/questions/3192/what-is-meant-by-mounting-a-device-in-linux) says:

    "Mounting is the act of associating a storage device to a particular location in the directory tree."

```bash
sudo nano /etc/fstab
```

This gets inside the file to locate the mounted memory storage partition.

[fstab](https://wiki.archlinux.org/title/Fstab) is used to define how disk partitions, various other block devices, or remote file systems should be mounted into the file system.

```bash
UUID=<UUID_number_here> /mnt/hd1 ext4 nosuid,nodev,nofail 0 1
```

For me it is `UUID=38e049f5-e511-49a3-a784-f8dad186303c /mnt/hd1 ext4 nosuid,nodev,nofail 0 1`

nofail allows the server to boot if the drive is not inserted. Similar for the others.

```bash
sudo mount -a
```

To execute everything in the fstab file

```bash
lsblk
```

Lists the memory

    pi@headless:~ $ lsblk
    NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
    sda           8:0    0 931.5G  0 disk 
    └─sda1        8:1    0 931.5G  0 part /mnt/hd1
    mmcblk0     179:0    0  29.8G  0 disk 
    ├─mmcblk0p1 179:1    0   256M  0 part /boot
    └─mmcblk0p2 179:2    0  29.6G  0 part /
    zram0       254:0    0   5.7G  0 disk [SWAP]

sda1 looks good

To check the read write works

```bash
cd /mnt/hd1/
touch test 
```

you'll get `touch: cannot touch 'test': Permission denied`

so `cd` up a level and change mode on the directory

```bash
cd ..
chmod -R 760 hd1 
```

changes permissions in directory hd1 to read write 

To test it works

```bash
cd hd1 
touch test
```

it should work now

too make sure, we need to reboot

```bash
sudo reboot now 
```

ssh back in (takes 1-3 minutes to reboot)
```bash
ssh pi@headless.local
```

```bash
cd /mnt/hd1 
touch test2
ls
```

If you see "test" and "test2", you did it right.

Now, the last thing is to make sure the newly mounted filesystems are read-write.

type in `mount` to see everything mounted and the "rw" for read-write.

```bash
mount
```

You should see /dev/sda1 and read-write (rw) capable:

`/dev/sda1 on /mnt/hd1 type ext4 (rw,nosuid,nodev,relatime)`

If it's not rw, make the mounting directory read-write:
```bash
sudo mount -o remount,rw /mnt/hd1
```

This enables you to move files from the home directory to the mounted sda1 storage in `/mnt/hd1`

Congrats! You made it. No small feat.


### References:
- [Youtube, Connect a HardDrive / USB Stick on a RaspberryPi (From Terminal) | 4K TUTORIAL, by SpaceRex](https://youtu.be/eQZdPlMH-X8?si=my9CWTv5gJ82yXq_)
- [Armada Alliance Doc, Pi-Node, Mount the drive at boot](https://armada-alliance.com/docs/stake-pool-guides/pi-pool-tutorial/pi-node-full-guide/core-online#mount-the-drive-at-boot)
- [Digikey how to mount an external harddrive](https://www.digikey.com/en/maker/blogs/2022/how-to-connect-a-drive-hddssd-to-a-raspberry-pi-or-other-linux-computers)


