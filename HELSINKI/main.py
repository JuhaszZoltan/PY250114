from eredmeny import *

eredmenyek:list[Eredmeny] = []
stream = open('HELSINKI\\helsinki.txt', encoding='windows-1250')
for s in stream: eredmenyek.append(Eredmeny(s))

print('3. feladat:')
print(f'pontszerzo helyezesek szama: {len(eredmenyek)}')

print('4. feladat:')
ae:int = 0
ee:int = 0
be:int = 0
for e in eredmenyek:
    if   e.helyezes == 1: ae += 1
    elif e.helyezes == 2: ee += 1
    elif e.helyezes == 3: be += 1
print(f'arany: {ae}')
print(f'ezust: {ee}')
print(f'bronz: {be}')

print('5. feladat')
op:int = 0
for e in eredmenyek:
    op += e.olimpiai_pont
print(f'olimpiai pontok szama: {op}')

print('6. feladat')
ts:int = 0
us:int = 0
for e in eredmenyek:
    if e.sportag == 'torna': ts += 1
    elif e.sportag == 'uszas': us += 1
if ts == us: print('egyenlo volt az ermek szama')
elif ts > us: print('torna sportagban szereztek tobb ermet')
else: print('uszas sportagban szereztek tobb ermet')

# 7. feladat
stream = open('HELSINKI\\helsinki3.txt', 'w', encoding='windows-1250')
for e in eredmenyek:
    sportag:str = 'kajak–kenu' if e.sportag == 'kajakkenu' else e.sportag 
    stream.write(f'{e.olimpiai_pont} {e.helyezes} {e.sportolok} {sportag} {e.versenyszam}\n')
stream.close()

print('8. feladat')
mi:int = 0
for i in range(1, len(eredmenyek)):
    if eredmenyek[i].sportolok > eredmenyek[mi].sportolok:
        mi = i
print(f'helyezes: {eredmenyek[mi].helyezes}')
print(f'sportag: {eredmenyek[mi].sportag}')
print(f'versenyszam: {eredmenyek[mi].versenyszam}')
print(f'sportolok szama: {eredmenyek[mi].sportolok}')