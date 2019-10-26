litera_imie = input("Twoja pierwsza litera imienia to: ")
nazwisko = input("Twoje nazwisko to: ")
twoje_dane = litera_imie.upper()+"."+nazwisko.upper ()

Poczatek_roku = input(twoje_dane+" "+"podaj dwie pierwsze cyfry aktualnego roku: ")
Koniec_roku = input(twoje_dane+" "+"podaj dwie ostatnie cyfry aktualnego roku: ")
Ile_lat = input(twoje_dane+" "+"Jaki jest twój rok urodzenia?"+" ")
Rok = int(Poczatek_roku + Koniec_roku)
Cos = int(Ile_lat)
Rok2 = Rok - Cos

print (twoje_dane+" "+"masz "+str(Rok2)+" "+"lat!")
