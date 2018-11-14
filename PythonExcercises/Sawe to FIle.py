def zapis_do_pliku(nazwa, dane):
    with open(nazwa, 'w') as pliktxt:
        dane=str(dane)
        pliktxt.write(dane)
def odczyt_z_pliku(nazwa):
    with open(nazwa, 'r') as pliktxt:
        return pliktxt.read()
B=''
A=input('chcesz zapisać czy odczytać?')
if A=='zapisać':

    liczby=[1,2,3,4,5]
    zapis_do_pliku(input('podaj nazwę pliku txt'), liczby)
elif A=='odczytać':
    B=odczyt_z_pliku(input('podaj nazwę pliku'))
else:
    print('nie znam takiego słowa XD')
print(B)