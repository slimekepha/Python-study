days = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
print(days[2])
print(len(days))
days_list = list(days)
days_list[3] = "Thur"
days = tuple(days_list)
print(days)

my_tuple=("age",14,'location',"kiambu",[100,300,500])
my_tuple[4][1]=1000
print(type(my_tuple))


