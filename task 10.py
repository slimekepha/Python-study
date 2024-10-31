prods = [['omo', '30kshs', '300'], ['milk', '50kshs', '200'], ['bread', '45kshs', '359'], ['coffee', '5kshs', '79']]
total_stock = sum(int(prod[-1]) for prod in prods)
print(f"Total stock: {total_stock}")
