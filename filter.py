import sys
import string

printable = set(string.printable)
f = open(sys.argv[1], 'rw')
data = f.read()
newdata = filter(lambda x: x in printable, data)