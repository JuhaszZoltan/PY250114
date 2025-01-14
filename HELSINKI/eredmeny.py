class Eredmeny:
    def __init__(self, sor:str):
        tmp:list[str] = sor.strip().split(' ')
        self.helyezes:int = int(tmp[0])
        self.sportolok:int = int(tmp[1])
        self.sportag:str = tmp[2]
        self.versenyszam:str = tmp[3]
        self.olimpiai_pont:int = 7 if self.helyezes == 1 else 7 - self.helyezes