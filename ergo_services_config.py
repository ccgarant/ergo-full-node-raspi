import os
import subprocess
import time
import json  

# Function to execute shell commands
def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    return stdout.decode(), stderr.decode()
    
    # Increase SWAP size with elevated permissions
def increase_swap_size():
    swapoff_command = "sudo dphys-swapfile swapoff"
    swapfile_config_path = "/etc/dphys-swapfile"
    
    # Use sudo to open and write to the file
    with open(swapfile_config_path, 'r') as file:
        swapfile_config = file.read()
        swapfile_config = swapfile_config.replace("CONF_SWAPSIZE=100", "CONF_SWAPSIZE=4096")
    
    with open(swapfile_config_path, 'w') as file:
        file.write(swapfile_config)
    
    swapon_command = "sudo dphys-swapfile setup && sudo dphys-swapfile swapon"
    
    print("Optimizing your raspberry pi...")
    run_command(swapoff_command)
    run_command(swapon_command)

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
    
    # Grant permissions to the service file
    grant_permissions_command = "sudo chmod 644 ergo-node.service"
    run_command(grant_permissions_command)
    
    # Update systemd
    update_systemd_command = "sudo systemctl daemon-reload"
    run_command(update_systemd_command)
    
    # Enable and start the Ergo Node service
    enable_service_command = "sudo systemctl enable ergo-node.service"
    run_command(enable_service_command)
    
    # Start the Ergo Node service
    start_service_command = "sudo systemctl start ergo-node.service"
    run_command(start_service_command)


if __name__ == "__main__":

    print("\n\n")
    print("This program will help you set up your ergo node services.")
    print("The node will now run when automatically if/when raspberry PI is rebooted.")
    print("\n\n")
    
    # Ask the user to define the Ergo node file path
    node_path = input("Enter the path where you installed the Ergo node (default /home/pi): ") or "/home/pi"
    print("\n\n")
    
    # Ask the user to input the Ergo version with a default of "5.0.18"
    ergo_version = input("Enter the Ergo version (default is 5.0.18): ") or "5.0.18"
    print("\n\n")
    
    # Run the setup steps
    increase_swap_size()
    create_ergo_node_service(node_path, ergo_version)
    
    # Ask the user if they want to reboot
    print("Ergo node setup complete. Reboot so the changes to the system can take effect.")
    print("\n\n")
        
    reboot_choice = input("Do you want to reboot? (yes/no): ")
    if reboot_choice.lower() == "yes" or reboot_choice.lower() == "y":
        print("Rebooting now")
        reboot_command = "sudo reboot"
        run_command(reboot_command)
    else:
        print("Reboot soon.")

