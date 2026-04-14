from scapy.all import rdpcap, sniff, TCP
import os


def sniff_test():
    print("Sniffing test...")

    packets = sniff(count=1)

    if packets and len(packets) > 0:
        print("Success: Packet captured")
    else:
        print("Failed to capture packet")


def extract_features(pcap_file):

    if not os.path.exists(pcap_file):
        raise FileNotFoundError(f"PCAP file not found: {pcap_file}")

    packets = rdpcap(pcap_file)

    packets_count = len(packets)

    sizes = [len(pkt) for pkt in packets]
    avg_packet_size = sum(sizes) / len(sizes) if sizes else 0

    syn_packets = 0

    for pkt in packets:
        if pkt.haslayer(TCP):
            # Better SYN detection (correct bit check)
            if pkt[TCP].flags & 0x02:   # SYN flag
                syn_packets += 1

    syn_ratio = syn_packets / packets_count if packets_count else 0

    return [packets_count, syn_ratio, avg_packet_size]



if __name__ == "__main__":
    sniff_test()