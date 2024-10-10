# Tutorial: Running an Ergo Full Node on a Headless Raspberry Pi

A tutorial on how to setup and run an Ergo Full Node on a Headless Raspberry Pi.

![test1](/images/rpi-finished-iso-view.jpeg)

A headless raspberry pi (pi, raspi, or raspberrypi) does not have a monitor or mouse plugged in. Instead, you are securely remoted into the pi via the terminal command line.

This is geared toward beginners who want to learn and hopefully get more Ergo nodes running! See [ErgoNodes.net](http://ergonodes.net/).

Don't worry, it's not that hard, and you will feel super cool afterwards.

The tutorial includes 3 Tutorial Levels:

## [Manual Step-by-Step Setup (Best For Detail Learning)](/01-manual-step-by-step/node-beginner-tutorial.md)
Recommended for just getting started, step-by-step guide with heavy hand holding.

## [Python Script Automated Setup (**RECOMMENDED**)](/02-python-script-automated/node-proficient-tutorial.md)
Recommended after you've setup a node a few times, automated script for setup. Quick start.

## [Docker Ergo Node (IN-WORK)](/03-docker-ergo-node/node-specialist-tutorial.md)
(COMING SOON) Recommended docker ergo node for the super savvy. This will allow bootstrap from genesis or start from a snapshot for a quick sync.

## [Ergo Node Update](/resources/ergo_node_update.py)
To update your ergo node, use this script in resources.

--------------------------------------

## Ergo Full Node Resources
A comprehensive list of resources, references, and cheatsheets in the /resources folder.
- [Ergo Full Node Resource List](/resources/resources.md) - A comprehensive list of Ergo resources for everything you might need.
- [Run the Node in the Background as a Tmux Session](/resources/run-node-in-background-tmux.md)
    - Not needed, but helpful too to run terminal from laptop and not break ssh connection
    - Why is this needed (ssh connection breaks when computer sleeps)
    - What is a tmux session?
    - Run the node syncing in the background as a tmux session
- [Command Cheatsheet](/resources/command_cheatsheet.md) - A list of copy paste ready daily commands
- [Example Ergo Config File Light](/resources/example_ergo_config_file_light.txt) - A lightweight ergo.conf example file
- [Example Ergo Config File](/resources/example_ergo_config_file.txt) - A comprehensive (heavy) ergo.conf example file
- [Example Ergo Node Service File](/resources/example-ergo-node-service-file.txt) - For systemctl running in the background copy paste ready.


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
- [jkrek17](https://twitter.com/jkrek17) for the proficient python script node setup automation.
- [Reqlez ($psiloblox)](https://twitter.com/PSILOBLOX) for ergo.conf configuration file help & the Rosen Bridge early adopters invitation
- [ErgOne](https://twitter.com/Erg0ne) & [koukarin4](https://twitter.com/koukarin4) for the encouragement of a helpful tutorial
- [Armada Alliance](https://twitter.com/alliance_armada) for the community of ARM builders continusouly educating and amazing [documentation resources](https://armada-alliance.com/docs/)
- [Satergo Project](https://twitter.com/SatergoWallet) for an awesome full node ergo wallet and ergonodes.net platform
- [Ergo Foundation](https://twitter.com/ErgoFoundation) for the continuous AMA's teaching grassroot decentralization matters
- [Kushti](https://twitter.com/chepurnoy) for relentless unstoppable building

-------------

## Donations or Staking

If you find this tutorial helpful, here's my donation tip jar! #Ergo2Top10

![donations-qr-code](/images/wallet-qr-code.jpeg)

```bash
9htXsxhTNpt8LaSdLF5PDqNe99RaXmMRTAJu3iTB57ivxx3UNFa
```

Or better yet, if an $ADA hodler too, Stake to [BALNC Pool](https://pool.pm/a43ceac028a673e9f8611de0f683c70fdcadde560f28c2fb8cfabc81)! We provide high quality on-chain analysis and data visualization using Svelte: https://www.balanceanalytics.io/. Cheers!

## Questions?
Feel free to jump into our [Ergo - BALANCE](https://matrix.to/#/#ergo:forum.balanceanalytics.io) room to chat and ask questions. This chat is in the Matrix.org open source commmunication protocol, we recommend using the Element Client.