import re
pattern = 'PYTHON'
if re.match(pattern,"PYTHON python django"):
    print("matched")
else:
    print("not found")