import re
input= "<html> <param> </param>"
output= re.findall('<\/?[a-zA-Z]{5,}>', input)
print(str(output))
