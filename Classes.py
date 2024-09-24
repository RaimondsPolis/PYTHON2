
class Cilveks:
    def __init__(self, vards, dzimums, vecums = 0):
        self.name = vards
        self.gender = dzimums
        self.age = vecums
        
    def dzdiena(self):
        self.age += 1
        
    def vardamaina(self):
        self.name = input("Ievadi jauno vārdu!")

    
        
    def Genderchange(self, jaunais_dzimums = ""):
        if jaunais_dzimums == "":
            if self.gender == "s":
                print("s")
                self.gender = "v"
                print("tavs dzimums tagad ir: ", self.gender )
            elif self.gender == "v":
                print("v")
                self.gender = "s"
                print("tavs dzimums tagad ir: ", self.gender )
            else:
                print("nekatrs")
                # self.gender = input("ievadi savu jauno dzimumu: ")
        else:
            print("jauns")
            self.gender = jaunais_dzimums
        self.info()
        
    def info(self):
        if self.gender == "s":
            vards = "sieviete"
        elif self.gender == "v":
            vards = "vīrietis"
        else:
            vards = self.gender
        return "Sveiki, mani sauc {}, mans dzimums ir {}, man ir {} gadi.".format(self.name, vards, self.age)
    def info2(self):
        return "{}, {}, {}".format(self.name, self.gender, self.age)  
    

class Sieviete(Cilveks):
    def __init__(self, vards, haircolor, vecums=0):
        super().__init__(vards, "s", vecums)
        self.matukrasa = haircolor
        self.info()
    def __del__(self):
        print("aaa")

class Virietis(Cilveks):

    def __init__(self, vards, bench, vecums=0):
        super().__init__(vards, "v", vecums)
        self.press = bench
        self.info()

    def info(self):
        super().info()
        print("Es varu benchot {}".format( self.press))


    def strong(self):
        self.press +=20
    
    def __del__(self):
        print("aa")

# persona = Cilveks("Marta", "s", 34)
# raimonds = Cilveks("raimonds", "v", 17)
# human = Sieviete("Madara", "brūna")
# darius = Virietis("Darius", 405, 28)
