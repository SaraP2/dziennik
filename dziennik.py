class uczen:
    def __init__(self, imie, nazwisko, klasa, klasa_literka):
        #napisz konstruktor (imie nazwisko ....)
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa
        self.klasa_literka = klasa_literka
        self.przedmioty = dict()

    def dodaj_przedmiot(self, nazwa_przedmiotu):
        self.przedmioty[nazwa_przedmiotu] = list()

    def wstaw_ocene(self, nazwa_przedmiotu, ocena):
        # dla danego ucznia, wstaw do listy w slowniku ocene
        self.przedmioty[nazwa_przedmiotu].append(ocena)
#tu wyciagam element slownika ktory jest lista(.) po kropce dodaje do tej listy

    def policz_srednia_z_przedmiotu(self, nazwa_przedmiotu):
        #policz i zwroc ocene z danego przedmiotu
        # (jezeli nie ma ani jednej oceny zwroc false)

    def indentyfikator_ucznia(self):
        #zwroc string w postaci nazwisko_imie <- z malych liter

lista_uczniow = dict()

for i_ktory in range(1):
    imie = str(input("podaj imie:"))
    nazwisko = str(input("podaj nazwisko:"))
    klasa_nr = str(input("klasa_nr:"))
    klasa_literka = str(input("literka:"))
    nowy_uczen = uczen(imie, nazwisko, klasa_nr, klasa_literka)
    lista_uczniow[nowy_uczen.indentyfikator_ucznia()] = nowy_uczen

lista_uczniow["kowalski_piotr"]
lista_uczniow["kowalski_piotr"].wstaw_przedmiot("matematyka")

lista_uczniow["kowalski_piotr"].wstaw_ocene("matematyka", 4)
lista_uczniow["kowalski_piotr"].wstaw_ocene("matematyka", 2)
lista_uczniow["kowalski_piotr"].wstaw_ocene("matematyka", 1)
print(lista_uczniow["kowalski_piotr"].policz_srednia_z_przedmiotu("matematyka"))
