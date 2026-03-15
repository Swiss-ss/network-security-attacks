# Attack 2: DNS Poisoning

## What is DNS Poisoning?
DNS Poisoning (also called DNS Spoofing) is an attack where the attacker 
intercepts DNS queries and sends fake DNS responses, redirecting victims 
to malicious IP addresses instead of legitimate ones.

## How it Works
1. Victim sends a DNS query to resolve a domain (e.g. google.com)
2. Attacker intercepts the DNS query
3. Attacker sends a fake DNS response with attacker's IP
4. Victim connects to attacker's machine instead of real website

## Lab Setup
| Machine | IP | Role |
|---------|-----|------|
| Attacker (Windows) | 192.168.56.1 | DNS Interceptor |
| Victim (Ubuntu VM) | 192.168.56.10 | DNS Client |

## Tools Used
- Python 3.12
- Scapy library

## How to Run
```bash
pip install scapy
python dns_poison.py
```

## Expected Output
```
[*] Starting DNS Poisoning attack...
[*] Redirecting all DNS queries to: 192.168.56.1
[*] Listening for DNS queries...
[*] Intercepted DNS query for: google.com.
[*] Poisoned! Redirected google.com. to 192.168.56.1
```

## Countermeasures
- Use DNSSEC (DNS Security Extensions)
- Use encrypted DNS (DNS over HTTPS/TLS)
- Use trusted DNS servers
- Monitor DNS traffic for anomalies
