# SSH and Firewall Hardening

## Objective

SSH access was restricted so that the Ubuntu Server accepts SSH connections only from the Kali Linux machine used in the lab.

## Firewall

UFW was enabled on Ubuntu Server.

The SSH rule allows connections only from the Kali lab IP:

```bash
sudo ufw allow from 192.168.56.10 to any port 22 proto tcp
```

The firewall was then enabled:

```bash
sudo ufw enable
```

The configuration was verified with:

```bash
sudo ufw status
```

## Verification

The SSH port was scanned again from Kali:

```bash
nmap -p 22 192.168.56.20
```

The result confirmed that SSH remained accessible from the authorized Kali machine.

## Security Improvement

Instead of allowing SSH access from any source, the firewall rule limits SSH access to the specific IP address used by the Kali machine in the isolated lab.

This reduces unnecessary network exposure while preserving the required administrative connection.
