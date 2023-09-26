# Command Line Cheatsheet
The everyday commands you just can't live without. Meant to be a quick reference.


## Monitoring and Troubleshooting

### Systemd

====Common Troubleshooting and Monitoring====    
    
see what's running in systemd

```bash
systemctl --type=service --state=running
```

Edit the service file

```bash
sudo nano /etc/systemd/system/ergo-node.service
```

Reboot and run the service

```bash
sudo systemctl daemon-reload
sudo systemctl enable ergo-node.service
sudo systemctl start ergo-node.service
```

Check high level status

```bash
sudo systemctl status ergo-node
```

Stop the service to edit or troubleshoot
```bash
sudo systemctl stop ergo-node.service
```

See what the service is doing, or "journalling"

```bash
journalctl --unit=ergo-node --output=cat -f
```

### Memory & Storage

Check memory limits (like Control Panel) and status

```bash
htop
```

High level memory list
```bash
df -h
```

List block partitions
```bash
lsblk
```

Another list block paritions
```bash
sudo blkid
```

To find uuid upon boot up
```bash
ls -l /dev/disk/by-uuid
```

Remount a drive to be read-write
```bash
sudo su
#[type password]
mount -o remount, rw /
```

## Ergo Node Maintenance

Upgrade the node, here shown for version 5.0.14. Update the version!

Copy and paste this into a text file, edit the version, then c & p into terminal
```bash
wget https://github.com/ergoplatform/ergo/releases/download/v5.0.14/ergo-5.0.14.jar
```

Run the node not as a systemd
```bash
java -jar -Xmx2g ergo-5.0.14.jar --mainnet -c ergo.conf
```

Update the rpi for whatever reason

```bash
sudo apt update
sudo apt upgrade
```

reboot the pi
```bash
sudo reboot
```


## Networking

To find your public IP

```bash
curl icanhazip.com
```