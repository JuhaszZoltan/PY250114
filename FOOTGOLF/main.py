from versenyzo import *

versenyzok:list[Versenyzo] = []
stream = open('FOOTGOLF\\fob2016.txt', encoding='utf-8')
for s in stream: versenyzok.append(Versenyzo(s))

print(f'f3: versenyzok szama: {len(versenyzok)}')

nsz:int = 0
for v in versenyzok:
    if v.kategoria == 'Noi': nsz += 1
print(f'f4: noi versenyzok aranya: {(nsz / len(versenyzok) * 100):.2f}%')

nok:list[Versenyzo] = []
for v in versenyzok:
    if v.kategoria == 'Noi':
        nok.append(v)
bi:int = 0
for i in range(1, len(nok)):
    if nok[i].osszpontszam > nok[bi].osszpontszam:
        bi = i
print('f6: a bajnok noi versenyzo:')
print(f'\tnev: {nok[bi].nev}')
print(f'\tegyesulet:: {nok[bi].egyesulet}')
print(f'\tosszpont: {nok[bi].osszpontszam}')

#7. feladat:
stream = open('FOOTGOLF\\osszpontszamFF.txt', 'w', encoding='utf-8')
for v in versenyzok:
    if v. kategoria == 'Felnott ferfi':
        stream.write(f'{v.nev};{v.osszpontszam}\n')
stream.close()

print('f8: egyesuleti statisztika:')
d:dict[str, int] = { }
for v in versenyzok:
    if v.egyesulet not in d.keys():
        d[v.egyesulet] = 1
    else: d[v.egyesulet] += 1
for k, v in d.items():
    if k != 'n.a.' and v > 2:
        print(f'\t{k} - {v} fo')