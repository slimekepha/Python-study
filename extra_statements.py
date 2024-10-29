start_date = '2027-12-31'
end_date = '2024-12-31'
if start_date < end_date:
    print("Valid period")
elif start_date > end_date:
    print("Invalid period")
else:
    print("One-day period")



str1 = "Hello"
str2 = "World!"
if len(str1) > len(str2):
    print("str1 is longer")
elif len(str2) > len(str1):
    print("str2 is longer")
else:
    print("Both are of equal length")





valid_ids = [101, 102, 103]
user_id = 105 
if user_id in valid_ids== True:
    print("Access Granted")
else:
    print("Access Denied")

value="dope"
if isinstance(value,str):
    print("string detected")
elif isinstance(value,int):
    print("integer detected")
else:
    print("unknown type")


x = 8
y = 17
if x%2 == 0:
    if y % 2 == 0:
        print("x and y are both even")
    else:
        print("Only x is even")
else:
    if y%2 == 0:
        print("Only y is even")
    else:
        print("Neither x nor y are even")
