n_people = 100
n_land = 1000
n_health = 100
n_corn = 0
i = 1


        


while (i <= 10):
    n_people_input = int(input("Gib Anzahl fuer versorgte Bevoelkerung ein fuer Jahr " + str(i) + " > "))
    n_land_input = int(input("Gib Anzahl der gekauften Aecker ein fuer Jahr " + str(i) + " > "))
    n_land_used = int(input("Gib Anzahl der zu bewirtenden Aecker ein fuer Jahr " + str(i) + " > "))
    #n_corn = n_land_used*19 - (n_people_input*20) - n_land_input*1
    #print(n_people_input)


    
    land_price = 16 ##to do randomisieren

    #Check if summe < Anzahl corn
    def check_input (n_corn, n_people_input, n_land_input, n_land_used):
        if n_people_input + n_land_input + n_land_used > n_corn:
            pass

    #Berechnung healthslevel
    def check_health (n_corn, n_people_input):
        if n_people_input < n_people:
            n_health = 100 - (n_people_input/n_people)
            return n_health

    def calculate_corn (n_corn, n_people_input, n_land_input, n_land_used):
        #n_corn = 1200
        n_corn -= n_people_input*20 + n_land_input*land_price+ n_land_used
        return n_corn


    def check_gestorben (n_corn, n_people_input):
        n_corn -= n_people_input*20


    #eingabe()
    print("Jahr: " + str(i))
    print("Bevoelkerung: " + str(n_people_input))
    print("Anzahl land: " + str(n_land_input))
    print("Gesundheit: " + str(n_health))
    print("Getreide: " + str(n_corn))


    i += 1
    
    check_input(n_corn, n_people_input, n_land_input, n_land_used)
    calculate_corn(n_corn, n_people_input, n_land_input, n_land_used)
    check_gestorben(n_corn, n_people_input)
    check_health(n_corn, n_people_input)
