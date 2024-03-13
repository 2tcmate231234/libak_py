"""LIBÁK

A róka libát lop a faluból. A libák súlyát – pontosabban tömegét – listában adjuk meg. A farkas a dűlőútnál várja a rókát, és a három kilónál nagyobb libákat elveszi – a piciket nagylel�kűen otthagyja a rókának.
libak = [1,5,2,3,4]

a. Hány kiló libát ehet meg a róka?
b. Átlagosan hány kilósak a rókának maradt libák?
c1. Előfordult-e olyan, hogy a róka legalább háromkilós libát lopott?
c2. Előfordult-e olyan, hogy a róka kisebb libát hozott, mint az előző napon?
d. Hányadik napon sikerült a rókának először legalább háromkilós libát lopnia?
e. Melyik a róka első legalább háromkilós libája?
f. Hány libát tarthat meg a róka?
g. Mekkora a legkisebb liba, amit a farkas elvesz a rókától?
"""
def beolvasas():
    lista=[]
    with open("libak.txt","r",encoding="UTF-8") as fm:
        for sor in fm:
            lista.append(int(sor.strip()))
    return lista

def osszegzes(l):
    szum=0
    for suly in l:
        if suly<4:
            szum+=suly
    return szum

def megszamolas(l):
    db=0
    for suly in l:
        if suly < 4:
            db+=1
    return db

def eldontes(l):
    i=0
    van=False
    while i<len(l) and not (l[i]>=3):
        i+=1
    if i<len(l):
        van = True
    else:
        van = False
    return van

def eldontes2(l):
    i=len(l)-1
    van=False
    while i>0 and not (l[i]>l[i-1]):
        i-=1
    if i>0:
        van = True
    else:
        van = False
    return van

def kiir(l,r_o,r_db,r_lp,r_kisebb ):
    print(f"A lista elemei: {l}")
    print(f"{r_o} kiló libát ehet meg a róka.")
    print(f"Átlagosan {r_o/r_db} kilósak a rókának maradt libák.")
    if r_lp:
        print(f"Előfordult, hogy a róka legalább háromkilós libát lopott. ")
    else:
        print(f"Nem fordult elő, hogy a róka legalább háromkilós libát lopott.")
    if r_kisebb:
        print("Előfordult olyan, hogy a róka kisebb libát hozott, mint az előző napon.")
    else:
        print("Nem fordult elő olyan, hogy a róka kisebb libát hozott, mint az előző napon.")
   
 
#input
libak=beolvasas()

#számítás
roka_megehet_ennyi_kg_libat=osszegzes(libak)
roka_megehet_ennyi_db_libat=megszamolas(libak)
roka_lopott_legalabb_harom_kg_libat=eldontes(libak)
roka_lopott_kisebb_libat_az_elozo_nap=eldontes2(libak)


#output
kiir(libak,roka_megehet_ennyi_kg_libat,roka_megehet_ennyi_db_libat, roka_lopott_legalabb_harom_kg_libat,roka_lopott_kisebb_libat_az_elozo_nap)