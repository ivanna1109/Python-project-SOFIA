import crud
import globalne_funkc as gf

korisnik = None

iznajmljivanjeGlobal = False
narucivanjeGlobal = False

def meni(trenutni_korisnik):
    global korisnik
    korisnik = trenutni_korisnik
    print("\n---------------------Meni----------------------\n")
    print("1) Prikaz svih kategorija")
    print("2) Prikaz naručenih knjiga i ukupnog iznosa")
    print("3) Prikaz omiljenih knjiga")
    print("4) Iznajmljivanje knjige")
    print("5) Naručivanje knjige")
    print("6) Odjavi se\n")
    print("-----------------------------------------------")
    opc = eval(input("Unesite željenu opciju ---> "))
    print("\n{}".format("-"*47))
    izabrana_opcija(opc)
    
def izabrana_opcija(o):
    switch = {
        1: gf.prikaz_kategorija,
        2: prikaz_narucenih_knjiga,
        3: prikaz_omiljenih_knjiga,
        4: iznajmljivanje_knjige,
        5: narucivanje_knjige,
        6: gf.zavrsi_program
        }
    try:    
        return switch[o]()
    except:
        print("\nUnesite jednu od ponuđenih opcija!")
        print("\n{}".format("-"*47))
        meni(korisnik)
        return
    

def prikaz_knjige(k, idKat, iznajmljivanje, narucivanje):
    
    global iznajmljivanjeGlobal
    iznajmljivanjeGlobal = iznajmljivanje
    
    global narucivanjeGlobal
    narucivanjeGlobal = narucivanje
    
    global korisnik
    
    if iznajmljivanjeGlobal:
        iznajmi(k)
    elif narucivanjeGlobal:
        naruci(k)
    else:
        print("\n1) Dodaj knjigu u omiljene\n2) Povratak na listu knjiga\n")
        print("-"*47)
        opcija = eval(input("Unesite željenu opciju ---> "))
        print("\n{}".format("-"*47))
        if opcija == 1:
            if crud.dodaj_omiljene(korisnik[0], k[0]):
                print("\nUspešno ste dodali knjigu u Vaše omiljene knjige!\n")
            else:
                print("\nKnjiga je već u Vašim omiljenim knjigama.\n")
            print("-"*47)
            meni(korisnik)
            return
        elif opcija == 2:
            gf.prikaz_knjiga(idKat)
            return
        else:
            print("\nUnesite jednu od ponuđenih opcija!")
            print("\n{}".format("-"*47))
            prikaz_knjige(k,idKat, iznajmljivanje, narucivanje)
            return;

def iznajmi(k):
    global korisnik
    if k[4] > korisnik[6]:
        print("\nNemajte dovoljno poena da iznajmite ovu knjigu.")
        input("Za povratak na početni meni, pritisnite ENTER ---> ")
        print("\n{}".format("-"*47))
        meni(korisnik)
        return
    if k[5] == 0:
        print("Nema primeraka knjige na lageru.")
        input("Za povratak na početni meni, pritisnite ENTER ---> ")
        print("\n{}".format("-"*47))
        meni(korisnik)
        return
    input("Za nastavak sa iznajmljivanjem knjige ({} poena), pritisnite ENTER.\nNa Vašem računu imate {} poena.\n".format(k[4], korisnik[6]))
    crud.iznajmi_knjigu(korisnik[0], korisnik[6], k[0], k[4], k[5])
    print("-"*47)
    print("\nUspešno ste iznajmili knjigu!\n")
    print("-"*47)
    meni(korisnik)
    
def naruci(k):
    global korisnik
    if k[5] == 0:
        print("Nema primeraka knjige na lageru.")
        input("\nZa povratak na početni meni, pritisnite ENTER ---> ")
        meni(korisnik)
        return
    input("Knjiga će biti dostavljena na kućnu adresu.\nPlaćanje pouzećem.\nCena knjige: {}din\nZa nastavak kupovine knjige, pritisnite ENTER ---> ".format(k[7]))
    crud.naruci_knjigu(korisnik[0], k[0], k[5], k[7])
    print("\n{}".format("-"*47))
    print("\nUspešno ste naručili knjigu!\n")
    print("-"*47)
    meni(korisnik)
    
def prikaz_narucenih_knjiga():
    global korisnik
    narucene_knjige = crud.narucene(korisnik[0])
    if narucene_knjige:
        print("-"*65)
        print("\nVaše naručene knjige: ")
        print("-"*65)
        i = 1
        ukupna_suma = 0
        for k in narucene_knjige:
            knjiga = crud.nadji_knjigu(k[2])
            if knjiga:
                print("{}. {} - {} ({}din) ".format(i, knjiga[1], knjiga[2], knjiga[7]))
                print("-"*65)
                ukupna_suma += knjiga[7]
        print("\nUkupna suma svih naručenih knjiga je: {}.00".format(ukupna_suma))
        print("-"*65)
    else:
        print("Nemate naručenih knjiga!")
    input("Za povratak na meni, pritisnite ENTER ---> ")
    meni(korisnik)
    
def prikaz_omiljenih_knjiga():
    global korisnik
    omiljene = crud.omiljene_knjige(korisnik[0])
    if omiljene:
        print("-"*47)
        print("\nVaše omiljene knjige:")
        print("-"*47)
        i = 1
        for o in omiljene:
            omiljena_naziv = crud.nadji_knjigu(o[1])
            if omiljena_naziv != None:
                print("{}) {}".format(i, omiljena_naziv[1]))
                print("-"*47)
                i+=1
    else:
        print("Nemate nijednu knjigu u omiljenim!")
    input("\nZa povratak na meni, pritisnite ENTER ---> ")
    meni(korisnik)
    

def iznajmljivanje_knjige():
    gf.prikaz_kategorija(iznajmljivanje = True)
    

def narucivanje_knjige():
    gf.prikaz_kategorija(narucivanje = True)
    