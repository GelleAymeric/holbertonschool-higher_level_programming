#!/usr/bin/python3

if __name__ == "__main__":
    import sys

argv = sys.argv
num_argc = len(argv) - 1

if num_argc == 1:
    print("{} argument:" .format(num_argc, end=""))
elif num_argc == 0:
    print("0 arguments.")
else:
    print("{} arguments:".format(num_argc))

for i in range(num_argc):
    print("{}: {}".format(i + 1, sys.argv[i+1]))
