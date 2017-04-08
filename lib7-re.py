# regex => regular expressions

import re

print re.findall(r".+@.*\.\w{3}", "correo@gmail.com pepe@yahoo.com")