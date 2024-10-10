# Ergo Node Python Script Update Tutorial

This assumes that you have basic knowledge of Raspberry Pi and Linux system administration.

## Prerequisites

- The script assumes that you have installed the Ergo Node using 'ergo_node_setup.py'.
- The node should be installed in the default directory: '~/ergo-node'.
- You must have sudo privileges to move files and restart services.

## Make the Update

Make the program script executable using the following command (first time only):

```bash
chmod +x ergo_node_update.py
```

Run the program

```bash
python3 ergo_node_update.py
```

The program will start and guide you through the Ergo Node setup process. Follow the prompts, and leave the prompt blank to use default settings when applicable.

**Important:** The program will perform tasks that require administrative (sudo) privileges. You may be prompted to enter your password during the execution of certain commands.

---------------

## Ergo Node Update Script Description

This script automates the process of updating your Ergo Node to the latest mainnet release.
It performs the following tasks:

1. Determines the current version of the Ergo Node installed.
2. Fetches the latest mainnet release version from the Ergo GitHub repository.
3. Compares the current version with the latest version.
   - If already running the latest version, it provides proofs and exits.
4. Prompts the user to confirm updating to the latest version.
5. Downloads the latest Ergo Node JAR file.
6. Updates the systemd service file to point to the new JAR version.
7. Restarts the Ergo Node service to apply the changes.
8. Provides confirmation and instructions to verify the update.



## Ergo Node Command Aliases

Aliases were configured for your node to make node interaction easier:

```bash 
ergo-status     shows the status of the node.
ergo-start      will start the node service.
ergo-stop       will end the node service.
ergo-restart    will restart the node.
ergo-help       will show all node commands.
ergo-logs       shows the log file of the node.
```
---

