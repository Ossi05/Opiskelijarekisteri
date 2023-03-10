
#Opiskelijoiden lisays
def lisaa_opiskelija(opiskelijat, nimi):
    opiskelijat[nimi] = []

    return opiskelijat




#Tulosta opiskelija
def tulosta(opiskelijat, nimi):
    
    if nimi in opiskelijat:
        if opiskelijat[nimi] == []:
            print(nimi+":")
            print(" ei suorituksia")
        else:
            keskiarvo = 0
            print(nimi+":")
            print(f" suorituksia {len(opiskelijat[nimi])} kurssilta:")

            for suoritus in opiskelijat[nimi]:
                #Suoritukset
                print(" ", suoritus[0], suoritus[1])
                keskiarvo += suoritus[1]
                
            print(f" keskiarvo {keskiarvo / len(opiskelijat[nimi])}")
    else:
        print("ei löytynyt ketään nimellä", nimi)





#Suorituksien lisäys
def lisaa_suoritus(opiskelijat, nimi, suoritus):
    if nimi in opiskelijat:
        if suoritus[1] > 0:
            for suoritukset in opiskelijat[nimi]:
                if suoritus[0] == suoritukset[0]:
                    if suoritukset[1] < suoritus[1]:
                        suoritukset[1] = suoritus[1]
                    break
            else:
                opiskelijat[nimi].append(list(suoritus))



#Kooste   
def kooste(opiskelijat):
    
    eniten = 0
    opiskelija = ""
    
    for nimi in opiskelijat:
        #Suoritukset
        if len(opiskelijat[nimi]) > eniten:
            eniten = len(opiskelijat[nimi])
            opiskelija = nimi


    #Paras keskiarvo
    keskiarvo = 0
    paras_keskiarvo = ""
    

    for nimi in opiskelijat:
        luku = 0
        for suoritus in opiskelijat[nimi]:
            luku += suoritus[1]
        avg = luku / len(opiskelijat[nimi])
        if avg > keskiarvo:
            keskiarvo = avg
            paras_keskiarvo = nimi
        
    print(f"opiskelijoita {len(opiskelijat)}")
    print(f"eniten suorituksia {eniten} {opiskelija}")
    print(f"paras keskiarvo {keskiarvo} {paras_keskiarvo}")


if __name__ == "__main__":
    

    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "pekka")
    lisaa_suoritus(opiskelijat, "pekka", ("ohpe", 1))
    lisaa_suoritus(opiskelijat, "pekka", ("ohpe", 5))
    tulosta(opiskelijat, "pekka")