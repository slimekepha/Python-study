fruits=["mangoes","banana","apples","watermelons","kiwis","dates"]

for fruit in fruits:
    if fruit =='banana':
        print(fruit)
        
#c=list(range(20,101))
#   print(num)


#for num in range(20,101):
 #   print(num)


num=list(range(20,110))
for i in num:
    if i%2==0:
        print(i)


num=list(range(20,110))
even_num=[]
for i in num:
    if i%2==0:
        even_num.append(i)
print(even_num)




numbers = list(range(1, 51))
print(numbers)

divisible_seven_5=[]
for num in numbers:
    if num%7==0 or num%5==0:
        divisible_seven_5.append(num)

print(divisible_seven_5)

range_values = list(range(10, 41))
range_sum = sum(range_values)
range_average = range_sum / len(range_values)
print(f"Sum: {range_sum}, Average: {range_average}")


odd_numbers = []
for num in range(11, 50, 2):
    odd_numbers.append(num)
    if len(odd_numbers) == 10:
        break

print(odd_numbers)


num=list(range(11,50,2))
odd_numbers=[]
for num in num:
    odd_numbers.append(num)
    if len(odd_numbers)==10:
        break

print(odd_numbers)


num=list(range(10,41))
sum=0
count=0
for i in num:
    sum=sum+i
average=sum/len(num)
print(sum)
print(average)


num=list(range(10,50))
odd_numbers=[ ]
count=0
for x in num:
    if x%2 !=0:
        odd_numbers.append(x)
        count+=1
        if count==10:
            break

print(odd_numbers)



number=int(input("Enter the number"))

for i in range(11):
    print(f"{number} x {i} = {number * i}")


count=0
for i in range(1,51):
    if i%2==0:
        count+=1
    
print(count)


ls1 = [("Jay", 20), ("Mo", 30), ("Mya", 32)]
total_quantity=0

for i in ls1:
    stock=i[1]
    total_quantity+=stock

print=(total_quantity)

