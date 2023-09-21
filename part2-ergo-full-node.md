# Part 2: Ergo Full Node Setup (in-work)
Time Allotment:
- 15min-2hr to execute (depending on skill level and snags)

## Setup & Config
The following steps are a combination of the two great following resources mixed in with notes
- [Ergo Platform Docs, Node, Install, Pi](https://docs.ergoplatform.com/node/install/pi/#getting-started)
- [Eeysirhc's ergo-rpi tutorial](https://github.com/Eeysirhc/ergo-rpi/blob/main/docs/ergo-node.md)

### Update the Pi & Install Java
The node is built with Scala but is run by Java, thus we'll need to install package dependencies Java Development Kit.

Preparation, update and upgrade the rpi. Check Java SDK.

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install default-jdk -y
```

Install the Java JDK

```bash
sudo apt install default-jdk
```

To check java installed properly check the version

```bash
java -version
```

### Increase SWAP size

The steps below optimizes your Pi's hardware and extends its operational capabilities for this specific purpose.

```bash
sudo dphys-swapfile swapoff
sudo nano /etc/dphys-swapfile
```

Edit the CONF_SWAPSIZE default value of 100 to 4096 mega bytes

> CONF_SWAPSIZE=4096

Save file with "CTRL + X" then hit "Y" for Yes to save, and "ENTER" to confirm.

Turn swapfile on

```bash
sudo dphys-swapfile setup
sudo dphys-swapfile swapon
```

Reboot to start fresh

```bash
sudo reboot
```

## Ergo Node Steps
The following steps will setup the ergo node's configuration, download the node software ".jar" file, setup and run the node.

We will then check the node is syncing with the Ergo Node Explorer site in the browser.

First, inside the rpi, change directory to home and setup a new ergo folder.

```bash
cd
mkdir ergo-node
cd ergo-node
```

Inside the ergo-node directory, download the node software off [github](https://github.com/ergoplatform/ergo/releases)

```bash
wget https://github.com/ergoplatform/ergo/releases/download/v<VERSION>/ergo-<VERSION>.jar
```
Note: Update the version in the above file. e.g. `wget https://github.com/ergoplatform/ergo/releases/download/v5.0.13/ergo-5.0.13.jar`

Note: GNU Wget is a free utility for non-interactive download of files from the Web. [more](https://www.gnu.org/savannah-checkouts/gnu/wget/manual/wget.html)

Next, setup the ergo node configuration file

```bash
sudo nano ergo.conf
```
Note: sudo is super user do (admin privileges). Nano is command line to touch and edit the ergo.conf file. You will now be inside the ergo.conf file. If the file didn't exist, it was just now created.

<reference example file>

Give it a go and run it!

```bash
java -jar -Xmx2g ergo-<NODE>.jar --mainnet -c ergo.conf
```
Note: Update the version in the command above. e.g `java -jar -Xmx2g ergo-5.0.13.jar --mainnet -c ergo.conf`

### API Key

http://headless.local:9053/panel

Update hello in the command below with a custom API password.

```
curl -X POST "http://213.239.193.208:9053/utils/hash/blake2b" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-d "\"hello\""
```

### Enable Port Forwarding

Per [ErgoNodes.net](http://ergonodes.net/) you'll need to allow port forwarding of your ergo node thru your home router for an incoming and outgoing connection.

https://github.com/Satergo/Satergo/wiki/Initial-node-configuration

