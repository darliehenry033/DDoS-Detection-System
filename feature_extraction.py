from scapy.all import rdpcap, TCP

def extract_features(pcap_file):
  packets = rdpcap(pcap_file)
  packets_count = len(packets)
  sizes = [len(pkt) for pkt in packets]
  avg_packet_size = sum(sizes) /len(sizes) if sizes else 0

  syn_packets = 0
  for pkt in packets:
    if pkt.haslayer(TCP):
      if pkt[TCP].flags == "S":
        syn_packets += 1

  syn_ratio = syn_packets / packets_count if packets_count else 0

  return [packets_count, syn_ratio, avg_packet_size]
