import os
import subprocess
import time
import json  

# Function to execute shell commands
def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    return stdout.decode(), stderr.decode()

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
    api_key_command = f"curl -X POST 'http://213.239.193.208:9053/utils/hash/blake2b' -H 'accept: application/json' -H 'Content-Type: application/json' -d '\"{password}\"'"
    
    stdout, stderr = run_command(api_key_command)
    
    if "400 Bad Request" in stderr:
        print("Error: Bad Request")
        print("Response from the API:")
        print(stdout)
        return None
    
    return stdout.strip()  # Remove leading/trailing whitespaces


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
    
    print("Creating Node config file...")
    print(f"Public IP: {public_ip.strip()}")
    print(f"Node Name: {node_name}")
    print(f"API Hash: {api_key_hash}")
    
    print("Initializing Node...")
    
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
    print("\n\nErgo node setup complete. Run the system services script to automate node initialization.")
    print("\n\n")
        
