# Report
Barış Doğan 2521490 \
Okan Sağlam 2521904 \
Group 41 \
https://github.com/okan-saglam/covertovert \
In the homework, we first created an IP packet in the sender. We set its TTL value to 1. Then we added ICMP packet on top of the IP packet. Then we sent it to the receiver. We did not need to know the IP address of the receiver container since local docker DNS resolves the IP for us. In the sender, we listen packets using sniff method and we printed it by using show function. The critical point was to add filter to sniff method in order to listen packets only from the ICMP protocol and the sender. 
