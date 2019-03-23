from random import randint
print(randint(0, 9))
n_people = 100
n_land = 1000
n_health = 100
n_crop = 5000
i = 1
#acker_price = 16 ##to do randomisieren




while (i <= 10):
    land_price = randint(17, 26)
    n_yield = randint(1,8)

    print("Jahr: " + str(i))
    print("Bevölkerung: " + str(n_people))
    print("Anzahl Äcker: " + str(n_land))
    print("Gesundheit: " + str(n_health))
    print("Getreide: " + str(n_crop))
    print("Ackerpreis diese Jahr: " + str(land_price))


    n_people_input = int(input("Gib Anzahl für versorgte Bevölkerung ein für Jahr " + str(i) + " > "))
    n_land_input = int(input("Gib Anzahl der gekauften Äcker ein für Jahr " + str(i) + " > "))
    n_landcultivated = int(input("Gib Anzahl der zu bewirtenden Äcker ein für Jahr " + str(i) + " > "))

    #calculate Getreide
    n_nextCrop = n_crop- (n_people_input * 20 + n_land_input * land_price + n_landcultivated)
    if n_nextCrop <= 0:
        n_people_input = 0
        n_land_input = 0
        n_landcultivated = 0
        i -= 1
        print ("Zu wenig Getreide, nochmal versuchen: ")
    n_crop -= (n_people_input * 20 + n_land_input * land_price + n_landcultivated)

    #Berechnung Gesundheitslevel
    if n_people_input < n_people:
        n_health = (n_people_input/n_people)

    #Check gestorben
    if n_nextCrop >= 0 and n_health <= 30:
        #Wenn Gesundheit schlecht Dezimieren um 1/3
        n_people = n_people*0.7
        #Durchschnittliche Gesundheit geht wieder rauf
        n_health = 80

    #Check Acker Bewirtschaftet
    if n_nextCrop >= 0:
        n_land = int(n_land_input + (n_people_input * n_health)/10)
        n_Crop = n_Crop* n_yield

    i += 1