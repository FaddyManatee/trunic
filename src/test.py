import os
import sys
from trunic import Trunic

output_path = os.path.join(os.path.dirname(__file__), "..")
print(output_path)
d = Trunic(sys.argv[1])
print(d.to_string())
print(d.to_ipa())
print(d.decode())
d.to_png(os.path.join(output_path), "out", 200, (2000, 230), "#000000", "#e2e2e2")
