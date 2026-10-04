# Wireshark Analysis

## Objective

Wireshark was used on the Kali Linux machine to capture and inspect SSH traffic between Kali and Ubuntu Server.

## Capture Configuration

- **Capture interface:** `eth1`
- **Kali IP:** `192.168.56.10`
- **Ubuntu IP:** `192.168.56.20`
- **Protocol:** SSH
- **Display filter:**

```text
tcp.port == 22
```

## Observations

The capture showed TCP traffic between the Kali and Ubuntu machines associated with the SSH connection.

The packets demonstrated the underlying TCP communication used to establish and maintain the SSH connection.

Because SSH encrypts application data, the captured packets do not expose the contents of the SSH session as readable plaintext.

## Exported Data

The relevant packets were exported from Wireshark as:

```text
ssh_packets.csv
```

The CSV data was subsequently processed with a Python script to summarize the captured traffic.

## Analysis

The Python analysis examined:

- Protocol distribution
- Source IP addresses
- Destination IP addresses

This provided a simple programmatic summary of the captured SSH traffic.
