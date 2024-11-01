import random as rand

s = ['z', 'x', 'c']

print(rand.choices(s))
print(rand.choice(s))

random_int_list = [1 for _ in range(100)]
print(random_int_list)

random_int_list = [rand.randint(0, 100) for _ in range(100)]
print(random_int_list)

random_int_list = [i + 1 for i in range(100)]
print(random_int_list)

random_int_list = [i for i in range(101)]
print(random_int_list)





