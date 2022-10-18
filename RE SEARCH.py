import re
pattern = 'PYTHON'

if re.search(pattern,"PYTHON python django, AM HTML PYTHON"):
    print("matched")
else:
    print("not matched")

