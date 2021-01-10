#zajednicke funkcionalnosti
import interface_admin as admin
import interface_user as user
import crud

#predefinisane promenljive usera
iznajmljivanjeGlobal = False
narucivanjeGlobal = False

#predefinisanje promenljive admina
brisanjeGlobal = False
azuriranjeGlobal = False

korisnik = None 

def inicijalno(k):
    global korisnik
    korisnik = k
    
def prikaz_kategorija(iznajmljivanje = False, narucivanje = False, brisanje_admin = False, azuriranje_admin = False):
    
    global iznajmljivanjeGlobal
    iznajmljivanjeGlobal = iznajmljivanje
    global narucivanjeGlobal
    narucivanjeGlobal = narucivanje
    global brisanjeGlobal
    brisanjeGlobal = brisanje_admin
    global azuriranjeGlobal
    azuriranjeGlobal = azuriranje_admin
    
    global korisnik
    
    kategorije = crud.sve_kategorije();
    i = 1
    print("Prikaz kategorija: ")
    print("{}\n".format("-"*47))
    for k in kategorije:
        print("{}) {}".format(i, k[1]))
        i+=1
    print("{}) Povratak na meni\n".format(i))
    print("-"*47)
    opcija = eval(input("Unesite željenu opciju ---> "))
    print("\n{}".format("-"*47))
    kategorija = None
    if opcija == i:
        if korisnik[7] == 1:
            user.meni(korisnik)
            return
        else:
            admin.meni(korisnik)
            return
    try:
        kategorija = kategorije[opcija-1]
    except:
        print("-"*47)
        print("\nUnesite jednu od ponuđenih opcija!\n")
        print("-"*47)
        prikaz_kategorija()
        return
    try:
        prikaz_knjiga(kategorija[0])
    except Exception as e:
        print(e)
    
def prikaz_knjiga(idKat):
    print("Prikaz knjiga za izabranu kategoriju: ")
    print("{}\n".format("-"*47))
    knjige = crud.sve_knjige_za_kat(idKat)
    i = 1
    for k in knjige:
        print("{})'{}' - {}".format(i, k[1], k[2]))
        i+=1
    print("{}) Vratite se na prikaz kategorija\n".format(i))
    print("{}".format("-"*47))
    opcija = eval(input("Unesite željenu opciju ---> "))
    print("\n{}".format("-"*47))
    if opcija-1 == len(knjige):
        prikaz_kategorija()
        return
    knjiga = None
    try:
        knjiga = knjige[opcija-1]
    except:
        print("-"*47)
        print("\nUnesite jednu od ponudjenih opcija!\n")
        print("-"*47)
        prikaz_knjiga(idKat)
    prikaz_knjige(knjiga, idKat)
    

def prikaz_knjige(k, idKat):
    print("\n'{}' - {} ({})\n{}\nOpis: {}\n{}\nCena knjige: {}din\n{}".format(k[1], k[2], k[3],"-"*47, k[6], "-"*47, k[7], "-"*47))
    
    global iznajmljivanjeGlobal
    global narucivanjeGlobal
    global brisanjeGlobal
    global azuriranjeGlobal
    global korisnik
    
    if korisnik[7] == 1:
        user.prikaz_knjige(k, idKat, iznajmljivanjeGlobal, narucivanjeGlobal)
    else:
        admin.prikaz_knjige(k, idKat, brisanjeGlobal, azuriranjeGlobal)
            
def zavrsi_program():
    print("Završen program.")