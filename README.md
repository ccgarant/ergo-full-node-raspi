# Tutorial: Running an Ergo Full Node on a Headless Raspberry Pi

A tutorial on how to setup and run an Ergo Full Node on a Headless Raspberry Pi.

![test1](/images/rpi-finished-iso-view.jpeg)

A headless raspberry pi (pi, raspi, or raspberrypi) does not have a monitor or mouse plugged in. Instead, you are securely remoted into the pi via the terminal command line.

This is geared toward beginners who want to learn and hopefully get more Ergo nodes running! See [ErgoNodes.net](http://ergonodes.net/).

Don't worry, it's not that hard, and you will feel super cool afterwards.

The tutorial includes:

## [Part 1: Headless Raspi Setup & Login](/part1-raspi-setup.md)
- Hardware Shopping List
- Brief Intro to Headless Command Line Interface (CLI)
- Flash Setup & Configuration of the Pi
- Secure Shelling into the Pi
- Setup External Storage USB

## [Part 2: Ergo Full Node Configure & Run](/part2-ergo-full-node.md) 
- Setup & Configure the Pi for Ergo Node
- Headless Ergo Node setup
    - goal is for nipopow bootstrap setup
- Run the node in the background thru a tmux session

## [Part 3: Run the Node in the background to fully sync](/part3-run-node-in-background-tmux.md)
- Why is this needed (ssh connection breaks when computer sleeps)
- What is a tmux session?
- Run the node syncing in the background as a tmux session

## [Part 4: Robustly run the node in the background as a systemd](/part4-robust-run-node-in-background-systemd.md)
- Robustly configure the rpi to run the node upon startup, restart, and in the background
- Port forwarding to get incoming peer connections (not just outgoing).

## [Ergo Full Node Resources](/resources.md)
A cheatsheet and comprehensive list of references.

------------------------------------
## Issues, Improvements, Help

This project is still in work #buildinginpublic

If anything doesn't work or needs clarification, open a github Issue, or fork and submit a pull request update.

If you need help, DM me on twitter [@thestophe](https://twitter.com/TheStophe) or find me in the [Matrix #ergomatrix:matrix.org](https://matrix.to/#/#ergomatrix:matrix.org).

-------------------

## Too Much Work - Something Easier!

A really simple and nice option is to just use [Satergo](https://satergo.com/) full node wallet.

You can just download and run it, batteries included. If you don't have the computer memory storage, you can reference a "remote" full node.  

This is a great option, plus the UI/UX is beautiful.

-------------------

## Special Thanks
Appreciate the help from the following folks and resources!
- [Ergo Platform](https://twitter.com/Ergo_Platform) Documentation, tutorial, and chatbot
- [Eeysirhc](https://twitter.com/Eeysirhc) for an awesome [ergo-rpi tutorial](https://github.com/Eeysirhc/ergo-rpi) that was easy to follow and really helped
- [Wael](https://twitter.com/Piada_stakePool) Teaching me to tmux
- [WCat of Star Forge Stake Pool ](https://twitter.com/Star_Forge_Pool) for continuous education in all things sysadmin & prepping :) 
- [Reqlez ($psiloblox)](https://twitter.com/PSILOBLOX) for ergo.conf configuration file help & the Rosen Bridge early adopters invitation
- [ErgOne](https://twitter.com/Erg0ne) & [koukarin4](https://twitter.com/koukarin4) for the encouragement of a helpful tutorial
- [Armada Alliance](https://twitter.com/alliance_armada) for the community of ARM builders continusouly educating and amazing [documentation resources](https://armada-alliance.com/docs/)
- [Satergo Project](https://twitter.com/SatergoWallet) for an awesome full node ergo wallet and ergonodes.net platform
- [Ergo Foundation](https://twitter.com/ErgoFoundation) for the continuous AMA's teaching grassroot decentralization matters
- [Kushti](https://twitter.com/chepurnoy) for relentless unstoppable building