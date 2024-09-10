
class Cilveks:
    def __init__(self, vards, vecums, dzimums):
        self.name = vards
        self.gender = dzimums
        self.age = vecums
        
    def dzdiena(self):
        self.age += 1
        
    def vardamaina(self):
        self.name = input("Ievadi jauno vārdu!")
        
    def pastastiparsevi(self):
        if self.gender == "s":
            self.gender = "sieviete"
        elif self.gender == "v":
            self.gender = "vīrietis"
        print("sveiki,mani sauc {}, mans dzimums ir {}, man ir {} gadi.".format(self.name, self.gender, self.age))
        


persona = Cilveks("Marta", 34 , "s")
print(persona.name)
print(persona.age)
print(persona.gender)
raimonds = Cilveks("raimonds", 17, "v")
print(raimonds.name, raimonds.age, raimonds.gender)
raimonds.dzdiena()
print(raimonds.age)
raimonds.pastastiparsevi()
raimonds.vardamaina()
raimonds.pastastiparsevi() 