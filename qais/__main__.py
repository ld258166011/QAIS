import sys
import argparse

from qais import QAIS

def main():
    parser = argparse.ArgumentParser(prog='qais', description='Query Automation in Incremental Search')
    parser.add_argument('website', type=str,
                        help='currently support Google, Tmall, Facebook, Baidu, Yahoo, Wikipedia, Csdn, Twitch, Bing.')
    parser.add_argument('query', type=str,
                        help='search query to be entered. Currently support English and Chinese.')
    parser.add_argument('--chinese', dest='chinese', action='store_true',
                        help='Chinese query entered using Pinyin IME.')
    parser.add_argument('--bigrams', type=str, metavar='PATH', default=None,
                        help='filename of the bigram timing model (csv format).')
    parser.add_argument('--browser', type=str, metavar='NAME', default='chrome',
                        help='currently support Chrome, Firefox, and Edge, default is Chrome.')
    parser.add_argument('--click', dest='click', action='store_true',
                        help='click the search box once before entering the query.')
    parser.add_argument('-i', type=str, metavar='IFACE', dest='iface', default=None,
                        help='the interface to capture the packets on.')
    parser.add_argument('-f', type=str, metavar='FILE', dest='fname', default='./pkts.pcap',
                        help='filename of the captured traffic, default is pkts.pcap.')

    if len(sys.argv) == 1:
        parser.print_help()
        
    else:
        args = parser.parse_args(sys.argv[1:])
        QAIS(**vars(args))

if __name__ == "__main__":
    main()
