from datetime import datetime
import random
def meetup_date(year,month):
    if month in [4,6,9,11]:
        date = random.randint(1,30)
    elif month in [1,3,5,7,8,10,12]:
        date = random.randint(1,31)
    else:
        date = random.randint(1,29)

    a = f'{year},{month},{date}'
    return datetime.strptime(a,"%Y,%m,%d").date()

a = meetup_date(2012, 3)
print(a)