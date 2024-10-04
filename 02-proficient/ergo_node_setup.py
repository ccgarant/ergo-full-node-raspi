#!/usr/bin/env python3
#######################################################################
#
#   Python program to help set up a headless Raspberry Pi Ergo node.
#   
#   Tasks:
#   
#   1. Update and upgrade the Linux system
#   2. Download and install Java
#   3. Download and install Ergo node software
#   4. Create Ergo node directories, config file, API key hash, get user IP
#   5. Configure systemd service to manage Ergo node
#   6. Configure user aliases for node commands
#   7. Reboot system (optional)
#
#######################################################################

import os
import subprocess
import sys
import getpass

# Function to execute shell commands and handle errors
def run_command(command, capture_output=True):
    try:
        result = subprocess.run(
            command, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            shell=True, 
            check=True, 
            text=True
        )
        if capture_output:
            return result.stdout.strip()
        return ""
    except subprocess.CalledProcessError as e:
        print(f"\n[Error] Command failed: {command}")
        print(f"[Error] Error Output: {e.stderr.strip()}\n")
        sys.exit(1)

# Function to execute shell commands with sudo and handle errors
def run_sudo_command(command):
    try:
        sudo_command = f"sudo {command}"
        subprocess.run(
            sudo_command, 
            shell=True, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True
        )
        print(f"[Success] Executed: {sudo_command}")
    except subprocess.CalledProcessError as e:
        print(f"\n[Error] Failed to execute: {sudo_command}")
        print(f"[Error] Error Output: {e.stderr.strip()}\n")
        sys.exit(1)

# Update the system and install Java
def update_and_install_java():
    update_command = "apt -q update && apt -q upgrade -y"
    install_java_command = "apt -q install default-jdk -y"

    print("\n[Step 1] Updating the system...")
    run_sudo_command(update_command)
    print("[Step 1] System update and upgrade completed.\n")

    print("[Step 2] Installing Java...")
    run_sudo_command(install_java_command)
    print("[Step 2] Java installation completed.\n")

# Function to securely get API Key hash
def set_api_key(password):
    # Implement local hashing to avoid sending passwords over the network
    import hashlib

    print("[Step 4] Generating API Key hash locally...")
    # Use Blake2b hash algorithm
    hash_obj = hashlib.blake2b()
    hash_obj.update(password.encode('utf-8'))
    api_key_hash = hash_obj.hexdigest()
    print("[Success] API Key hash generated successfully.\n")
    return api_key_hash

# Function to increase SWAP size with elevated permissions
def increase_swap_size():
    swapfile_config_path = "/etc/dphys-swapfile"
    backup_swap_config = f"{swapfile_config_path}.bak"

    print("[Step 3] Increasing SWAP size...")

    # Backup the original swapfile configuration
    if not os.path.exists(backup_swap_config):
        run_sudo_command(f"cp {swapfile_config_path} {backup_swap_config}")
        print(f"[Backup] Original swapfile config backed up to {backup_swap_config}")
    else:
        print(f"[Backup] Swapfile config backup already exists at {backup_swap_config}")

    # Modify the swap size (e.g., set to 2048MB)
    run_sudo_command(
        f"sed -i 's/^CONF_SWAPSIZE=.*/CONF_SWAPSIZE=2048/' {swapfile_config_path}"
    )
    print("[Modification] Swap size set to 2048MB in swapfile configuration.")

    # Restart swapfile service
    run_sudo_command("dphys-swapfile setup")
    run_sudo_command("dphys-swapfile swapon")
    print("[Success] Swap size updated and swapfile service restarted.\n")

# Function to create and configure the systemd service for Ergo Node
def create_ergo_node_service(node_path, version, data_dir, username):
    service_file_path = "/etc/systemd/system/ergo-node.service"

    print("[Step 5] Creating systemd service for Ergo Node...")

    service_file_contents = f"""
[Unit]
Description=Ergo Node Service
Wants=network-online.target
After=network-online.target

[Service]
User={username}
Group={username}
Type=simple
WorkingDirectory={node_path}/ergo-node
ExecStart=/usr/bin/java -Xmx4g -jar {node_path}/ergo-node/ergo-{version}.jar --mainnet -c {node_path}/ergo-node/ergo.conf
KillSignal=SIGINT
RestartKillSignal=SIGINT
TimeoutStopSec=60
LimitNOFILE=32768
Restart=always
RestartSec=60
StandardOutput=journal
StandardError=journal
PIDFile={data_dir}/ergo.pid

[Install]
WantedBy=multi-user.target
    """

    try:
        with open(service_file_path, "w") as service_file:
            service_file.write(service_file_contents)
        print(f"[Success] Service file created at {service_file_path}")
    except Exception as e:
        print(f"\n[Error] Failed to write service file: {e}\n")
        sys.exit(1)

    # Set permissions for the service file
    run_sudo_command(f"chmod 644 {service_file_path}")
    print(f"[Success] Service file permissions set to 644.\n")

# Function to start and enable the Ergo Node service
def start_services(username):
    print("[Step 6] Starting and enabling Ergo Node service...")

    # Reload systemd daemon to recognize the new service
    run_sudo_command("systemctl daemon-reload")

    # Enable the service to start on boot
    run_sudo_command("systemctl enable ergo-node.service")
    print("[Info] Service enabled to start on boot.")

    # Start the service
    run_sudo_command("systemctl start ergo-node.service")
    print("[Info] Ergo Node service started.")

    # Check service status
    status = run_command("systemctl is-active ergo-node.service")
    if status == "active":
        print("[Success] Ergo Node service is active and running.\n")
    else:
        print("[Error] Ergo Node service failed to start. Check logs for details.")
        sys.exit(1)

# Function to configure user aliases
def alias_config(username):
    alias_file_path = f"/home/{username}/.bash_aliases"

    print("[Step 7] Configuring user aliases...")

    alias_file_contents = f"""
# Ergo Node Aliases
alias ergo-status="systemctl status ergo-node"
alias ergo-start="sudo systemctl start ergo-node"
alias ergo-stop="sudo systemctl stop ergo-node"
alias ergo-restart="sudo systemctl restart ergo-node"
alias ergo-logs="sudo journalctl -u ergo-node.service -f"
alias ergo-help="cat {alias_file_path}"
    """

    try:
        # Append aliases to .bash_aliases
        with open(alias_file_path, 'a') as alias_file:
            alias_file.write(alias_file_contents)
        print(f"[Success] Aliases added to {alias_file_path}")

        # Ensure .bashrc sources .bash_aliases
        bashrc_path = f"/home/{username}/.bashrc"
        with open(bashrc_path, 'r') as file:
            bashrc_content = file.read()
            source_line = f"source ~/.bash_aliases"
            if source_line not in bashrc_content:
                with open(bashrc_path, 'a') as file_append:
                    file_append.write(f"\n# Source Ergo aliases\n{source_line}\n")
                print(f"[Success] Added source line to {bashrc_path}")
            else:
                print(f"[Info] {bashrc_path} already sources .bash_aliases")
        print("[Success] Alias configuration completed.\n")
    except Exception as e:
        print(f"\n[Error] An error occurred while configuring aliases: {e}\n")
        sys.exit(1)

# Function to create Ergo node directories and configuration
def setup_ergo_node(node_path, version, data_dir, username):
    print("[Step 4] Setting up the Ergo node...")

    ergo_node_path = os.path.join(node_path, "ergo-node")

    # Create Node Directory
    run_command(f"mkdir -p {ergo_node_path}")
    print(f"[Success] Created Ergo node directory at {ergo_node_path}")

    # Change working directory to ergo_node_path
    os.chdir(ergo_node_path)

    # Download Ergo JAR
    download_ergo_jar = f"wget https://github.com/ergoplatform/ergo/releases/download/v{version}/ergo-{version}.jar"
    print("[Info] Downloading Ergo Node Software...")
    run_command(download_ergo_jar)
    print("[Success] Ergo JAR downloaded successfully.\n")

    # Get the public IPv6 address
    print("[Info] Fetching public IPv6 address...")
    public_ip_command = "curl -6 -s ifconfig.co"  # Using -6 to ensure IPv6
    public_ip = run_command(public_ip_command)
    if not public_ip:
        print("\n[Error] Failed to retrieve public IPv6 address.")
        sys.exit(1)
    print(f"[Success] Public IPv6 Address: {public_ip}\n")

    # Ask the user to set the node name
    node_name = input("Enter the node name: ").strip()
    if not node_name:
        node_name = "ErgoNode"  # Default node name
        print(f"[Info] No node name provided. Using default: {node_name}")

    # Ask the user to set the API Key password
    api_key_password = getpass.getpass("Enter your API Key password: ").strip()
    if not api_key_password:
        print("\n[Error] API Key password cannot be empty.")
        sys.exit(1)

    # Get the API Key hash using the user-defined password
    api_key_hash = set_api_key(api_key_password)
    if not api_key_hash:
        print("\n[Error] Failed to generate API Key hash.")
        sys.exit(1)
    print(f"[Success] API Key Hash: {api_key_hash}\n")

    # Contents of ergo.conf file with API Key hash and node name
    ergo_conf_contents = f"""
ergo {{
    node {{
        mining = false
        extraIndex = false

        utxo {{
            utxoBootstrap = false
            storingUtxoSnapshots = 2
            p2pUtxoSnapshots = 2
        }}
        nipopow {{
            nipopowBootstrap = false
            p2pNipopows = 2
        }}
    }}
}}
scorex {{
    restApi {{
        publicUrl = "http://[{public_ip}]:9053/"
        apiKeyHash = "{api_key_hash}"
    }}
    network {{
        declaredAddress = "[{public_ip}]:9030"
        nodeName = "{node_name}"
    }}
}}

# Ensure the data directory is set correctly
dataDir = "{data_dir}"
    """

    # Write ergo.conf contents to the file
    try:
        with open(f"{ergo_node_path}/ergo.conf", "w") as conf_file:
            conf_file.write(ergo_conf_contents)
        print("[Success] ergo.conf configuration file created successfully.\n")
    except Exception as e:
        print(f"\n[Error] Failed to write ergo.conf: {e}\n")
        sys.exit(1)

    # Create necessary .ergo subdirectories
    run_command(f"mkdir -p {data_dir}/peers {data_dir}/blocks {data_dir}/chainstate {data_dir}/logs")
    print(f"[Success] Created data directories under {data_dir}")

    run_sudo_command(f"chown -R {username}:{username} {data_dir}")
    run_sudo_command(f"chmod -R 700 {data_dir}")
    print(f"[Success] Set ownership and permissions for {data_dir}\n")

    print("[Info] Ergo node setup completed.\n")

def main():
    print("\n\n")
    print("#############################################")
    print("#      Ergo Node Setup Script v2.1          #")
    print("#############################################\n")

    # Prompt user for installation directory
    default_node_path = f"/home/{getpass.getuser()}"
    node_path_input = input(f"Enter the path where you want to install the Ergo node (default {default_node_path}): ").strip()
    node_path = node_path_input if node_path_input else default_node_path
    print(f"[Input] Using Ergo node path: {node_path}\n")

    # Prompt user for Ergo version
    default_ergo_version = "5.0.22"
    ergo_version_input = input(f"Enter the Ergo version to install (default is {default_ergo_version}): ").strip()
    ergo_version = ergo_version_input if ergo_version_input else default_ergo_version
    print(f"[Input] Using Ergo version: {ergo_version}\n")

    # Prompt user for their username
    current_user = getpass.getuser()
    print(f"[Info] Current system user: {current_user}")
    username_input = input(f"Enter the username to run the Ergo node (default is {current_user}): ").strip()
    username = username_input if username_input else current_user
    print(f"[Input] Using username: {username}\n")

    # Define the data directory
    default_data_dir = f"/home/{username}/.ergo"  # Default data directory
    # Optionally, allow user to input a different data directory
    data_dir_input = input(f"Enter the data directory for Ergo node (default is {default_data_dir}): ").strip()
    data_dir = data_dir_input if data_dir_input else default_data_dir
    print(f"[Input] Using data directory: {data_dir}\n")

    # Run the setup steps
    update_and_install_java()
    setup_ergo_node(node_path, ergo_version, data_dir, username)
    increase_swap_size()
    create_ergo_node_service(node_path, ergo_version, data_dir, username)
    start_services(username)
    alias_config(username)

    # Final instructions
    print("\n#############################################")
    print("#        Ergo Node Setup Complete!          #")
    print("#############################################\n")

    print("Aliases have been configured for your node:")
    print("- ergo-status: Shows the status of the node")
    print("- ergo-start: Starts the node service")
    print("- ergo-stop: Stops the node service")
    print("- ergo-restart: Restarts the node service")
    print("- ergo-logs: Shows the log file of the node")
    print("- ergo-help: Shows all node commands\n")

    # Prompt to reboot
    reboot_choice = input("Do you want to reboot now to apply all changes? (yes/no): ").strip().lower()
    if reboot_choice in ["yes", "y"]:
        print("\n[Action] Rebooting the system...")
        run_sudo_command("reboot")
    else:
        print("\n[Info] Reboot aborted. Please reboot manually later to apply all changes.\n")

if __name__ == "__main__":
    main()