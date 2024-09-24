from Classes import Sieviete
from Classes import Cilveks
cilveku_saraksts = []

for i in range(20):
    cilveku_saraksts.append(Sieviete("Anna","blonda", i))

for sieviete in cilveku_saraksts:
    if sieviete.vecums % 2 == 0:
        sieviete.genderchange()

print("__________________________________________________")
for sieviete in cilveku_saraksts:
    sieviete.info()