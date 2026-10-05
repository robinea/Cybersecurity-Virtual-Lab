# Baseline Reconnaissance

## Objective

The first scan was performed from Kali Linux to identify services exposed by the Ubuntu Server before firewall hardening.

## Tool

Nmap was used for service discovery and version detection.

```bash
nmap -sV 192.168.56.20
```

## Result

The scan identified SSH as an accessible service:

```text
22/tcp  open  ssh  OpenSSH
```

This established the baseline network exposure of the Ubuntu Server.

## SSH Verification

SSH access was tested from Kali:

```bash
ssh cyberlab@192.168.56.20
```

The connection succeeded, confirming that the SSH service was reachable from the Kali machine.

## Purpose of the Baseline

The baseline scan provides a point of comparison for the security configuration after firewall hardening.
