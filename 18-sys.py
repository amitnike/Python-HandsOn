import sys

#pass the arugment while running the code, if not passed it will give error if we try to get 1
#argv[0]..is the name of program
"""
try:
    print("hello,my name is ",sys.argv[1])
except IndexError:
    print("Too few arguments")
"""
"""
if len(sys.argv) < 2:
    print("Too few args")
elif len(sys.argv) > 2:
    print("Too many args")
else:
    print("hello,my name is ",sys.argv[1])
# if argv is sent as "complete string", it will be considered as a single string
"""
"""
# sys exit will cause to termniate once error condition is satisfied, code not executed further
if len(sys.argv) < 2:
    sys.exit("Too few args")
elif len(sys.argv) > 2:
    sys.exit("Too many args")

print("hello,my name is ",sys.argv[1])
"""

if len(sys.argv) < 2:
    sys.exit("Too few args")
#slice the argument list from 1st item to last using 1:
# start end can be given as 1:3 to get 1st and 2nd item only
# end can be left blank to get all items from start to end of list
# end can be given as -1 to get all items except last item
for arg in sys.argv[1:]:
    print("Hello, nam is ", arg)