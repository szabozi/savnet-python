the_list = [
    {"unit_price": 123.0, 'qty': 22},
    {"unit_price": 123.0, 'qty': 22},
    {"unit_price": 123.0, 'qty': 22}
]

print(the_list)

for list_item in the_list:
    list_item.update({
        'total_price': list_item['unit_price'] * list_item['qty']
    })

print(the_list)

the_list.sort(key=lambda item: item['unit_price'])

the_values_of_list = [item['unit_price'] for item in the_list]
print(the_values_of_list)



