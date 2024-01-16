# Raspberry Pi Ergo Node Setup

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
cd ergo-node-setup
```

4. **Make the Program Executable:**

Make the program script executable using the following command:

```bash
chmod +x ergo_node_setup.py
```

5. **Run the Program:**

Execute the program with the following command:

```bash
sudo python ergo_node_setup.py
```

The program will start and guide you through the Ergo Node setup process. Follow the prompts, and leave the prompt blank to use default settings when applicable.

**Important:** The program will perform tasks that require administrative (sudo) privileges. You may be prompted to enter your password during the execution of certain commands.

6. **Reboot (Optional):**

After the Ergo Node setup is complete, the program will prompt you to reboot your Raspberry Pi.

If you choose to reboot, the Raspberry Pi will restart. If not, you can manually reboot later with the `sudo reboot` command.

## Program Description

This Python program automates the following tasks for setting up an Ergo node on a Raspberry Pi:

1. Update and upgrade the Linux system.
2. Download and install Java.
3. Download and install the Ergo node software.
4. Create the Ergo node directory, configuration file, API key hash, and obtain the user's IP address.
5. Start the Ergo Node.
6. Configure system services to initiate the Ergo Node on startup.
7. Configure user aliases for Ergo node commands.
8. Optionally, reboot the Raspberry Pi to apply configuration changes.

---

**Note:** This program was created to simplify the setup process for an Ergo node on a Raspberry Pi and assumes that you have basic knowledge of Raspberry Pi and Linux system administration.

