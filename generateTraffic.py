from scapy.all import IP, TCP,  wrpcap
import random

packets = []

for i in range(200):
    pkt = IP(
        dst="192.168.1.1",
        src=f"192.168.1.{random.randint(2, 254)}"
    ) / TCP(
        dport=80,
        sport=random.randint(1024, 65535),
        flags="S"
    )

for burst in range(5):  # burst windows
    for i in range(50):  # high activity inside burst
        pkt = IP(
            src=f"10.0.0.{random.randint(1, 254)}",
            dst="192.168.1.1"
        ) / TCP(
            sport=random.randint(1024, 65535),
            dport=80,
            flags="S"
        )
        packets.append(pkt)

wrpcap("traffic.pcap", packets)

print("Synthetic traffic.pcap created (normal + anomaly)")