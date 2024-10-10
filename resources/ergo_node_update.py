#!/usr/bin/env python3
import os
import sys
import subprocess

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

def get_current_ergo_version(node_path):
    # Assuming the JAR file is named as ergo-<version>.jar
    ergo_node_path = os.path.join(node_path, "ergo-node")
    files = os.listdir(ergo_node_path)
    for file in files:
        if file.startswith("ergo-") and file.endswith(".jar"):
            return file.replace("ergo-", "").replace(".jar", "")
    return None

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
    temp_service_file = os.path.join(os.getcwd(), 'ergo-node.service')
    try:
        with open(temp_service_file, "w") as service_file:
            service_file.write(new_service_contents)
        print(f"[Success] Updated service file created at {temp_service_file}")
    except Exception as e:
        print(f"\n[Error] Failed to write updated service file: {e}\n")
        sys.exit(1)

    # Move the updated service file to /etc/systemd/system/
    run_sudo_command(f"mv {temp_service_file} {service_file_path}")
    run_sudo_command(f"chmod 644 {service_file_path}")
    print(f"[Success] Service file updated at {service_file_path}\n")

def restart_ergo_node_service():
    print("[Info] Restarting Ergo Node service...")
    run_sudo_command("systemctl daemon-reload")
    run_sudo_command("systemctl restart ergo-node.service")
    print("[Success] Ergo Node service restarted.\n")

def main():
    print("\n#############################################")
    print("#         Ergo Node Update Script           #")
    print("#############################################\n")
    print("\nAssumes ergo_node_setup.py script has already been run.\n")

    # Get the user's home directory
    home_dir = os.path.expanduser("~")

    # Assume the node is installed in the user's home directory
    node_path = home_dir

    # Get the current Ergo version
    current_version = get_current_ergo_version(node_path)
    if not current_version:
        print("[Error] Could not determine the current Ergo Node version.")
        sys.exit(1)

    print(f"[Info] Current Ergo Node version: {current_version}")

    # Prompt user for the new Ergo version
    new_version_input = input(f"Enter the new Ergo version to install (current is {current_version}): ").strip()
    if not new_version_input:
        print("[Error] No version entered. Exiting.")
        sys.exit(1)
    new_version = new_version_input
    print(f"[Input] New Ergo version: {new_version}\n")

    if new_version == current_version:
        print("[Info] The new version is the same as the current version. No update needed.")
        sys.exit(0)

    # Confirm with the user
    confirm = input(f"Are you sure you want to update from version {current_version} to {new_version}? (yes/no): ").strip().lower()
    if confirm not in ['yes', 'y']:
        print("Update canceled.")
        sys.exit(0)

    # Perform the update
    update_ergo_node(node_path, new_version)
    update_systemd_service(node_path, new_version)
    restart_ergo_node_service()

    print("#############################################")
    print("#      Ergo Node Update Complete!           #")
    print("#############################################\n")

    print(f"[Success] Your Ergo Node has been updated to version {new_version}.\n")

if __name__ == "__main__":
    main()
