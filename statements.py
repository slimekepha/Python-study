if 20>40:
    print('20 is greater')
else:
    print('20 is less than')


marks=20
if marks>50:
    print('pass')
else:
    print('fail')
num=11
if num%2==0:
    print('even')
else:
    print('odd')

marks=int(input('enter marks:'))
if marks>=90 and marks<=100:
    print('A')
elif marks>=80 and marks<=90:
    print('B')
elif marks>=70 and marks<=80:
    print('C')
elif marks>=60 and marks<=70:
    input('D')
elif marks>=50 and marks<=60:
    input('E')
else:
    print('fail')



age=int(input('enter age:'))
if age>=60:
    print('you are an older')
elif age>=18 and age<60:
    print(' you are adult')
else:
    print('You are a minor')


purchase=int(input('enter purchase:'))
if purchase>1000:
    print('100 discount')
    if purchase>5000:
        print('200 discount')
else:
    print('no discount')

age=int(input('enter your age:'))
license=True
if age>=18:
    license=input('do you have a license yes/no:').lower().strip()
    if license=='yes':
        print('you are eligible to drive')
    else:
        print('not eligible to drive')
else:
    print('you are too young')




credit_score = int(input("Enter your credit score: "))
annual_income = int(input("Enter your annual income in dollars: "))
if credit_score >700:
    if annual_income >50000:
        print("Loan approved.")
    else:
        print("Income requirement not met.")
else:
    print("Credit score too low.")
