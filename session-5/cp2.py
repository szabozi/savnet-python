number_of_input = input("Enter number: ")


def power_of(n):
    return lambda b: b ** n


map_of_input = map(lambda range_index: int(number_of_input) ** range_index, range(10))

for i in map_of_input:
    print(i)
