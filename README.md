# Cybersecurity Virtual Lab

An isolated VirtualBox cybersecurity lab built with Kali Linux and Ubuntu Server to practice network reconnaissance, SSH traffic analysis, packet capture, and firewall hardening.

## Lab Architecture

- **Kali Linux** — attacker and analysis machine
- **Ubuntu Server** — target/server
- **VirtualBox Internal Network** — `CyberLab`
- **Kali IP** — `192.168.56.10`
- **Ubuntu IP** — `192.168.56.20`

## Security Workflow

1. Configured an isolated virtual network.
2. Performed baseline network reconnaissance with Nmap.
3. Configured and tested SSH access.
4. Captured SSH traffic with Wireshark.
5. Hardened SSH access using UFW.
6. Exported packet data from Wireshark.
7. Analyzed the packet data with Python.

## Tools

- Kali Linux
- Ubuntu Server
- VirtualBox
- Nmap
- Wireshark
- OpenSSH
- UFW
- Python

## Project Structure

```text
Cybersecurity-Virtual-Lab/
├── README.md
├── setup/
├── reconnaissance/
├── hardening/
├── analysis/
├── evidence/
└── report/
```

## Key Findings

The baseline scan identified SSH as an accessible service on the Ubuntu server. SSH traffic was then captured and examined with Wireshark. UFW was configured to restrict SSH access to the designated Kali lab address.

## Purpose

This project demonstrates practical experience with network reconnaissance, Linux administration, traffic analysis, and basic defensive security in a controlled environment.
