"""
prima cifra indica sexul si secolul
1, 2 = 1900, 1999
3, 4 = 1800, 1899
5, 6 = 2000, 2099
"""

cnp = list(input("Scrie primele 7 cifre din CNP: "))
print(cnp)

an_cnp_last_two = str(cnp[1]) + str(cnp[2])
last_two_digits = int(an_cnp_last_two)


if cnp[0] in ['1', '2']:  # 1900-1999
    an_cnp = 1900 + last_two_digits
    x = 2024 - an_cnp
    if x >= 18:
        print("ai peste 18 ani")
    elif x < 18:
        print("ai mai putin de 18 ani")
elif cnp[0] in ['3', '4']:  # 1800-1899
    an_cnp = 1800 + last_two_digits
    x = 2024 - an_cnp
    if x >= 18:
        print("ai peste 18 ani")
    elif x < 18:
        print("ai mai putin de 18 ani")
elif cnp[0] in ['5', '6']:  # 2000-2099
    an_cnp = 2000 + last_two_digits
    x = 2024 - an_cnp
    if x >= 18:
        print("ai peste 18 ani")
    elif x < 18:
        print("ai mai putin de 18 ani")


