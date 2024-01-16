##########################################################################
#
#   Python program to help set up a headless raspberry pi ERGO node.
#   
#   Tasks:
#   
#   1. Update and upgrade the linux system
#   2. Download and install Java
#   3. Download and install ERGO node software
#   4. Create ergo node directory, config file, api key hash, get user IP
#   5. Start Node
#   6. Configure system services to initiate Node on startup
#   7. Configure user aliases for node commands
#   8. Reboot system
#
##########################################################################

import os
import subprocess
import time
import json  

# Function to execute shell commands
def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    return stdout.decode(), stderr.decode()
    
# Function to execute shell commands with sudo
def run_sudo_command(command):
    try:
        sudo_command = f"sudo {command}"
        subprocess.run(sudo_command, shell=True, check=True)
        print("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

# Update the Pi and install Java
def update_and_install_java():
    update_command = "sudo apt -q update && sudo apt -q upgrade -y"
    install_java_command = "sudo apt -q install default-jdk -y"
    
    print("Updating the system...")
    run_command(update_command)
    
    print("Installing Java...")
    run_command(install_java_command)

def set_api_key(password):

    # Use the JSON data in the curl request
    api_key_command = f"curl -X POST 'http://128.253.41.49:9053/utils/hash/blake2b' -H 'accept: application/json' -H 'Content-Type: application/json' -d '\"{password}\"'"
    
    stdout, stderr = run_command(api_key_command)
    
    if "400 Bad Request" in stderr:
        print("Error: Bad Request")
        print("Response from the API:")
        print(stdout)
        return None
    
    return stdout.strip()  # Remove leading/trailing whitespaces

# Function to increase SWAP size with elevated permissions
def increase_swap_size():
    swapoff_command = "dphys-swapfile swapoff"
    swapfile_config_path = "/etc/dphys-swapfile"
    
    # Use sudo to open and write to the file
    with open(swapfile_config_path, 'r') as file:
        swapfile_config = file.read()
        swapfile_config = swapfile_config.replace("CONF_SWAPSIZE=100", "CONF_SWAPSIZE=4096")
    
    with open(swapfile_config_path, 'w') as file:
        file.write(swapfile_config)
    
    swapon_command = "dphys-swapfile setup && dphys-swapfile swapon"
    
    print("Optimizing your Raspberry Pi...\n\n")
    run_sudo_command(swapoff_command)
    run_sudo_command(swapon_command)

# Function to create and configure the systemd service for Ergo Node
def create_ergo_node_service(node_path, version):
    os.chdir("/etc/systemd/system")

    print("Setting up system services...")
    full_path = f"{node_path}/ergo-node"
    
    service_file_contents = f"""
[Unit]
Description=Ergo Node Service
Wants=network-online.target
After=network-online.target

[Service]
User=pi
Type=simple
WorkingDirectory={full_path}
ExecStart=/usr/bin/java -jar -Xmx2g ergo-{version}.jar --mainnet -c ergo.conf
KillSignal=SIGINT
RestartKillSignal=SIGINT
TimeoutStopSec=10
LimitNOFILE=32768
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
"""

    # Write the service file contents to /etc/systemd/system/ergo-node.service
    service_file_path = "/etc/systemd/system/ergo-node.service"
    with open(service_file_path, "w") as service_file:
        service_file.write(service_file_contents)
        
    print("Services Config Complete...\n\n")

# Function to start services
def start_services(node_path):

    full_path = f"{node_path}/ergo-node"

    print("Starting Ergo Node Service...")
    os.chdir("/etc/systemd/system")
    
    # Grant permissions to the service file
    grant_permissions_command = "chmod 644 ergo-node.service"
    run_sudo_command(grant_permissions_command)
    
    owner_command = f"chown -R pi:pi {full_path}"
    run_sudo_command(owner_command)
    
    # Update systemd
    update_systemd_command = "systemctl daemon-reload"
    run_sudo_command(update_systemd_command)
    
    # Enable and start the Ergo Node service
    enable_service_command = "systemctl enable ergo-node.service"
    run_sudo_command(enable_service_command)
    
    # Start the Ergo Node service
    start_service_command = "systemctl start ergo-node.service"
    run_sudo_command(start_service_command)
    
    print("Ergo Node Service up and running...\n\n")
    

def alias_config(node_path):

     # Path to the alias file within the specified node_path
    full_path = f"{node_path}/ergo-node"
    alias_file_path = os.path.join(full_path, "ergo_aliases.txt")

    # Alias definitions
    alias_file_contents = """
alias ergo-status="systemctl status ergo-node"
alias ergo-start="sudo systemctl start ergo-node"
alias ergo-stop="sudo systemctl stop ergo-node"
alias ergo-restart="sudo systemctl restart ergo-node"
alias ergo-logs="sudo journalctl --unit=ergo-node --output=cat -f"
alias ergo-help="cat {}/ergo_aliases.txt"
    """.format(full_path)  # Add the alias for ergo-help with the correct path
  
    try:
        # Create the alias file at the specified path
        with open(alias_file_path, 'w') as alias_file:
            alias_file.write(alias_file_contents)
        
        # Check if ~/.bashrc contains a line to source the alias file
        bashrc_file = f"{node_path}/.bashrc"
        source_line = f"source {alias_file_path}"
        
        with open(bashrc_file, 'r') as file:
            bashrc_content = file.read()
            if source_line not in bashrc_content:
                # Append the source line to ~/.bashrc if not already present
                with open(bashrc_file, 'a') as file:
                    file.write(f"{source_line}\n")  # Remove extra newline
        
        print("Aliases added to the alias file and sourced in ~/.bashrc.")
        
    except Exception as e:
        print(f"An error occurred: {e}")


# Setup Ergo Node
def setup_ergo_node(node_path, version):
    
    print("Setting up the ERGO node...")
    full_path = f"{node_path}/ergo-node"
    
    # Create Node Directory
    create_ergo_directory = f"mkdir -p {full_path}"
    run_command(create_ergo_directory)
    
    # Change working directory to full_path
    os.chdir(full_path)
    
    download_ergo_jar = f"wget https://github.com/ergoplatform/ergo/releases/download/v{version}/ergo-{version}.jar"
    
    print("Downloading Ergo Node Software...")
    # Download Ergo JAR and wait for it to finish
    download_process = subprocess.Popen(download_ergo_jar, shell=True)
    download_process.wait()  # Wait for the download to complete
    
    # Check if the download was successful
    if download_process.returncode != 0:
        print("Failed to download Ergo Node JAR. Aborting.")
        return
    
    # Get the public IP address using curl
    public_ip_command = "curl icanhazip.com"
    public_ip, _ = run_command(public_ip_command)
    
    # Ask the user to set the node name
    print("\n\n")
    node_name = input("Enter the node name: ")
    print("\n\n")
    
    # Ask the user to set the API Key password
    api_key_password = input("Enter your API Key password: ")
    print("\n\n")
    
    # Get the API Key hash using the user-defined password
    api_key_hash = set_api_key(api_key_password)
    
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
        publicUrl = "http://{public_ip.strip()}:9053"
        apiKeyHash = {api_key_hash}
    }}
    network {{
        declaredAddress = "{public_ip.strip()}:9030"
        nodeName = "{node_name}"
    }}
}}
"""
    
    # Write ergo.conf contents to the file
    with open(f"{full_path}/ergo.conf", "w") as conf_file:
        conf_file.write(ergo_conf_contents)
    
    print("\nCreating Node config file...")
    print(f"Public IP: {public_ip.strip()}")
    print(f"Node Name: {node_name}")
    print(f"API Hash: {api_key_hash}")
    
    print("\nInitializing Node...")
    
    run_command("java -jar -Xmx2g ergo-5.0.18.jar --mainnet -c ergo.conf > /dev/null 2>&1 &")

if __name__ == "__main__":

    print("\n\n")
    print("This program will help you set up your ergo node. Follow the prompts. Leaving the prompt blank will use default settings.")
    print("\n\n")
    
    # Ask the user to define the Ergo node file path
    node_path = input("Enter the path where you want to install the Ergo node (default /home/pi): ") or "/home/pi"
    print("\n\n")
    
    # Ask the user to input the Ergo version with a default of "5.0.18"
    ergo_version = input("Enter the Ergo version (default is 5.0.18): ") or "5.0.18"
    print("\n\n")
    
    # Run the setup steps
    update_and_install_java()
    setup_ergo_node(node_path, ergo_version)
    
    # Ask the user if they want to reboot
    print("\n\nErgo node setup complete. Now we will configure system services to automate node initialization.")
    print("\n\n")
    
    increase_swap_size()
    create_ergo_node_service(node_path, ergo_version)
    start_services(node_path)
    alias_config(node_path)
    
    # Ask the user if they want to reboot
    print("Ergo node setup complete. Reboot so the changes to the system can take effect.")
    print("\n\n")
    print("Aliases were configured for your node.\n")
    print("ergo-status shows the status of the node")
    print("ergo-start will start the node service")
    print("ergo-stop will end the node service")
    print("ergo-restart will restart the node")
    print("ergo-help will show all node commands")
    print("ergo-logs shows the log file of the node\n\n")
    
    
    reboot_choice = input("Do you want to reboot? (yes/no): ")
    if reboot_choice.lower() == "yes" or reboot_choice.lower() == "y":
        print("Rebooting now")
        run_sudo_command("reboot")
    else:
        print("Reboot soon.")

        
