length = int(input('Length: '))
even_numbers_list = filter(lambda i: i % 2 == 0, range(int(length)))

print(list(even_numbers_list))

