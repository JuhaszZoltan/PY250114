class Versenyzo:
    def __init__(self, sor:str):
        tmp:list[str] = sor.strip().split(';')
        self.nev:str = tmp[0]
        self.kategoria:str = tmp[1]
        self.egyesulet:str = tmp[2]
        self.pontok:list[int] = []
        for i in range(8): self.pontok.append(int(tmp[i + 3]))
        self.osszpontszam:int = 0
        self.pontok.sort()
        if self.pontok[0] != 0: self.osszpontszam += 10
        if self.pontok[1] != 0: self.osszpontszam += 10
        for i in range(2, len(self.pontok)):
            self.osszpontszam += self.pontok[i]