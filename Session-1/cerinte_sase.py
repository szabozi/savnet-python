x = "Hello Python"
y = "Ana are mere"
z = "Pizza Party"

print(x.replace(" ", "_"))
print(y.replace(" ", "_"))
print(z.replace(" ", "_"))

print("----------------------")

print(x, end=".\n")
print(y, end=".\n")
print(z, end=".\n")

print("----------------------")
cuvinte_x = x.split()
primul_x = f"{cuvinte_x[0]} " * 3
print(f"{primul_x}{x}")

cuvinte_y = y.split()
primul_y = f"{cuvinte_y[0]} " * 3
print(f"{primul_y}{y}")

cuvinte_z = z.split()
primul_z = f"{cuvinte_z[0]} " * 3
print(f"{primul_z}{z}")

