# Cybersecurity Virtual Lab — Final Report

## Overview

This project involved building an isolated cybersecurity laboratory using VirtualBox, Kali Linux, and Ubuntu Server.

The purpose was to practice network reconnaissance, SSH administration, packet capture, traffic analysis, and basic firewall hardening in a controlled environment.

## Lab Environment

The laboratory consisted of two virtual machines connected through an isolated VirtualBox Internal Network named `CyberLab`.

**Kali Linux**

- Role: Attacker and analysis machine
- IP address: `192.168.56.10`

**Ubuntu Server**

- Role: Target and server
- IP address: `192.168.56.20`

## Reconnaissance

Nmap was used to identify services exposed by the Ubuntu Server.

```bash
nmap -sV 192.168.56.20
```

The scan identified SSH on port 22.

This provided a baseline of the server's network exposure before hardening.

## SSH Testing

SSH connectivity was tested from Kali using:

```bash
ssh cyberlab@192.168.56.20
```

The successful connection confirmed that the two machines could communicate over the isolated laboratory network.

## Traffic Analysis

Wireshark was used to capture SSH traffic on the Kali machine.

The filter:

```text
tcp.port == 22
```

was used to isolate SSH-related traffic.

The captured packets demonstrated TCP communication between the Kali and Ubuntu machines. Since SSH encrypts application data, the contents of the session were not visible as readable plaintext.

## Firewall Hardening

UFW was enabled on Ubuntu Server and SSH access was restricted to the Kali laboratory IP address.

The rule used was:

```bash
sudo ufw allow from 192.168.56.10 to any port 22 proto tcp
```

The firewall configuration was then verified with:

```bash
sudo ufw status
```

A follow-up Nmap scan was performed from Kali to verify SSH accessibility.

## Python Analysis

The exported Wireshark packet data was saved as `ssh_packets.csv`.

A Python script was created to analyze the exported data and summarize:

- Protocols
- Source IP addresses
- Destination IP addresses

This connected the packet capture stage with basic programmatic analysis.

## Skills Demonstrated

This project provided practical experience with:

- Linux system administration
- Virtual machine networking
- Nmap reconnaissance
- SSH
- UFW firewall configuration
- Wireshark packet capture
- Python data processing
- Basic network security analysis

## Conclusion

The project demonstrated a complete basic security workflow: establishing an isolated environment, identifying network exposure, observing traffic, applying a defensive control, and analyzing captured data.

The laboratory was intentionally kept isolated so that all testing could be performed safely on systems controlled by the project owner.
