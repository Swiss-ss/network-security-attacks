# Network Security Attacks - Lab Assignment

## Overview
This repository contains implementation of three network security attacks
performed in a controlled lab environment for educational purposes.

## Lab Setup
- **Attacker:** Windows 11 (192.168.56.1)
- **Victim:** Ubuntu Server 24.04 VM (192.168.56.10)
- **Network:** VirtualBox Host-Only Network (isolated)
- **Tools:** Python 3.12, Scapy

## Attacks Implemented
| Attack | Description | Script |
|--------|-------------|--------|
| ARP Spoofing | MITM attack poisoning ARP cache | ARP-Spoofing/arp_spoof.py |
| DNS Poisoning | Redirecting DNS queries to attacker | DNS-Poisoning/dns_poison.py |
| SYN Flood | DoS attack flooding target with SYN packets | SYN-Flood/syn_flood.py |

## disclaimer
These attacks were performed in an isolated lab environment for
educational purposes only. Never perform these attacks on unauthorized networks.
