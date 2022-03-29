import random

name = input('Podaj swoje imie: ')
your_number = int(input('Zgadnij Numer: '))

bla = random.randint(1,10)


print(f"Numer to {bla}")

if __name__ == "__main__":
    while your_number < bla:
        print(f"twoja liczna jest mniejsza {name}")
        your_number = int(input("Podaj inna liczbe: "))
    while your_number > bla:
        print(f"twoja liczna jest większa {name}")
        your_number = int(input("Podaj inna liczbe: "))
    else:
       print(f"Twoja liczba jest prawidłowa {name}")