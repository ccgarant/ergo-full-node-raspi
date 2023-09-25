# Part 2: Ergo Full Node Setup (in-work)
Time Allotment:
- 15min-2hr to execute (depending on skill level and snags)

## Setup & Config
The following steps are a combination of the two great following resources mixed in with notes
- [Ergo Platform Docs, Node, Install, Pi](https://docs.ergoplatform.com/node/install/pi/#getting-started)
- [Eeysirhc's ergo-rpi tutorial](https://github.com/Eeysirhc/ergo-rpi/blob/main/docs/ergo-node.md)

### Update the Pi & Install Java

**Important:** Start out in the `/mnt/hd1` directory, this is the external ssd hard drive, with the tons of memory for the ergo-node. Else, you will quickly overload your sd card memory and crash the pi soon enough (trust me :)

```bash
cd /mnt/hd1
```

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

First, ssh back into the pi

```bash
ssh pi@headless.local
```

Then once inside the rpi, change directory to the external hard drive location **very important** /mnt/hd1 and setup a new ergo folder.

```bash
cd /mnt/hd1
mkdir ergo-node
cd ergo-node
```

From the [Ergo Platform Github Release](https://github.com/ergoplatform/ergo/releases), check the latest release version.

Next, copy and paste the following line into a text file. **Remove VERSION** and insert the latest.

```bash
wget https://github.com/ergoplatform/ergo/releases/download/v<VERSION>/ergo-<VERSION>.jar
```
Note: Update the version in the above file. For copy and paste ease:

```bash
wget https://github.com/ergoplatform/ergo/releases/download/v5.0.14/ergo-5.0.14.jar
```

This will take a few minutes.

Note: GNU Wget is a free utility for non-interactive download of files from the Web. [more](https://www.gnu.org/savannah-checkouts/gnu/wget/manual/wget.html)

Next, setup the ergo node configuration file

```bash
sudo nano ergo.conf
```
Note: sudo is super user do (admin privileges). Nano is command line to touch and edit the ergo.conf file. You will now be inside the ergo.conf file. If the file didn't exist, it was just now created.

Copy and paste the contents of the [Reference ergo.conf example file](/example_ergo_config_file.txt) into a separate text file:

    ergo {
        node {
            mining = false
            extraIndex = false
            utxo {
                # Download and apply UTxO set snapshot and full-blocks after that
                utxoBootstrap = false

                # How many utxo set snapshots to store, 0 means that they are not stored at all
                storingUtxoSnapshots = 2

                # How many utxo set snapshots for a height with the same id we need to find in p2p network
                # in order to start downloading it
                p2pUtxoSnapshots = 2
            }
            # Settings releated to headers-chain bootstrapping via NiPoPows
            nipopow {
                # Download PoPoW proof on node utxoBootstrap
                nipopowBootstrap = false

                #how many different proofs we are downloading from other peers
                # and compare with each other, before choosing the best one
                p2pNipopows = 2
            }
        }
    }
    scorex {
        restApi {
            # node which exposes restApi in firewall should define publicly accessible URL of it
            # you will need to enable port forwarding from logging into your router for 9053
            # publicUrl = "http://xxx.xxx.xxx.xxx:9053"
            # apiKeyHash = "CHANGE_ME_HASH"
        }
        network {
            # For below declared address do not include "http://"!
            # you will need to enable port forwarding from logging into your router for 9030
            # declaredAddress = "xxx.xxx.xxx.xxx:9030"
            # nodeName = "my-ergo-node"
        }
    }

You'll need to make the following updates:
- extraIndex ?: If true, will basically store extra blockchain data
- Under scorex
  - publicUrl - update
  - apiKeyHash - update
  - declared address - update
  - nodeName - update


Give it a go and run it! Ctrl+X to overwrite and Yes enter to save.

```bash
java -jar -Xmx2g ergo-<NODE>.jar --mainnet -c ergo.conf
```
Note: Update the version in the command above. e.g 

```bash
java -jar -Xmx2g ergo-5.0.14.jar --mainnet -c ergo.conf
```

### API Key

http://headless.local:9053/panel

Update hello in the command below with a custom API password. Where instead of **hello** insert custom password!

```
curl -X POST "http://213.239.193.208:9053/utils/hash/blake2b" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-d "\"hello\""
```

Type in the password in the browser node panel under "API Key". It should work.

### Enable Port Forwarding

Per [ErgoNodes.net](http://ergonodes.net/) you'll need to allow port forwarding of your ergo node thru your home router for an incoming and outgoing connection.

https://github.com/Satergo/Satergo/wiki/Initial-node-configuration

