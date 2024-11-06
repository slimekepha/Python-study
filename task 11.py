dob=input("Enter the date of birth (YY-MM-DD):")
dob_2 = dob.split('-')
birth_year=int(dob_2[0])
birth_month=int(dob_2[1])
birth_day=int(dob_2[2])

currentdate=input("Enter the current date (YY-MM-DD):")
currentdate2=currentdate.split("-")
current_year=int(currentdate2[0])
current_month=int(currentdate2[1])
current_day=int(currentdate2[2])


age_year=current_year-birth_year
age_month=current_month-birth_month
age_day=current_day-birth_day


if age_day < 0:
    age_month -= 1
    age_day+= 30  
if age_month < 0:
    age_year -= 1
    age_month += 12

print(f"You are {age_year}years, {age_month} months, {age_day}days")




