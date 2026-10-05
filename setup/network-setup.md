# Network Setup

## Virtual Lab Network

The lab was created in VirtualBox using an isolated Internal Network named `CyberLab`.

### Kali Linux

- **Role:** Attacker and analysis machine
- **Interface:** `eth1`
- **IP address:** `192.168.56.10/24`

### Ubuntu Server

- **Role:** Target and server
- **Interface:** `enp0s8`
- **IP address:** `192.168.56.20/24`

Ubuntu Server also uses a separate NAT interface for normal network connectivity. The `CyberLab` interface is used for communication between the two virtual machines.

## Connectivity Test

Connectivity was verified from Kali using:

```bash
ping 192.168.56.20
```

The connection succeeded with no packet loss.

SSH connectivity was also verified using:

```bash
ssh cyberlab@192.168.56.20
```

The successful connection confirmed communication between the two machines over the isolated lab network.
