# Attack 3: SYN Flood

## What is SYN Flood?
SYN Flood is a Denial of Service (DoS) attack that exploits the TCP 
three-way handshake. The attacker sends a large number of SYN packets 
with fake source IPs, exhausting the victim's resources and making it 
unable to serve legitimate connections.

## How TCP Three-Way Handshake Works
Normal connection:
1. Client sends SYN
2. Server replies SYN-ACK
3. Client sends ACK → Connection established

During SYN Flood:
1. Attacker sends thousands of SYN packets with fake IPs
2. Server sends SYN-ACK to fake IPs (no response)
3. Server waits for ACK that never comes
4. Server's connection table fills up → Legitimate users can't connect

## Lab Setup
| Machine | IP | Role |
|---------|-----|------|
| Attacker (Windows) | 192.168.56.1 | Flood Source |
| Victim (Ubuntu VM) | 192.168.56.10 | Target (Port 80) |

## Tools Used
- Python 3.12
- Scapy library

## How to Run
```bash
pip install scapy
python syn_flood.py
```

## Expected Output
```
[*] Starting SYN Flood Attack!
[*] Target: 192.168.56.10:80
[*] Sent SYN packet #1 | Src: 181.126.115.34:21997 → 192.168.56.10:80
[*] Sent SYN packet #2 | Src: 240.250.70.226:22314 → 192.168.56.10:80
[*] Total SYN packets sent: 50
```

## Countermeasures
- Enable SYN cookies
- Use firewalls and rate limiting
- Use Intrusion Detection Systems (IDS)
- Use DDoS protection services
