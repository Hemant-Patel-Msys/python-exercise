# 19. Write a function that takes two strings representing dates and returns the string
# that represents the earliest point in time ? Ex. get_earliest("01/27/1832",
# "01/27/1756") return '01/27/1756'.

from datetime import datetime
d1 = "01/27/1832"
d2 = "01/27/1756"




def earlist_year(d1,d2):
    d1 = d1.replace("/", ",")
    d2 = d2.replace("/", ",")
    d1 = datetime.strptime(d1, "%m,%d,%Y").date()
    d2 = datetime.strptime(d2, "%m,%d,%Y").date()
    a = min(d1,d2)
    return f"{a.month}\{a.day}\{a.year}"

print(earlist_year(d1,d2))


    