"""
Luati input de la utilizator un numar si parcurgeti intervalul de la 0 pana la numarul introdus de catre utilizator,
afisand toate numerele pare.
"""


numar = int(input("Introduceți un număr: "))

print("Numerele pare sunt:")
for i in range(numar + 1):
    if i % 2 == 0:
        print(i)
