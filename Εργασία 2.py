Eis = True

while(Eis==True):
    Prwtoi = []
    Meg=True
    while (Meg==True): #Ginetai elegxos an o arithmos pou dothike einai mikroteros tou 1000000
        x = int(input("Eisagete enan akeraio mikrotero h iso tou 1000000"))
        if (x<=1000000):
            Meg=False
        else:
            print("O arithmos htan megalyteros tou 1000000")
    i = 1
    while (i<=x): #Vriskontai oi prwtoi mexri ton arithmo pou dothike
        k = 0
        if (x%i==0):
            j = 1
            while (j<=i):
                if (i%j==0):
                    k = k + 1
                j = j + 1
            if (k==2):
                Prwtoi.append(i)
        i = i + 1

    result = ""
    for i in range (0,len(Prwtoi)):
        n = x
        d = 0 #H dynami sthn opoia ypswnetai kathe paragontas
        while (n%Prwtoi[i]==0):
            d = d + 1
            n = n/Prwtoi[i]

        if (d>1):
            result = result + "(" + str(Prwtoi[i]) + "**" + str(d) + ")"
        else:
            result = result + "(" + str(Prwtoi[i]) + ")"

    print ("O arithmos " + str(x) + " analyetai se  ginomeno prwtwn paragontwn ws " + result)

    ok = False
    while(ok == False):
        ap = input("Thelete na eisagete allon arithmmo gia analysh prwtwn paragwntwn?(Nai/Oxi)")
        if (ap == "Nai"):
            Eis = True
            ok = True
        elif (ap == "Oxi"):
            Eis = False
            ok = True
        else:
            print("Nai h Oxi? Greeklish please, I don't understand")


