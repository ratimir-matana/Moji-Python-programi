# encoding UTF-8
# Author: Ratimir Matana
# Year: 2020
# Version 2.0
# Made in Python version 3.6
# File name: boje_slova2.py
# License: GNU v3.0


def get_letters(name):
    return [letter for letter in name]


def main():
    x = 1
    boje_slova = {
        'bijela': ['a', 'j', 's'],
        'crvena': ['c', 'č', 'l', 'š', 'u'],
        'žuta': ['e', 'n', 'ć', 'đ', 'y'],
        'zelena': ['g', 'p', 'ž', 'dž'],
        'plava': ['h', 'z', 'lj'],
        'narančasta': ['d', 'm', 'v'],
        'smeđa': ['f', 'o', 'nj'],
        'ljubičasta': ['b', 'k', 't', 'w'],
        'crna': ['i', 'r']}
    while x == 1:
        bijela = 0
        žuta = 0
        crvena = 0
        zelena = 0
        plava = 0
        narančasta = 0
        smeđa = 0
        ljubičasta = 0
        crna = 0
        letters_colors = []
        print()
        name = input('Unesite vaše ime i prezime [npr. Anita Tomić]): ')
        name_ready = get_letters(name.replace(' ', '').lower())
        for keys, values in boje_slova.items():
            for letter in name_ready:
                if letter not in values:
                    continue
                else:
                    for elements in values:
                        if letter == elements:
                            if keys == 'bijela':
                                bijela += 1
                                letters_colors.append(letter)
                                letters_colors.append(keys)
                            else:
                                if keys == 'crvena':
                                    crvena += 1
                                    letters_colors.append(letter)
                                    letters_colors.append(keys)
                                if keys == 'žuta':
                                    žuta += 1
                                    letters_colors.append(letter)
                                    letters_colors.append(keys)
                                if keys == 'zelena':
                                    zelena += 1
                                    letters_colors.append(letter)
                                    letters_colors.append(keys)
                                if keys == 'plava':
                                    plava += 1
                                    letters_colors.append(letter)
                                    letters_colors.append(keys)
                                if keys == 'narančasta':
                                    narančasta += 1
                                    letters_colors.append(letter)
                                    letters_colors.append(keys)
                                if keys == 'smeđa':
                                    smeđa += 1
                                    letters_colors.append(letter)
                                    letters_colors.append(keys)
                                if keys == 'ljubičasta':
                                    ljubičasta += 1
                                    letters_colors.append(letter)
                                    letters_colors.append(keys)
                            if keys == 'crna':
                                crna += 1
                                letters_colors.append(letter)
                                letters_colors.append(keys)

        print()
        print('Ime i prezime:', letters_colors)
        print()
        if bijela > 0:
            print('Bijela: ', bijela)
        if crvena > 0:
            print('Crvena: ', crvena)
        if žuta > 0:
            print('Žuta: ', žuta)
        if zelena > 0:
            print('Zelena: ', zelena)
        if plava > 0:
            print('Plava: ', plava)
        if narančasta > 0:
            print('Narančasta: ', narančasta)
        if smeđa > 0:
            print('Smeđa: ', smeđa)
        if ljubičasta > 0:
            print('Ljubičasta: ', ljubičasta)
        if crna > 0:
            print('Crna: ', crna)


if __name__ == '__main__':
    main()
