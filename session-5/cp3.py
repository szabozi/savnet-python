def standardize_name(name):
    return name.strip().lower()


user_inputs = [" Alice", "BOB ", "Charlie"]
new_name = list(map(standardize_name, user_inputs))

print(new_name)
