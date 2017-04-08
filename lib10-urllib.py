import urllib
import re

response = urllib.urlopen("http://docs.python.org.ar/tutorial/3/stdlib.html")

f = open("tutorial.html", "w")

for line in response:
    print re.findall(r'href=".*"', line)
    f.write(line)

f.close()