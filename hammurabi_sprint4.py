from random import randint
import doctest

"""This Program is a basic version of Hammurabi's Game. The goal is to keep your people alive for ten years
respectively ten moves. It's about growing and trading crops and trading land. During the game some unexpected events may happen.
 Authors of this program are: Magdalena Breu, Thomas Honeder, Jochen Hollich and Paul Klein."""

"""The numbers below are the initial values. The population can take values between 0 and 100. If it's 0 you lost
and the game is finished. The health can take also values between 0 and 100. As mentioned before: If it's 0 you lost
and the game is finished. The number of land and crop are infinite because you can buy and sell them. But if you don't 
have enough crops to feed your people it's hard to survive."""


n_people = 100
n_land = 1000
n_health = 100
n_crop = 5000
i = 1
n_health = 100

"""The yield of the crops is random due to the health condition of the people
 and the and the other environmental conditions"""
def randomize_yield():
    global n_yield
    n_yield = randint(1,8)
    return n_yield

"""The function randomize_land() defines the price of the land. It takes random values between 17 and 26. The 
The currency is crop. The price varies every year."""

def randomize_land():
    global land_price
    land_price = randint(17, 26)
    return land_price

"""These print statements are shown every year to let you know how many resources are available."""

def print_stats():
    print("{:<25} {:>10}".format("Jahr: ", i))
    print("{:<25} {:>10}".format("Bevölkerung: ", n_people))
    print("{:<25} {:>10}".format("Anzahl Äcker:", n_land))
    print("{:<25} {:>10}".format("Gesundheit:", n_health))
    print("{:<25} {:>10}".format("Getreide:", n_crop))
    print("{:<25} {:>10}".format("Ackerpreis diese Jahr:", land_price))


"""These three ask-functions are for user input. You can vary the values every year."""

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

"""This function checks if your overall crop invest matches your stock. 
If not you are requested to revise your input."""

def check_crop():
    global i
    #calculate Getreide
    if n_nextCrop <= 0:
        n_people_input = 0
        n_land_input = 0
        n_landcultivated = 0
        i -= 1
        print ("Zu wenig Getreide, nochmal versuchen: ")

"""If you are treating your people bad or if you have non forward-looking investment planning the health 
condition of your people is about to fall and they will die. If more than 30 percent of the people are died
in one year you lost the game."""

def check_too_many_died():
    global n_people
    global n_people_input
    #if more than 30% die in this round, game is lost
    if (n_people_input/n_people) <= 0.3:
        print("Zu viele Menschen gestorben, du hast verloren;(")
        exit()

"""You win, if your people survived ten years."""

def end_of_game():
    global i
    if i == 10 and n_people > 0:
        print ("Gewonnen!")

"""The function calculate_crop calculates the crop you are earning in the next year. It's calculated
from the quantity of people, the health condition """

def calculate_crop():
    global n_crop
    global n_nextCrop
    n_nextCrop = n_crop- (n_people_input * 20 + n_land_input * land_price + n_landcultivated)

    if n_nextCrop <= 0:
        n_crop -= (n_people_input * 20 + n_land_input * land_price + n_landcultivated)
        return n_crop
    else: #!
        n_crop == n_nextCrop #!
        return n_crop


"""This function calculates the health condition of the people. If you are not feeding the entire population
 the health condition drops in the relation to the underfed."""

def check_health():
    global n_health
    #Berechnung Gesundheitslevel
    if n_people_input < n_people:
        n_health = int((n_people_input/n_people))
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

"""Based on the random yield """
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

"""To make the game more exciting and uncontrollable, unexpected events e.g. plagues or rat infestation 
may take place. The probability of these events are random."""
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

def start_game():
    global i
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

def set_globals():
    global land_price

    land_price = 20

def get_globals():
    return (n_people, n_land, n_health, n_crop, i,n_people_input, land_price, n_land_input, n_landcultivated, n_health)

def set_input(people_input, land_input, landcultivated):
    global n_people_input
    global n_land_input
    global n_landcultivated


    n_people_input = people_input
    n_land_input = land_input
    n_landcultivated = landcultivated

def set_input_nCrop(nCrop):
    global n_nextCrop

    n_nextCrop = nCrop

def set_input_land(calc_land_input,nextCrop):
    global n_nextCrop
    global n_land

    n_land_input = calc_land_input
    n_nextCrop = nextCrop

def set_input_price(nprice):
    global price

    price = nprice


def set_input_endgame(xx,people):
    global i
    global n_people

    i = xx
    n_people = people