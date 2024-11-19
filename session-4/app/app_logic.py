import utils as utils


def main_meniu():
    print("\n\n\n==============================")
    print("========== OPTIUNI ==========")
    print("==============================\n\n\n")
    print("1. Categorii")
    print("2. Produse")
    print("3. Iesire")


def categori_menu():
    print("\n\n\n==============================")
    print("=========  CATEGORII =========")
    print("==============================\n\n\n")
    print("1. Haine")
    print("2. Accesorii")
    print("3. Incaltaminte")
    print("4. Revenire la main meniu.")


def product_menu():
    print("\n\n\n==============================")
    print("============  PRODUCTS =============")
    print("==============================\n\n\n")
    print("1. Add Product")
    print("2. Show products by categorii")
    print("3. Return to main meniu")


def user_input():
    return input("Alegeti optiune: ")


def start_categorie():
    categori_menu()
    categori_option = user_input()
    if categori_option == "1":  # haine
        print('Print all Categorie: Haine\n\n')
        utils.print_all_products("Haine")
        print('\n\n')
        press = input("Press 'enter' to continue...")
    elif categori_option == "2":  # accesorii
        print('Print all Categorie: Accesorii\n\n')
        utils.print_all_products("Accesorii")
        print('\n\n')
        press = input("Press 'enter' to continue...")
    elif categori_option == "3":  # incaltaminte
        print('Print all Ctegorie: Incaltaminte\n\n')
        utils.print_all_products("Incaltaminte")
        print('\n\n')
        press = input("Press 'enter' to continue...")
    elif categori_option == "4":  # revenire main meniu
        print('Returning to main meniu.\n\n')
        start()
    else:
        print('Invalid option..')

    start_categorie()


def start_produse():
    product_menu()
    product_option = user_input()
    if product_option == "1":  # add
        print('Adding products..\n\n')
        added_product = utils.get_validated_produs()
        utils.save_produs_to_json(added_product)
    elif product_option == "2":  # show products by categori
        print('Showing products by category..\n\n')
        utils.sorted_products_by_category()
        print('\n\n')
        press = input("Press 'enter' to continue...")
    elif product_option == "3":  # return to main meniu
        print('Returning to Main Meniu!\n\n')
        start()
    else:
        print('Invalid option..')

    start_produse()


def start():
    main_meniu()
    option = user_input()
    if option == "1":  # Categorii
        start_categorie()
    elif option == "2":  # Produse
        start_produse()
    elif option == "3":
        print('Iesire..')
        exit(1)
    else:
        print('Invalid option, returning to main meniu!')
        start()

