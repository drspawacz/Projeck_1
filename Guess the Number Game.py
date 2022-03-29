import random

name = input('Podaj swoje imie: ')
your_number = int(input('Zgadnij Numer: '))

bla = random.randint(1,10)


print(f"Numer to {bla}")

if __name__ == "__main__":
    if your_number == bla:
        print(f"wygrałeś {name}")
    else:
        print(f'przegrales {name}')