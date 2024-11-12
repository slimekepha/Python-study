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


word=input('enter word:')
print('original sting is', word)
size=len(word)
for i in range(0,size -1, 2):
    print("Index[",i,"]", word[i] )