import re
pattern="[0-10][a-z][A-Z]"
if re.search(pattern, "1bB"):
    print("ok")
else:
    print("error")
