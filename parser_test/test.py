
from optparse import OptionParser 
parser = OptionParser() 
parser.add_option("-p", "--pdbk", action="store_true", 
                    dest="pdcl", 
                    default=False, 
                    help="write pdbk data to oracle db") 
parser.add_option("-z", "--zdbk", action="store_true", 
                    dest="zdcl", 
                    default=False, 
                    help="write zdbk data to oracle db") 

(options, args) = parser.parse_args() 

print options
print args

if options.pdcl==True: 
    print 'pdcl is true' 
if options.zdcl==True: 
     print 'zdcl is true' 
