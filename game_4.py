from random import randint

n_people = 100
n_land = 1000
n_health = 100
n_crop = 5000
i = 1
#n_people_input = int
#land_price = int
#n_land_input = int
#n_landcultivated = int
n_health = 100
#n_yield = int




def randomize_yield():
    global n_yield
    n_yield = randint(1,8)
    return n_yield

def randomize_land():
    global land_price
    land_price = randint(17, 26)
    return land_price

def print_stats():
    print("Jahr: " + str(i))
    print("Bevölkerung: " + str(n_people))
    print("Anzahl Äcker: " + str(n_land))
    print("Gesundheit: " + str(n_health))
    print("Getreide: " + str(n_crop))
    print("Ackerpreis diese Jahr: " + str(land_price))


def ask_inputs_people():
    global n_people_input
    n_people_input = int(input("Gib Anzahl für versorgte Bevölkerung ein für Jahr " + str(i) + " > "))
    return n_people_input
def ask_land_input():
    global n_land_input
    n_land_input = int(input("Gib Anzahl der gekauften Äcker ein für Jahr " + str(i) + " > "))
    return n_land_input
def ask_land_cultivate():
    global n_landcultivated
    n_landcultivated = int(input("Gib Anzahl der zu bewirtenden Äcker ein für Jahr " + str(i) + " > "))
    return n_landcultivated

def check_crop():
    global i
    #calculate Getreide
    if n_nextCrop <= 0:
        n_people_input = 0
        n_land_input = 0
        n_landcultivated = 0
        i -= 1
        print ("Zu wenig Getreide, nochmal versuchen: ")


def check_too_many_died():
    global n_people
    global n_people_input
    #if more than 30% die in this round, game is lost
    if (n_people_input/n_people) <= 0.3:
        print("Zu viele Menschen gestorben, du hast verloren;(")
        exit()
def end_of_game():
    global i
    if i == 10 and n_people > 0:
        print ("Gewonnen!")

def calculate_crop():
    global n_crop
    global n_nextCrop
    n_nextCrop = n_crop- (n_people_input * 20 + n_land_input * land_price + n_landcultivated)

    if n_nextCrop <= 0:
        n_crop -= (n_people_input * 20 + n_land_input * land_price + n_landcultivated)
        return n_crop

def check_health():
    global n_health
    #Berechnung Gesundheitslevel
    if n_people_input < n_people:
        n_health = (n_people_input/n_people)
    return n_health

def check_starved():
    global n_nextCrop
    global n_health
    global n_people
    #Check gestorben
    if n_nextCrop >= 0 and n_health <= 30:
        #Wenn Gesundheit schlecht Dezimieren um 1/3
        n_people = n_people*0.7
        print("Die Gesundheit ist zu niedrig, 30% der Bevölkerung sind gestorben")
        #Durchschnittliche Gesundheit geht wieder rauf
        n_health = 80
    return n_health

def check_land_yield():
    global n_crop
    #Check Acker Bewirtschaftet
    if n_nextCrop >= 0:
        n_crop = n_crop * n_yield
        return n_crop

def check_land_is_cultivated():
    if n_nextCrop >= 0:
        n_land = int(n_land_input + (n_people_input * n_health)/10)
        return n_land

def calculate_land():
    global n_land
    #global n_land
    if n_nextCrop >= 0:
        n_land += n_land_input
        return n_land

def plague():
    global n_people
    plague_appear = False
    plague_amount = randint(1,30)
    if plague_appear == True:
        print("Eine Plage ist aufgetreten und hat " + plague_amount + "% der Bevölkerung vernichtet!" )
        n_people = int (n_people*(plague_amount/100))
        return int(n_people)


def rats():
    global n_crop
    rats_appear = False
    rats_amount = randint(1, 30)
    if rats_appear == True:
        print("Ratten sind aufgetreten und hat " + rats_amount + "% des Getreides vernichtet!" )
        n_crop = n_crop*(rats_amount/100)
        return n_crop

def set_plague():
    global i
    if i == randint(1,10):
        plague_appear = True

def set_rats():
    global i
    if i == randint(1,10):
        rats_appear = True


while (i <= 10):
    randomize_land()
    randomize_yield()
    print_stats()
    ask_inputs_people()
    ask_land_input()
    ask_land_cultivate()
    calculate_crop()
    check_crop()
    check_starved()
    check_land_yield()
    check_health()
    check_starved()
    set_plague()
    set_rats()

    calculate_land()

    i += 1

