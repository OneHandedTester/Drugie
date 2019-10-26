slowo = input("Wprowadź swoje słowo aby sprawdzić czy jest palidromem: ")
odwrocone = slowo [::-1]

if slowo==odwrocone:
    print("Podane słowo to palindrom.")
else:
    print("Podane słowo to nie palindrom.")
