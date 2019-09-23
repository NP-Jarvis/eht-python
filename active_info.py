import nmap
import sys
from pprint import pprint
import time

nm_scan = nmap.PortScanner()   #initiating the scanner

print('\nRunning....\n')

nm_scanner = nm_scan.scan(sys.argv[1],'80',arguments='-O')  
# sys.argv[1] : will pass the ip address as command line arguement

'''
#result is gonna be a dict
pprint(nm_scanner)
'''
#accessing the data from dict

host_is_up = 'The host is: '+ nm_scanner['scan'][sys.argv[1]]['status']['state']+'.\n'
port_open = 'The port is: '+ nm_scanner['scan'][sys.argv[1]]['tcp'][80]['state']+'.\n'
method_scan = 'The method of scanning is: '+nm_scanner['scan'][sys.argv[1]]['tcp'][80]['reason']+'.\n'
guessed_os = 'There is %s chance that the host is running %s' %(nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['accuracy'],nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['name'])

#saving the data
with open('%s.txt'%sys.argv[1],'w') as f:
    f.write(host_is_up+port_open+method_scan+guessed_os)
    f.write('\n Report generated '+time.strftime('%Y-%m-%d_%H:%M:%S GMT', time.gmtime()))


print('\nFinished....')


