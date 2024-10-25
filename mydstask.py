my_ds = [23, "Jane", 560, ["Lesson", "Maths", {"currency": "KES"}], 987, (76, "John")]
print(my_ds[3][2]["currency"])
print(my_ds[2])
print(my_ds[3][1])
my_ds[3][2]["amount"] = 90
print(my_ds[3][2])
num = 987
reversed_num = int(str(num)[::-1])
print(reversed_num)
my_ds[5] = (76, "Jane")
print(my_ds)

my_ds[5]=list(my_ds[5])
my_ds[5][1]="jane"
my_ds[5]=tuple(my_ds[5])
print(my_ds)