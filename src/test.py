import os
import sys
from trunic import Trunic

output_path = os.path.join(os.path.dirname(__file__), "..")

def view_trunic(trunic):
    f = open(os.path.join(output_path, "test.html"), "w+")
    f.write(
f"""<!DOCTYPE html>
<html>
  <head>
    <style>
      @font-face {{
        font-family: "Trunic";
        src: url("src/trunic.otf");
      }}

      p {{
        font-family: "Trunic";
        font-size: 100px;
      }}
    </style>
  </head>
  <body>
    <p>{trunic}</p>
  </body>
</html>
""")
    f.close()

a = Trunic(sys.argv[1])
print(a.to_string())
print(a.to_ipa())
print(a.encode())
view_trunic(a.encode())
# a.to_png(os.path.join(output_path), "out1", 200, "#000000", "#e2e2e2")
print()

# b = Trunic(sys.argv[2])
# print(b.to_string())
# print(b.to_ipa())
# print(b.encode())
# b.to_png(os.path.join(output_path), "out2", 45, "#000000", "#e2e2e2")
# print()

# c = Trunic(sys.argv[3])
# print(c.to_string())
# print(c.to_ipa())
# print(c.encode())
# c.to_png(os.path.join(output_path), "out3", 70, "#000000", "#e2e2e2")
