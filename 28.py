import re
data = ["example (.com)", "MSys", "github (.com)", "keka (.com)"]
for i in data:
    a = re.sub('(.com)'," ",i).replace("( )"," ")
    print(a)