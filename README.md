# Tutorial: Running an Ergo Full Node on a Headless Raspberry Pi

A tutorial on how to setup and run an Ergo Full Node on a Headless Raspberry Pi.

![test1](/images/IMG_4552.jpeg)

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
