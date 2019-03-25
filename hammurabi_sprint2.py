n_Menschen = 100
n_Acker = 1000
n_Gesundheit = 100
n_Getreide = 1200
i = 1
acker_price = 16 ##to do randomisieren

while (i <= 10):


    print("Jahr: " + str(i))
    print("Bevölkerung: " + str(n_Menschen))
    print("Anzahl Äcker: " + str(n_Acker))
    print("Gesundheit: " + str(n_Gesundheit))
    print("Getreide: " + str(n_Getreide))

    n_Menschen_input = int(input("Gib Anzahl für versorgte Bevölkerung ein für Jahr " + str(i) + " > "))
    n_Acker_input = int(input("Gib Anzahl der gekauften Äcker ein für Jahr " + str(i) + " > "))
    n_Acker += n_Acker_input
    n_Ackerbewirtet = int(input("Gib Anzahl der zu bewirtenden Äcker ein für Jahr " + str(i) + " > "))
    i += 1

    #Check if summe < Anzahl Getreide
    def check_input (n_Menschen_input, n_Acker_input, n_Ackerbewirtet):
        if n_Menschen_input + n_Acker_input + n_Ackerbewirtet > n_Getreide:
            return print("nicht möglich")

    #Berechnung Gesundheitslevel
    def check_Gesundheit (n_Menschen_input):
        if n_Menschen_input < n_Menschen:
            n_Gesundheit = 100 - (n_Menschen_input/n_Menschen)
            return n_Gesundheit

    def calculate_Getreide (n_Menschen_input, n_Acker_input, n_Ackerbewirtet):
        n_Getreide -= n_Menschen_input*20 + n_Acker_input*price+ n_Ackerbewirtet
        return n_Getreide


    def check_gestorben (n_Menschen_input):
        n_Getreide -= in_Menschen_input*20

    calculate_Getreide(n_Menschen_input, n_Acker_input, n_Ackerbewirtet)
    check_input(n_Menschen_input, n_Acker_input, n_Ackerbewirtet)
    check_gestorben(n_Menschen_input)
    check_Gesundheit(n_Menschen_input)