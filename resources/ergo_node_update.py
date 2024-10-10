#!/usr/bin/env python3
"""
Ergo Node Update Script
-----------------------

This script automates the process of updating your Ergo Node to the latest mainnet release.
It performs the following tasks:

1. Determines the current version of the Ergo Node installed.
2. Fetches the latest mainnet release version from the Ergo GitHub repository.
3. Compares the current version with the latest version.
   - If already running the latest version, it provides proofs and exits.
4. Prompts the user to confirm updating to the latest version.
5. Downloads the latest Ergo Node JAR file.
6. Updates the systemd service file to point to the new JAR version throughout the file.
7. Restarts the Ergo Node service to apply the changes.
8. Checks the logs to confirm the node is running the expected version.
9. Provides confirmation and instructions to verify the update.

Prerequisites:

- The script assumes that you have installed the Ergo Node using 'ergo_node_setup.py'.
- The node should be installed in the default directory: '~/ergo-node'.
- You must have sudo privileges to move files and restart services.
"""

# Import necessary modules for the script
import os                   # For interacting with the operating system
import sys                  # For system-specific parameters and functions
import subprocess           # For running shell commands
import json                 # For parsing JSON data
import urllib.request       # For making HTTP requests
import re                   # For regular expressions (pattern matching)

def run_command(command, capture_output=True):
    """
    Executes a shell command and handles errors.

    Parameters:
    - command (str): The shell command to execute.
    - capture_output (bool): Whether to capture and return the command's output.

    Returns:
    - str: The command's output if capture_output is True.

    If the command fails, the script prints an error message and exits.
    """
    try:
        # Run the shell command
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE if capture_output else None,  # Capture stdout if required
            stderr=subprocess.PIPE if capture_output else None,  # Capture stderr if required
            shell=True,          # Execute the command in the shell
            check=True,          # Raise an exception if the command exits with a non-zero status
            text=True            # Return output as a string (text), not bytes
        )
        if capture_output:
            # Return the command's output, stripped of leading/trailing whitespace
            return result.stdout.strip()
        return ""
    except subprocess.CalledProcessError as e:
        # Handle errors if the command fails
        print(f"\n[Error] Command failed: {command}")
        if capture_output:
            # Print the error output from the command
            print(f"[Error] Error Output: {e.stderr.strip()}\n")
        else:
            # Inform the user that the command exited with a non-zero status
            print(f"[Error] Command exited with non-zero status.\n")
        # Exit the script with an error code
        sys.exit(1)

def get_current_ergo_version(node_path):
    """
    Determines the current version of the Ergo Node installed.

    Parameters:
    - node_path (str): The path to the Ergo Node installation directory.

    Returns:
    - str or None: The current version as a string if found, otherwise None.
    """
    try:
        # List all files in the node installation directory
        files = os.listdir(node_path)
    except FileNotFoundError:
        # Return None if the directory is not found
        return None
    # Iterate over the files to find the JAR file
    for file in files:
        # Look for files that start with 'ergo-' and end with '.jar'
        if file.startswith("ergo-") and file.endswith(".jar"):
            # Extract and return the version number from the file name
            return file.replace("ergo-", "").replace(".jar", "")
    # Return None if no matching JAR file is found
    return None

def get_latest_ergo_version():
    """
    Fetches the latest mainnet release version of the Ergo Node from GitHub.

    Returns:
    - str: The latest version as a string.

    If it fails to fetch the version, the script prints an error message and exits.
    """
    print("[Info] Fetching the latest Ergo mainnet release version from GitHub...")
    try:
        # GitHub API URL for Ergo releases
        url = "https://api.github.com/repos/ergoplatform/ergo/releases"
        # Open the URL and read the response
        with urllib.request.urlopen(url) as response:
            data = response.read()
            # Parse the JSON data
            releases = json.loads(data.decode('utf-8'))

            # Iterate over the releases
            for release in releases:
                # Skip pre-releases and drafts
                if not release['prerelease'] and not release['draft']:
                    # Get the tag name (version) of the release
                    version_tag = release['tag_name']
                    # Remove the leading 'v' if present (e.g., 'v5.0.23' becomes '5.0.23')
                    if version_tag.startswith('v'):
                        version_tag = version_tag[1:]
                    print(f"[Info] Latest mainnet release version: {version_tag}\n")
                    # Return the latest version found
                    return version_tag
        # If no suitable release is found, print an error and exit
        print("[Error] No suitable mainnet release found.")
        sys.exit(1)
    except Exception as e:
        # Handle exceptions during the HTTP request or JSON parsing
        print(f"[Error] Failed to fetch the latest release version: {e}")
        sys.exit(1)

def update_ergo_node(node_path, new_version):
    """
    Downloads the latest Ergo Node JAR file.

    Parameters:
    - node_path (str): The path to the Ergo Node installation directory.
    - new_version (str): The new version to download.

    If the download fails, the script prints an error message and exits.
    """
    # Change the current working directory to the node installation directory
    os.chdir(node_path)

    # Construct the download command using wget
    download_ergo_jar = f"wget -q https://github.com/ergoplatform/ergo/releases/download/v{new_version}/ergo-{new_version}.jar"
    print(f"[Info] Downloading Ergo Node version {new_version}...")
    # Execute the download command
    run_command(download_ergo_jar)
    print(f"[Success] Ergo Node version {new_version} downloaded successfully.\n")

def update_systemd_service(node_path, current_version, new_version):
    """
    Updates the systemd service file to point to the new JAR version throughout the file.

    Parameters:
    - node_path (str): The path to the Ergo Node installation directory.
    - current_version (str or None): The current version installed.
    - new_version (str): The new version to update to.

    If updating the service file fails, the script prints an error message and exits.
    """
    # Path to the systemd service file
    service_file_path = "/etc/systemd/system/ergo-node.service"

    # Read the existing service file
    try:
        with open(service_file_path, "r") as service_file:
            # Read the entire content of the service file
            service_contents = service_file.read()
    except Exception as e:
        # Handle exceptions if the file cannot be read
        print(f"\n[Error] Failed to read service file: {e}\n")
        sys.exit(1)

    # Define a regular expression pattern to match the old JAR file name
    # This pattern matches 'ergo-<version>.jar', where <version> consists of digits and dots
    old_jar_pattern = r'ergo-\d+\.\d+\.\d+\.jar'

    # Define the new JAR file name using the new version
    new_jar = f'ergo-{new_version}.jar'

    # Replace all occurrences of the old JAR file name with the new one in the service file content
    updated_service_contents = re.sub(old_jar_pattern, new_jar, service_contents)

    # Write the updated service file to a temporary location in the node installation directory
    temp_service_file = os.path.join(node_path, 'ergo-node.service')
    try:
        with open(temp_service_file, "w") as service_file:
            # Write the updated service content to the temporary file
            service_file.write(updated_service_contents)
        print(f"[Success] Updated service file created at {temp_service_file}")
    except Exception as e:
        # Handle exceptions if the file cannot be written
        print(f"\n[Error] Failed to write updated service file: {e}\n")
        sys.exit(1)

    # Move the updated service file to the systemd directory
    run_command(f"sudo mv {temp_service_file} {service_file_path}")
    # Set the correct permissions for the service file
    run_command(f"sudo chmod 644 {service_file_path}")
    print(f"[Success] Service file updated at {service_file_path}\n")

def restart_ergo_node_service():
    """
    Restarts the Ergo Node service using systemd.

    If restarting the service fails, the script prints an error message and exits.
    """
    print("[Info] Restarting Ergo Node service...")
    # Reload the systemd daemon to recognize changes
    run_command("sudo systemctl daemon-reload")
    # Restart the Ergo Node service
    run_command("sudo systemctl restart ergo-node.service")
    print("[Success] Ergo Node service restarted.\n")

def check_node_version_in_logs(version):
    """
    Checks the Ergo Node logs to confirm it's running the expected version.

    Parameters:
    - version (str): The version to check for in the logs.

    If the version is found in the logs, it prints a confirmation message.
    Otherwise, it prints a warning.
    """
    print("\n[Info] Checking the Ergo Node logs for version information...")
    try:
        # Construct the command to search the logs for the version
        # This command searches for lines containing 'Version: <version>'
        log_output = run_command(f"sudo journalctl -u ergo-node.service | grep -E 'Version:? {version}' | tail -1")
        if version in log_output:
            # If the version is found in the logs, print a proof message
            print(f"[Proof] Ergo Node is running version {version} as per logs.")
        else:
            # If the version is not found, print a warning with the last matching log entry
            print(f"[Warning] Could not confirm the node version from the logs. Last version in logs: {log_output}")
    except Exception as e:
        # Handle exceptions if the log check fails
        print(f"\n[Error] Failed to check logs: {e}\n")

def main():
    """
    The main function orchestrates the update process.

    It performs the following steps:
    - Prints the script header and prerequisites.
    - Determines the node installation path.
    - Gets the current and latest Ergo Node versions.
    - Compares versions and prompts for update if necessary.
    - Performs the update and restarts the service.
    - Checks the logs to confirm the node is running the expected version.
    """
    # Print the script header
    print("\n#############################################")
    print("#         Ergo Node Update Script           #")
    print("#############################################\n")

    # Print prerequisites
    print("Prerequisites:")
    print("- This script assumes that you have installed the Ergo Node using 'ergo_node_setup.py'.")
    print("- The script manages the service directly using system commands.\n")

    # Get the user's home directory (e.g., '/home/username')
    home_dir = os.path.expanduser("~")

    # Define the node installation directory (default: '~/ergo-node')
    node_path = os.path.join(home_dir, "ergo-node")

    # Get the current Ergo Node version installed
    current_version = get_current_ergo_version(node_path)
    if not current_version:
        # If the version cannot be determined, print a warning
        print("[Warning] Could not determine the current Ergo Node version.")
    else:
        # Print the current version
        print(f"[Info] Current Ergo Node version: {current_version}")

    # Get the latest Ergo Node version from GitHub
    latest_version = get_latest_ergo_version()

    # Check if the current version is known and matches the latest version
    if current_version and current_version == latest_version:
        print("[Info] You are already running the latest Ergo Node version.")
        # Provide proofs to confirm the node is up-to-date

        # Print the current version detected from the JAR file
        print("\n[Proof] Current Ergo Node version detected from JAR file: {}".format(current_version))

        # Verify that the systemd service file points to the correct JAR version
        service_file_path = "/etc/systemd/system/ergo-node.service"
        try:
            with open(service_file_path, "r") as service_file:
                # Read the service file content
                service_contents = service_file.read()
            if f"ergo-{current_version}.jar" in service_contents:
                # If the service file points to the correct JAR version, print a proof message
                print("[Proof] Systemd service file points to the correct JAR version.")
            else:
                # If not, print a warning
                print("[Warning] Systemd service file does not point to the expected JAR version.")
            # Indicate that the service file has been checked
            print("[Proof] Service file checked: {}".format(service_file_path))
        except Exception as e:
            # Handle exceptions if the service file cannot be read
            print(f"\n[Error] Failed to read service file: {e}\n")

        # Check the status of the Ergo Node service
        print("\n[Info] Checking the status of the Ergo Node service...")
        run_command("systemctl status ergo-node.service", capture_output=False)

        # Check the logs to confirm the node is running the expected version
        check_node_version_in_logs(current_version)

        # Exit the script since the node is already up-to-date
        sys.exit(0)

    # Prompt the user to confirm updating to the latest version
    if current_version:
        # If the current version is known, include it in the prompt
        prompt_message = f"Do you want to update from version {current_version} to the latest version {latest_version}? ([yes]/no). Press Enter for default yes: "
    else:
        # If the current version is unknown, adjust the prompt accordingly
        prompt_message = f"Do you want to install the latest Ergo Node version {latest_version}? ([yes]/no). Press Enter for default yes: "

    # Get the user's input and convert it to lowercase
    confirm = input(prompt_message).strip().lower()
    if confirm in ['no', 'n']:
        # If the user answers 'no', cancel the update and exit
        print("Update canceled.")
        sys.exit(0)

    # Proceed to perform the update
    update_ergo_node(node_path, latest_version)
    update_systemd_service(node_path, current_version, latest_version)

    # Restart the Ergo Node service to apply the changes
    restart_ergo_node_service()

    # Check the logs to confirm the node is running the new version
    check_node_version_in_logs(latest_version)

    # Print the update completion message
    print("#############################################")
    print("#      Ergo Node Update Complete!           #")
    print("#############################################\n")

    print(f"[Success] Your Ergo Node has been updated to version {latest_version}.\n")

    # Provide instructions to check the service status
    print("You can check the status of your Ergo Node service using:")
    print("  systemctl status ergo-node.service\n")

# Entry point of the script
if __name__ == "__main__":
    main()
