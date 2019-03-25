nMenschen = 100
nAcker = 1000
nGesundheit = 100
nGetreide = 1200
i = 1

while (i <= 10):

    print("Jahr: " + str(i))
    print("Bevölkerung: " + str(nMenschen))
    print("Anzahl Äcker: " + str(nAcker))
    print("Gesundheit: " + str(nGesundheit))
    print("Getreide: " + str(nGetreide))

    nMenschen_input = int(input("Gib Anzahl für versorgte Bevölkerung ein für Jahr " + str(i) + " > "))
    nAcker_input = int(input("Gib Anzahl der gekauften Äcker ein für Jahr " + str(i) + " > "))
    nAcker += nAcker_input
    nAckerbewirtet = int(input("Gib Anzahl der zu bewirtenden Äcker ein für Jahr " + str(i) + " > "))
    i += 1

    if (nAckerbewirtet < nAcker): nAacker = nAckerbewirtet

    #Check if summe < Anzahl Getreide
    if nMenschen_input + nAcker_input + nAckerbewirtet > nGetreide:
        print("nicht möglich")

    #Berechnung Gesundheitslevel
    if nMenschen_input < nMenschen:
        nGesundheit = 100 - (nMenschen_input/nMenschen)
