Eis = True

while (Eis==True):

    x = int(input("Eisagete to megethos tis listas"))
    list1 = []
    for i in range (0,x):
        diast = []
        mini = int(input("Elaxisto " + str(i+1) + "ou diasthmatos"))
        maxi =int(input("Megisto " + str(i+1) + "ou diasthmatos"))
        diast.append(mini)
        diast.append(maxi)
        list1.append(diast)

    def sumIntervals(list1):
        for i in range (0,len(list1)):
            for j in range (i+1,len(list1)):
                if (list1[i][0]>=list1[j][0] and list1[i][1]<=list1[j][1]):
                    list1[i][0]=0
                    list1[i][1]=0
                    break
                elif (list1[i][0]<=list1[j][0] and list1[i][1]>=list1[j][1]):
                    list1[j][0]=0
                    list1[j][1]=0
                elif(list1[i][0]>=list1[j][0] and list1[i][1]>=list1[j][1] and list1[i][0]<=list1[j][1]):
                    list1[j][1]=list1[i][0]
                elif (list1[i][0]<=list1[j][0] and list1[i][1]<=list1[j][1] and list1[i][1]>=list1[j][0]):
                    list1[j][0]=list1[i][1]
        s = 0
        for i in range(0,len(list1)):
            s = s + list1[i][1]-list1[i][0]
        return s

    print("To athroisma tou mhkous twn diasthmatwn einai: " + str(sumIntervals(list1)))

    ok = False
    while(ok == False):
        ap = input("Thelete na eisagete allh lista arithmwn?(Nai/Oxi)")
        if (ap == "Nai"):
            Eis = True
            ok = True
        elif (ap == "Oxi"):
            Eis = False
            ok = True
        else:
            print("Nai h Oxi? Greeklish please, I don't understand")
