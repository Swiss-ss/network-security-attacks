\# Attack 1: ARP Spoofing



\## What is ARP Spoofing?

ARP (Address Resolution Protocol) Spoofing is a Man-in-the-Middle (MITM) 

attack where the attacker sends fake ARP messages to link their MAC address 

with the IP address of a legitimate device on the network.



\## How it Works

1\. Attacker sends fake ARP replies to both Victim and Gateway

2\. Victim's ARP cache gets poisoned — thinks Gateway's MAC is Attacker's MAC

3\. Gateway's ARP cache gets poisoned — thinks Victim's MAC is Attacker's MAC

4\. All traffic between Victim and Gateway now passes through Attacker



\## Lab Setup

| Machine | IP | MAC |

|---------|-----|-----|

| Attacker (Windows) | 192.168.56.1 | 0a:00:27:00:00:13 |

| Victim (Ubuntu VM) | 192.168.56.10 | 08:00:27:c4:a5:eb |



\## Tools Used

\- Python 3.12

\- Scapy library



\## How to Run

```bash

pip install scapy

python arp\_spoof.py

```



\## Expected Output

```

\[\*] Starting ARP Spoofing attack...

\[\*] Target: 192.168.56.10 (08:00:27:c4:a5:eb)

\[\*] Gateway: 192.168.56.1 (0a:00:27:00:00:13)

\[\*] Sent ARP spoof: Telling 192.168.56.10 that 192.168.56.1 is at our MAC

\[\*] Total Packets Sent: 2

```



\## Countermeasures

\- Use Dynamic ARP Inspection (DAI)

\- Use static ARP entries

\- Use VPNs and encrypted protocols

\- Use network monitoring tools like XArp

