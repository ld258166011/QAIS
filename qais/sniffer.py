import threading
from scapy.all import sniff, wrpcap, send
from scapy.layers.inet import IP, TCP


class Sniffer:
    '''
    Sniff network traffic and save packets.
    '''

    def start(self, iface, fname):
        '''
        Start sniffing in a new thread.
        '''
        thread = threading.Thread(target=self._sniff, args=[iface, fname, ])
        thread.start()


    def _sniff(self, iface, fname):
        '''
        Sniff HTTPS packets and save as pcap.
        '''
        filter_rule = 'tcp port 443'
        stop_filter = lambda x:x.haslayer(IP) and x[IP].ttl==1
        pkts = sniff(iface=iface, filter=filter_rule, stop_filter=stop_filter)
        wrpcap(fname, pkts)


    def stop(self, iface):
        '''
        Stop sniffing by sending stop flag packet.
        '''
        stop_pkt = IP(ttl=1)/TCP(dport=443)
        send(stop_pkt, iface=iface, verbose=False)
