"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Petra Šnajdrová
email: petra.snajdrova@seznam.cz
"""

from random import choice, sample

def pozdrav_uzivatele():
    oddelovac = ('-' * 47)
    print('Hi there!')
    print(oddelovac)
    print("I've generated a random 4 digit number for you.", "Let's play a bulls and cows game.", sep="\n")
    print(oddelovac)

def tajne_cislo():
    cisla = list('123456789')
    prvni_cislo = choice(cisla)
    cisla.remove(prvni_cislo)
    zbyvajici_cisla = sample(cisla + ['0'], 3)
    return prvni_cislo + ''.join(zbyvajici_cisla)

def zkontroluj_vstup(tip):
    if not tip.isdigit():
        return 'Enter the number not text!'
    if len(tip) != 4:
        return 'Enter the number with 4 digits!'
    if tip[0] == '0':
        return 'The number cannot starts with zero!'
    if len(set(tip)) != 4:
        return 'The number contains duplicates!'
    return None


def vyhodnot_tip(tajne, tip):
    bulls = 0
    for x, digit in enumerate(tip):
        if tajne[x] == digit:
            bulls += 1
    
    cows = 0
    for digit in tip:
        if digit in tajne:
            cows += 1
    cows -= bulls
    
    return bulls, cows


def format_slov(bulls, cows):
    """ fromat slov bull/bulls a cow/cows"""
    if bulls == 1:
        bull_word = "bull"
    else:
        bull_word = "bulls"
    
    if cows == 1:
        cow_word = "cow"
    else:
        cow_word = "cows"
    oddelovac = ('-' * 47)
    return f'{bulls} {bull_word}, {cows} {cow_word}\n{oddelovac}'

def hlavni_smycka_hry():
    pozdrav_uzivatele()
    hadane_cislo = tajne_cislo()
    pokusy = 0
    
    while True:
        tip = input('Enter a number: ').strip()
        overeni = zkontroluj_vstup(tip)

        if overeni:
            print(overeni)
            continue

        pokusy += 1
        bulls, cows = vyhodnot_tip(hadane_cislo, tip)
        print(format_slov(bulls, cows))

        if bulls == 4:
            oddelovac = ('-' * 47)
            print(f"Correct, you've guessed the right number \nin {pokusy} guesses!")
            print(oddelovac)
            print('That is amazing!')
            break

if __name__ == "__main__":
    hlavni_smycka_hry()