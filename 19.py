import datetime

dt_Str = "2020-01-15 09:03:32.744178"

get_year = lambda x:x.year
get_month = lambda x:x.month
get_day = lambda x:x.day
get_time = lambda x:x.time()


dt_obj = datetime.datetime.strptime(dt_Str,"%Y-%m-%d %H:%M:%S.%f")

year = get_year(dt_obj)
month = get_month(dt_obj)
day = get_day(dt_obj)
time = get_time(dt_obj)



print("Year: ",year)
print("Month: ",month)
print("Date: ",day)
print("Time: ",time)

