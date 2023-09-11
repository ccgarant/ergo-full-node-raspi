# Part 2: Ergo Full Node Setup
Time Allotment:
- 1hr to order parts (if you don't have it)
- 1hr-3hr to execute (depending on skill level and snags)

## Setup & Config
The following steps will install package dependencies like java, and streamline memory
https://docs.ergoplatform.com/node/install/pi/#getting-started
bonus work: recommend do the zram //tldr get 50% more out of your memory, more efficient solution, backend sharing
sudo nano zram-swap-config.config
update to recommended parameters per raspi

java -version //to check install correctly
sudo reboot //just to make sure everything is good

## Ergo Node Steps

Follow:
https://github.com/Eeysirhc/ergo-rpi/blob/main/docs/ergo-node.md


e.g.
`wget https://github.com/ergoplatform/ergo/releases/download/v5.0.13/ergo-5.0.13.jar`

e.g.
```
curl -X POST "http://213.239.193.208:9053/utils/hash/blake2b" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-d "\"hello\""
```

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

java -jar -Xmx2g ergo-<NODE>.jar --mainnet -c ergo.conf
e.g
`java -jar -Xmx2g ergo-<NODE>.jar --mainnet -c ergo.conf`

http://headless.local:9053/panel

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

### Enable Port Forwarding

Per [ErgoNodes.net](http://ergonodes.net/) you'll need to allow port forwarding of your ergo node thru your home router for an incoming and outgoing connection.

https://github.com/Satergo/Satergo/wiki/Initial-node-configuration

