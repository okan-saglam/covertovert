import scapy.all as scapy



# Implement your ICMP receiver here
scapy.sniff(count = 1, filter = "icmp and host sender", prn = lambda x: x.show())
