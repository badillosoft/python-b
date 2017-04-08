import sys

try:
    x = 1 / 0
except:
    sys.stderr.write("Error matematico\n")