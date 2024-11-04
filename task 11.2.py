from datetime import datetime
today=datetime.today()
print(today)




dob=input("enter dob yy-mm-dd")
dob_split=dob.split('-')
today=datetime.now()
today_month=today.month
today_year=today.year
today_day=today.day
print(today_day)


years=today_year-int(dob_split[0])
months=today_month-int(dob_split[1])
days=today_day-int(dob_split[2])


if days < 0:
    months-= 1
    days+= 30  
if months< 0:
    years-= 1
    months+= 12