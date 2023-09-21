# Part 2: Ergo Full Node Setup (in-work)
Time Allotment:
- 15min-2hr to execute (depending on skill level and snags)

## Setup & Config
The following steps are a combination of the following two great resources mixed in with personal comments and notes
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

Save file with "CTRL + X" then hit "Y" and "ENTER" to confirm

```bash
sudo dphys-swapfile setup
sudo dphys-swapfile swapon
```

Reboot to start fresh

```bash
sudo reboot
```


## Ergo Node Steps

Follow:



e.g.
`wget https://github.com/ergoplatform/ergo/releases/download/v5.0.13/ergo-5.0.13.jar`



ergo {
  node {
    mining = false
  }
}

scorex {
 restApi {
    # Hex-encoded Blake2b256 hash of an API key. 
    # Should be 64-chars long Base16 string.
    # below is the hash of the string 'hello'
    # replace with your actual hash 
    apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"
  }
}

```bash
java -jar -Xmx2g ergo-<NODE>.jar --mainnet -c ergo.conf
```

e.g `java -jar -Xmx2g ergo-5.0.13.jar --mainnet -c ergo.conf`



recommend the step-by-step guide
https://github.com/ergoplatform/ergo/wiki/Set-up-a-full-node

recommend downloading scala package manager
https://www.scala-sbt.org/download.html
sbt - scala interactive build tool
Linux Debian, copy paste code into terminal
sbt -v  //to check version but also initiates it
might need to compile jar from a github clone
had some errors with java memory after sbt -v...
let's see if it hurts us.
mkdir github
git clone https://github.com/ergoplatform/ergo.git
cd ergo
//tried ./ergo-installer.sh needed --api-key
sbt assemble //to build jar file from scratch
cd //return home
mkdir ergo
cd ergo
mkdir ergo_folder
cd ergo_folder
echo " " > ergo.conf //makes empty file
nano ergo.conf

### API Key

http://headless.local:9053/panel

e.g.
```
curl -X POST "http://213.239.193.208:9053/utils/hash/blake2b" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-d "\"hello\""
```

### Enable Port Forwarding

Per [ErgoNodes.net](http://ergonodes.net/) you'll need to allow port forwarding of your ergo node thru your home router for an incoming and outgoing connection.

https://github.com/Satergo/Satergo/wiki/Initial-node-configuration

