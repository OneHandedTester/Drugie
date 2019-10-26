# Robię listę cyfr i oddzielam spacjami
txt = "16 45 78 96 55 78 58 69 74"
# Używam funkcji split - moja lista
x = txt.split(" ")
print (x)
print (type (x))

# Używam funkcji "tuple" - krotka, żeby zmienić typ z listy na krotki
y = tuple(x)
print (y)
print (type (y))
