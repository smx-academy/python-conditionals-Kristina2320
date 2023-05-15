
#zadaca 1
"""Напишете програма која ќе прочита два броја од корисникот и ќе го испечати збирот, разликата, производот и количникот на двата броја. 
Споредете кој резултат е поголем, збирот или производот"""

"""broj1 = int(input("vnesete eden broj "))
broj2 = int(input("vnesete vtor broj "))
zbir = broj1 + broj2
print(f"Zbirot na broevite {broj1} i {broj2} e {zbir}")
razlika = broj1-broj2
print(f"Razlikata na broevite {broj1} i {broj2} e {razlika}")
proizvod = broj1*broj2
print(f"Proizvodot na broevite {broj1} i {broj2} e {proizvod}")
kolicnik = broj1/broj2
print(f"Kolicnikot na broevite {broj1} i {broj2} e {kolicnik}")
if proizvod > zbir:
    print ("Proizvodot e pogolem od zbirot")
elif proizvod < zbir:
    print ("Zbirot e pogolem od proizvodot")
elif proizvod == zbir:
    print ("Proizvodot i zbirot se ednakvi")"""


#zadaca 2
"""Напишете програма која ќе прочита број од корисникот и ќе го провери дали тој е деллив со 3, 5, 3 и 5, а потоа ќе испечати соодветната порака."""
"""broj = int(input("vnesete eden broj "))
if broj % 3 == 0:
    print ("Brojot e delliv so 3")
else:
    print ("Brojot ne e delliv so 3")
if broj % 5 == 0:
    print ("Brojot e delliv so 5")
else:
    print ("Brojot ne e delliv so 5")"""


#zadaca 3
"""Напишете програма која ќе прочита број од корисникот и ќе го провери дали тој е парен, и потоа ќе испечати соодветната порака."""
"""paren_broj = int(input("vnesete eden broj "))
if paren_broj % 2 == 0:
    print ("Brojot e paren")
else:
    print ("Projot e neparen")"""



#zadaca 5
"""Напишете програма која ќе прочита два броја од корисникот и ќе го испечати производот на броевите, да се провери дали резултатот е парен или не парен."""
"""broj_eden = int(input("vnesete eden broj "))
broj_dva = int(input("vnesete vtor broj "))
proizvodd = broj_eden*broj_dva
print(f"Proizvodot na broevite {broj_eden} i {broj_dva} e {proizvodd}")
if proizvodd % 2 == 0:
    print ("Proizvodot e paren broj")
else:
    print ("Proizvodot e neparen broj")
"""



#zadaca 6
"""Напишете програма која ќе прочита страни на правоаголник и квадрат, да се пресмета плоштината и да се провери дали збирот на плоштините е деллив со 2,3 или 5"""
"""a = int(input("Vnesete ja sirinata na pravoagolnikot: "))
b = int(input("Vnesete ja dolzinata na pravoagolnikot:"))
plostina = a*b
print(f"Plostinata na pravoagolnikot е {plostina}")
c = int(input("Vnesete strana na kvadrat: "))
plostina_c = c*c
print(f"Plostinata na kvadratot е {plostina_c}")
zbir_na_plostini = plostina + plostina_c
print(f"Zbirot na plostinite na pravoagolnikot i kvadratot е {zbir_na_plostini}")
if zbir_na_plostini % 2 == 0:
    print ("Zbirot na plostinite e delliv so 2")
else:
    print ("Zbirot na plostinite ne e delliv so 2")
if zbir_na_plostini % 3 == 0:
    print ("Zbirot na plostinite e delliv so 3")
else:
    print ("Zbirot na plostinite ne e delliv so 3")
if zbir_na_plostini % 5 == 0:
    print ("Zbirot na plostinite e delliv so 5")
else:
    print ("Zbirot na plostinite ne e delliv so 5")"""




#zadaca 7
"""Напишете програма која ќе прочита големина на агли во триаголник, да се провери дали може да се формира триаголник со тие агли(збирот мора да биде 180) 
и ако може да се формира триаголник да се провери каков триаголник може да се формира"""
"""x = int(input("Vnesete prv agol na traigolnikot:"))
y = int(input("Vnesete vtor agol na traigolnikot:"))
z = int(input("Vnesete tret agol na traigolnikot:"))
zbir = x+y+z
print(f"Zbirot na aglite na triagolnikot e {zbir}")
if zbir != 180:
    print ("Triagolnikot ne moze da se formira")
else:
    #odreduvanje na vidot na triagolnik
    if x == y == z:
        print ("Triagolnikot e ramnostran")
    elif x == y or x == z or x == z:
        print ("Triagolnikot e ramnokrak")
    else:
        print ("Triagolnikot e raznostran")"""


#bonus zadaca
"""Да се напише програма која ќе прочита година од корисникот и да одреди дали е годината престапна"""
"""godina=int(input("Vnesete godina:"))
if godina % 4 == 0 or godina % 100 == 0:
    print("Godinata e prestapna")
else:
    print ("Godinata ne e prestapna")"""

