foods =  ["pizza", "pasta", "french frise", "kabab", "sausage", "sandwich", "peperoni pizza"]
prices = [190000,   170000,  140000,         250000,  180000,    110000,     280000         ]
# foods2 = ['pizza', 'pizza', 'kabab', 'french frise', 'kabab']
print(foods)
food = input("what do you need? ")
i = food.index(food)
print(f"price is {prices[food]}")