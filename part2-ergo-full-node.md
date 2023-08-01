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

