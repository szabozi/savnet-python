import json
from produs import Produs
from operator import itemgetter


def get_validated_produs():
    produs = Produs()

    while True:
        categorie = input("Enter category (Haine, Accesorii, Incaltaminte): ")
        produs.set_categorie(categorie)
        if produs.validare_categorie():
            break
        else:
            print("Invalid category. Please try again.")

    # Validate and set product name
    while True:
        nume = input("Enter product name (letters only): ")
        produs.set_nume(nume)
        if produs.validare_nume():
            break
        else:
            print("Invalid name. Please use letters only.")

    # Validate and set price
    while True:
        try:
            pret = float(input("Enter price (positive number): "))
            produs.set_pret(pret)
            if produs.validare_pret():
                break
            else:
                print("Invalid price. Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Validate and set stock
    while True:
        try:
            stoc = int(input("Enter stock (non-negative integer): "))
            produs.set_stoc(stoc)
            if produs.validare_stoc():
                break
            else:
                print("Invalid stock. Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    return produs


def load_json_file(char):
    with open("produse.json", char) as file:
        json_data = json.load(file)
    return json_data


def dump_json_file(char, data):
    with open("produse.json", char) as file:
        json.dump(data, file, indent=2)


def save_produs_to_json(produs):
    product_data = produs.to_dict()
    data = load_json_file("r")
    data.append(product_data)
    dump_json_file('w', data)

    print('Product added!')


def print_all_products(name):
    product_data = load_json_file("r")

    for product in product_data:
        if product.get("categorie") == name:
            print(f'Produs: {product["produse"]}, Pret: {product["pret"]}, Stoc: {product["stoc"]}')


def sorted_products_by_category():
    product_data = load_json_file("r")

    # Sortam dupa categorie
    sorted_products = sorted(product_data, key=itemgetter("categorie"))

    for product in sorted_products:
        print(
            f'Categorie: {product["categorie"]}, Produs: {product["produse"]}, Pret: {product["pret"]} lei, Stoc: {product["stoc"]}')


"""
print('=' * 15)
print(category_key)
print('=' * 15)

print(product["produse"])
print(product["pret"])
print(product["stoc"])
print('-' * 15)
"""
