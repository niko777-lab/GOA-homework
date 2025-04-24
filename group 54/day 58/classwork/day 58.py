names = ["Anna", "Luka", "Mariam", "Alex", "Nino", "Sandro", "Dato", "Elene", "Giorgi", "Anano"]

renewed = [name for name in names if len(name) < 6 or name[0] == "A"]

print(renewed)

try:
    number = int(input("enter num: "))
    print("num entered is:", number)
except ValueError:
    print("error")
