s = "ceva"

print(s.center(20, "*"))


print(("*" * 1).center(20, " "))
print(("*" * 3).center(20, " "))
print(("*" * 5).center(20, " "))
print(("*" * 7).center(20, " "))

layers = [7, 5, 3, 1]
for layer in layers:
    print(("*" * layer).center(20, " "))

