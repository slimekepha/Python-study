def multiply(num1,num2):
    product=num1*num2
    if product<=1000:
        return product
    else:
        return num1+num2

result=multiply(70,100)
print(f"The result is {result}")




previous_num = 0
for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    previous_num = i


# word=input('enter word:')
# print('original sting is', word)
# size=len(word)
# for i in range(0,size -1, 2):
#     print("Index[",i,"]", word[i] )


word=input("enter the word:")
print("Original string is",word)
x=list(word)
for i in x[0::2]:
    print(i)


x=[10,20,3,3,45,60,30]
for i in x:
    if i%5==0:
        print(i)


def first_last_same(numberlist):
    first_num=numberlist[0]

    second_num=numberlist[-1]
    if first_num==second_num:
        return True
    else:
        return False
numx=[20,20,30,20]
print("result is:",first_last_same(numx))




for i in range(7,0,-1):
    for j in range(0,i-1):
        print("*",end='')
    print("")


def person(name,age):
    print(name,age)

person("Hazel",40)



fruits=["apples","kiwis","bananas","passions","mangoes"]
fruit_tuple=tuple(fruits)
fruits.append("avocados")
print(fruits)
print(fruit_tuple)