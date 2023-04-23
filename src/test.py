import sys
from trunic import Trunic


d = Trunic(sys.argv[1])
print(d.to_string())
print(d.to_ipa())
print(d.decode())
d.to_png("out", 200, (2000, 300), "#ffffff", "#000000")
