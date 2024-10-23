person={
    'name':"hazel",
    'age':22,
    'gender':'male',
    'location':['kiambu',518,'thika'],
    'address':{
        'street':'mthaiga',
        'city':'nairobi',
        'country':'kenya',
    }
}

print(type(person))
print(person['name'])
print(person['age'])
print(person['gender'])
print(person['location'][1])
print(person['address']['country'])
print(person['address']['city'])
print(person['address']['street'])
person['age']=40


print(person.keys())
print(person.values())
print(person.items())
person.pop('location')
print(person)
print(person.get('address'))