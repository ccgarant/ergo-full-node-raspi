# Ergo Node Python Script Setup Tutorial

This assumes that you have basic knowledge of Raspberry Pi and Linux system administration.

This Python program helps you set up a headless Raspberry Pi Ergo node. It automates the process of updating the Linux system, installing Java, downloading and configuring the Ergo node software, creating system services for automatic node initialization, configuring user aliases for node commands, and optionally rebooting the system.

## Prerequisites

Before running the program, ensure you have the following prerequisites:

- A Raspberry Pi (tested on Raspberry Pi 4)
- Raspberry Pi OS installed (tested on Raspberry Pi OS Lite)
- Internet connectivity on the Raspberry Pi

## Usage

Follow these steps to set up your Ergo node:

1. **Install Git:**

Install the Git program onto your Raspberry Pi:
   
```bash
sudo apt-get install git
```

2. **Clone the Repository:**

Clone the GitHub repository containing the program onto your Raspberry Pi:
   
```bash
git clone 'https://github.com/ccgarant/ergo-full-node-raspi.git'
```

3. **Navigate to the Program Directory:**

Use the `cd` command to enter the program directory:

```bash
cd 02-python-script-automated
```

4. **Make the Program Executable:**

Make the program script executable using the following command:

```bash
chmod +x ergo_node_setup.py
```

5. **Run the Program:**

Execute the program with the following command for a full node from scratch (no bootstrapping):

```bash
sudo python ergo_node_setup.py
```

The program will start and guide you through the Ergo Node setup process. Follow the prompts, and leave the prompt blank to use default settings when applicable.

**Important:** The program will perform tasks that require administrative (sudo) privileges. You may be prompted to enter your password during the execution of certain commands.

## Script Programming Description

This Python program automates the following tasks for setting up an Ergo node on a Raspberry Pi:

**Tasks:**   
1. Update and upgrade the Linux system
2. Download and install Java
3. Download and install Ergo node software
4. Create Ergo node directories, config file, API key hash, get user IP
5. Configure systemd service to manage Ergo node
6. Configure user aliases for node commands
7. Reboot system (optional)

## Ergo Node Commands

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

