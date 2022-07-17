# encoding UTF-8
# Author: Ratimir Matana
# Year: 2022
# Version 1.3 (Fixed some bugs)
# Made in Python version 3.6
# File name: numerologija_imena.py
# License: GNU v3.0


def get_letters(name):
    return [letter for letter in name]

def get_number_of_digits(n):
    return len(list(str(n)))

def get_sum_of_digits(n):
    sum = 0
    while n != 0:
        sum = sum + (n % 10)
        n = n // 10
    return sum

def all_elements_equal(lst):
    return not lst or [lst[0]]*len(lst) == lst

def main():
    x = 1
    numeričke_vrijednosti_slova = {
        'jedan': ['a', 'i', 'j', 'q', 'y'],
        'dva': ['b', 'k', 'r'],
        'tri': ['c', 'g', 'l', 's', 'ć', 'č', 'š'],
        'četiri': ['d', 'm', 't', 'đ'],
        'pet': ['e', 'h', 'n', 'x'],
        'šest': ['u', 'v', 'w'],
        'sedam': ['o', 'z', 'ž'],
        'osam': ['f', 'p']}
    while x == 1:
        suma = 0

        numbers = []
        print()
        name = input('Unesite vaše ime [npr. Manda]): ')
        name_ready = get_letters(name.replace(' ', '').lower())
        for keys, values in numeričke_vrijednosti_slova.items():
            for letter in name_ready:
                if letter not in values:
                    continue
                else:
                    for elements in values:
                        if letter == elements:
                            if keys == 'jedan':
                                suma += 1
                                numbers.append(1)
                            else:
                                if keys == 'dva':
                                    suma += 2
                                    numbers.append(2)
                                if keys == 'tri':
                                    suma += 3
                                    numbers.append(3)
                                if keys == 'četiri':
                                    suma += 4
                                    numbers.append(4)
                                if keys == 'pet':
                                    suma += 5
                                    numbers.append(5)
                                if keys == 'šest':
                                    suma += 6
                                    numbers.append(6)
                                if keys == 'sedam':
                                    suma += 7
                                    numbers.append(7)
                                if keys == 'osam':
                                    suma += 8
                                    numbers.append(8)

        numbers.sort(reverse=True)
        zbroj1 = sum(numbers)
        zbroj2 = get_sum_of_digits(zbroj1)
        zbroj3 = get_sum_of_digits(zbroj2)
        print()
        print('Unijeli ste ime: %s, slova u imenu %s imaju numeričku vrijednost %s:' % (name, name_ready, numbers))
        # Izračun 1
        rez = ''
        for n in numbers:
           rez = rez + '+' + str(n)
        rez = rez[1:len(rez)]
        print('Zbroj numeričkih vrijednosti je: %s = %s' % (rez, zbroj1))

        if len(str(zbroj1)) > 1:
            zbroj_2 = list(str(zbroj1))
            # Izračun 2
            for n in zbroj_2:
                rez2 = '' if n == zbroj_2[0] else rez2
                if not rez2:
                    rez2 = str(n)
                else:
                    rez2 = rez2 + '+' + str(n)
            print('Broj %s se svodi na jednoznamekast daljnjim zbrajanjem znamenki, %s = %s' % (zbroj1, rez2, zbroj2))

        if len(str(zbroj2)) > 1:
            zbroj_3 = list(str(zbroj2))
            # Izračun 3
            if all_elements_equal(zbroj_3):
                for n in zbroj_3:
                    rez3 = str(n)
                    rez4 = rez3 + '+' + str(n)
            else:
                 for n in zbroj_3:
                    rez4 = '' if n == zbroj_3[0] else rez4
                    if not rez4:
                        rez4 = str(n)
                    else:
                        rez4 = rez4 + '+' + str(n)
            print('Broj %s se svodi na jednoznamenkast daljnim zbrajanjem znamenki, %s = %s' % (zbroj2, rez4, zbroj3))
        print('Krajni rezultat je broj: %s' % zbroj3)
        print()
        sum2 = get_sum_of_digits(suma)
        final = get_sum_of_digits(sum2)
        if len(list(str(final))) == 1:
            if final == 1:
                print('Broj 1: Ove osobe ostavljaju jak utisak na ljude u svojoj okolini, jer uvijek privlače pažnju. Puni su samopouzdanja i svjesni svojih vrijednosti. Uglavnom postižu uspijeh u životu, ne podnose da gube.')
            if final == 2:
                print('Broj 2: Ovo su ljudi blage, nježne i miroljubive prirode. Imaju umirujuće dejstvo na okolinu i uvijek su puni riječi utjehe za druge. Ovaj broj uglavnom donosi uspijeh u privatnom životu.')
            if final == 3:
                print('Broj 3: Ove ljude odlikuje hrabrost. Ubjedljivi su i često postižu uspijeh u polju koje su odabrali. Uvijek su spremni za akciju.')
            if final == 4:
                print('Broj 4: Oprez ih često sprečava da naprave veći uspijeh. Spori su u djelovanju i reakcijama, i često su sumnjičave prirode. Imaju malo povjerenja u druge i u sebe. Dobri su u detaljima, ali im izmiče cjelokupna slika. Međutim, uporni su i lojalni, pa se na njih uvijek možete osloniti.')
            if final == 5:
                print('Broj 5: Ove osobe su komunikativne, prijateljski nastrojene, živahne i omiljene u društvu. Materijalni komfor uzimaju zdravo za gotovo, a udoban život im je imperativ. Lako uče i obrazuju se i ne mogu zamisliti život bez aktivnog, društvenog angažovanja.')
            if final == 6:
                print('Broj 6: Ovaj broj odgovara umjetnicima, muzičarima i pjesnicima. Oni su šarmantni i dopadljivi, ali i pomalo nestabilni. Vole ljepotu i interesuju se za ljude i prirodu. Privlači ih i okultno.')
            if final == 7:
                print('Broj 7: Ovi ljudi su originalni i inventivni. Interesuju se za misticizam. Ozbiljni su, odani i stabilni.')
            if final == 8:
                print('Broj 8: Ovaj broj donosi težu sudbinu i život pun prepreka koje zahtjevaju veliku borbenost i istrajnost.')
            if final == 9:
                print('Broj 9: Ove osobe su poštene, kreativne i duhovno snažne. Sposobni su da prebrode mnoge teškoće u životu. Rutinu života podnose lakše nego drugi. Sposobni su da vole čista srca.')


if __name__ == '__main__':
    main()
