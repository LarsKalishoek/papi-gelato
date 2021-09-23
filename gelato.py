

# def f_bollen():
#     bollen = input("Hoeveel bolletjes wilt u?")
#     return bollen

def ijshouder(hoorn):
    if hoorn == 'a':
        hoorn = "hoorntje"
        return hoorn
    elif hoorn == "b":
        hoorn = "bakje"
        return hoorn
def stap3(hoorn, bollen):
    antwoord = input("Hier is uw " + hoorn +  " met " + bollen + " bolletje(s). Wilt u nog meer bestellen? (Y/N) ").lower()
    if antwoord == "y":
        stap1()
    elif antwoord == 'n':
        print("Bedankt en tot ziens.")
    else:
        print("Sorry, dat snap ik niet...")
        stap3(hoorn, bollen)

def stap2(bollen):
    hoorn = input("Wilt u deze " + bollen + " bolletje(s) in A) een hoorntje of B) een bakje? ").lower()
    if hoorn == 'a' or hoorn == 'b':
        hoorn = ijshouder(hoorn)
        stap3(bollen, hoorn)
        return 
    else:
        print("Sorry, dat snap ik niet...")
        stap2(bollen)
def stap1():
    bollen = input("Hoeveel bolletjes wilt u? ")
    if bollen.isdigit() == False:
        print("Sorry, dat snap ik niet...")
        stap1()
    if int(bollen) <= 3:
        smaak(bollen)
        stap2(bollen)
    elif int(bollen) <= 8:
        smaak(bollen)
        print("Dan krijgt u van mij een bakje met " + bollen + " bolletje")
        hoorn = "bakje"
        stap3(hoorn, bollen)
    elif int(bollen) > 8:
        print("Sorry, zulke grote bakken hebben we niet")
        stap1()
    else:
        print("Sorry, dat snap ik niet...")
        stap1()
def smaak(bollen):
    x = 0
    while x < int(bollen):
        x += 1
        check = input("Welke smaak wilt u voor bolletje nummer "  + str(x) + "? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ").lower()
        if check != "a" and check != "c" and check != "m" and check != "v":
            x -= 1
            print("Sorry, dat snap ik niet...")



print("Welkom bij Papi Gelato.")
stap1()

# bollentjes = int(bollen)
# var1 = f_bollen()
# stap2(var1)
# stap1()