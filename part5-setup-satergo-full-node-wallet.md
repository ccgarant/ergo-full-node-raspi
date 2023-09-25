# Part 5: Satergo Full Node Wallet Setup (in-work)
This tutorial steps thru setting up your rpi full node as a "remote node for the awesome open source full node wallet Satergo. Also, steps to get your node reflected in ergonodes.net.

Time allocation: 15-30min

![satergo_settings](/images/satergo_settings.jpeg)

Why [Satergo Wallet](https://satergo.com/) you say?
- open source: [Satergo Github](https://github.com/Satergo/Satergo)
- full node (full trustless & transaction inspection security)
- beautiful design and gui (love the color themes)
- grassroots community built: [Satergo Twitter](https://twitter.com/SatergoWallet)

![why-satergo](/images/satergo_why_use.jpeg)

## Initialize Wallet on the Ergo Node Interface
1. From http://headless.local:9053/panel/ the Ergo Node Explorer -> Initialize Wallet (top left)
2. Create a new wallet or restore from mneumatic seed phrase
3. Test Locking your wallet with your password
4. On the left dashboard > Wallet > Wallet Information > Addresses > More

![ergo-node-wallet](/images/ergo-node-explorer-wallet.jpeg)

5. Click on the address hyperlink to open the Ergo Explorer for the wallet
6. Copy the https address hyperlink.

## Download Satergo & Setup
Now, downloading the Satergo wallet since it's open source is a little different. I haven't found a good way to make a shortcut icon.

You can inspect their code in the [Satergo Wallet Github](https://github.com/Satergo/Satergo/)

1. Basically, from the Satergo website, download the wallet according to your operating system.
2. There might be missing steps here, but once you download and unzip the file, double click `run.command` from the gui explorer or `./run.command` from terminal.
3. If done correctly, you'll see the Satergo welcome screen below. Click `Remote Node`.

![satergo-welcome](/images/satergo-welcome.jpeg)

4. Paste in your Ergo Explorer https wallet address link like so

![satergo-wallet-registration](/images/satergo-wallet-registeration.jpeg)

5. Restore wallet using Seed Phrase.
6. Save your wallet file somewhere.
7. Enjoy

If you find this tutorial helpful, here's my donation tip jar!

![donations-qr-code](/images/wallet-qr-code.jpeg)


## Enable Port Forwarding
This is definitely tricky. You'll need to get into your router and enable "open" `Port Forwarding` of `9053` and `9030`.

Satergo has a good [wiki on Initial Node Configuration](https://github.com/Satergo/Satergo/wiki/Initial-node-configuration) regarding this.

Per [ErgoNodes.net](http://ergonodes.net/) you'll need to allow port forwarding of your ergo node thru your home router for an incoming and outgoing connection.

This section is lacking, please feel free to add helpful steps here.

## Congrats!

You now have a full node running on a raspberry pi with a beautiful wallet gui. All open source, permissionless, and maxmimized trustlessness.

