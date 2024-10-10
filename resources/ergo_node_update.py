#!/usr/bin/env python3
import os
import sys
import subprocess
import json
import urllib.request

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

def get_current_ergo_version(node_path):
    # Assuming the JAR file is named as ergo-<version>.jar
    ergo_node_path = os.path.join(node_path, "ergo-node")
    try:
        files = os.listdir(ergo_node_path)
    except FileNotFoundError:
        return None
    for file in files:
        if file.startswith("ergo-") and file.endswith(".jar"):
            return file.replace("ergo-", "").replace(".jar", "")
    return None

def get_latest_ergo_version():
    print("[Info] Fetching the latest Ergo mainnet release version from GitHub...")
    try:
        url = "https://api.github.com/repos/ergoplatform/ergo/releases"
        with urllib.request.urlopen(url) as response:
            data = response.read()
            releases = json.loads(data.decode('utf-8'))

            for release in releases:
                # Skip pre-releases and drafts
                if not release['prerelease'] and not release['draft']:
                    version_tag = release['tag_name']
                    # Remove the leading 'v' if present
                    if version_tag.startswith('v'):
                        version_tag = version_tag[1:]
                    print(f"[Info] Latest mainnet release version: {version_tag}\n")
                    return version_tag
            print("[Error] No suitable mainnet release found.")
            sys.exit(1)
    except Exception as e:
        print(f"[Error] Failed to fetch the latest release version: {e}")
        sys.exit(1)

def update_ergo_node(node_path, new_version):
    ergo_node_path = os.path.join(node_path, "ergo-node")
    os.chdir(ergo_node_path)

    # Download the new Ergo JAR
    download_ergo_jar = f"wget -q https://github.com/ergoplatform/ergo/releases/download/v{new_version}/ergo-{new_version}.jar"
    print(f"[Info] Downloading Ergo Node version {new_version}...")
    run_command(download_ergo_jar)
    print(f"[Success] Ergo Node version {new_version} downloaded successfully.\n")

def update_systemd_service(node_path, new_version):
    service_file_path = "/etc/systemd/system/ergo-node.service"

    # Read the existing service file
    try:
        with open(service_file_path, "r") as service_file:
            service_contents = service_file.read()
    except Exception as e:
        print(f"\n[Error] Failed to read service file: {e}\n")
        sys.exit(1)

    # Replace the ExecStart line with the new version
    new_exec_start = f"ExecStart=/usr/bin/java -Xmx4g -jar {node_path}/ergo-node/ergo-{new_version}.jar --mainnet -c {node_path}/ergo-node/ergo.conf"
    service_lines = service_contents.splitlines()
    for i, line in enumerate(service_lines):
        if line.startswith("ExecStart="):
            service_lines[i] = new_exec_start
            break

    new_service_contents = "\n".join(service_lines)

    # Write the updated service file to a temporary location
    temp_service_file = os.path.join(ergo_node_path, 'ergo-node.service')
    try:
        with open(temp_service_file, "w") as service_file:
            service_file.write(new_service_contents)
        print(f"[Success] Updated service file created at {temp_service_file}")
    except Exception as e:
        print(f"\n[Error] Failed to write updated service file: {e}\n")
        sys.exit(1)

    # Move the updated service file to /etc/systemd/system/
    run_command(f"sudo mv {temp_service_file} {service_file_path}")
    run_command(f"sudo chmod 644 {service_file_path}")
    print(f"[Success] Service file updated at {service_file_path}\n")

def restart_ergo_node_service():
    print("[Info] Restarting Ergo Node service...")
    # Use the actual command instead of the alias
    run_command("sudo systemctl daemon-reload")
    run_command("sudo systemctl restart ergo-node.service")
    print("[Success] Ergo Node service restarted.\n")

def main():
    print("\n#############################################")
    print("#         Ergo Node Update Script           #")
    print("#############################################\n")

    print("Prerequisites:")
    print("- This script assumes that you have installed the Ergo node using 'ergo_node_setup.py'.")
    print("- The script manages the service directly using system commands.\n")

    # Get the user's home directory
    home_dir = os.path.expanduser("~")

    # Assume the node is installed in the user's home directory
    node_path = home_dir

    # Get the current Ergo version
    current_version = get_current_ergo_version(node_path)
    if not current_version:
        print("[Warning] Could not determine the current Ergo Node version.")
    else:
        print(f"[Info] Current Ergo Node version: {current_version}")

    # Get the latest Ergo version from GitHub
    latest_version = get_latest_ergo_version()

    # If current_version is known and equals latest_version, exit
    if current_version and current_version == latest_version:
        print("[Info] You are already running the latest Ergo Node version.")
        sys.exit(0)

    # Prompt user to confirm updating to the latest version, default to 'yes' on Enter
    if current_version:
        prompt_message = f"Do you want to update from version {current_version} to the latest version {latest_version}? ([yes]/no). Press Enter for default yes: "
    else:
        prompt_message = f"Do you want to install the latest Ergo Node version {latest_version}? ([yes]/no). Press Enter for default yes: "

    confirm = input(prompt_message).strip().lower()
    if confirm in ['no', 'n']:
        print("Update canceled.")
        sys.exit(0)

    # Perform the update
    update_ergo_node(node_path, latest_version)
    update_systemd_service(node_path, latest_version)

    # Restart the Ergo node service using the actual command
    restart_ergo_node_service()

    print("#############################################")
    print("#      Ergo Node Update Complete!           #")
    print("#############################################\n")

    print(f"[Success] Your Ergo Node has been updated to version {latest_version}.\n")

    # Suggest checking the status using the command
    print("You can check the status of your Ergo Node service using:")
    print("  systemctl status ergo-node.service\n")

if __name__ == "__main__":
    main()
