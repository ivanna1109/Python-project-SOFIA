import crud
import globalne_funkc as gf
import matplotlib.pyplot as plt
from numpy import arange
import random

brisanjeGlobal = False
azuriranjeGlobal = False

korisnik = None

def meni(trenutni_korisnik):
    global korisnik
    korisnik = trenutni_korisnik
    print("\n---------------------Meni----------------------\n")
    print("1) Prikaz svih kategorija")
    print("2) Prikaz svih korisnika")
    print("3) Prikaz broja izdatih knjiga po korisnicima")
    print("4) Prikaz 5 najomiljenijih knjiga")
    print("5) Prihod 5 najprodavanijih knjiga")
    print("6) Dodavanje nove knjige")
    print("7) Azuriranje informacije o knjizi")
    print("8) Brisanje knjige")
    print("9) Odjavi se\n")
    print("-"*47)
    opc = eval(input("Unesite željenu opciju ---> "))
    print("\n{}".format("-"*47))
    izabrana_opcija(opc)
    

def izabrana_opcija(o):
    switch = {
        1: gf.prikaz_kategorija,
        2: prikaz_svih_korisnika,
        3: prikaz_izdatih_knjiga,
        4: prikaz_najomiljenijih_knjiga,
        5: prihod_knjiga,
        6: dodavanje_knjige,
        7: azuriranje_informacija,
        8: brisanje_knjige,
        9: gf.zavrsi_program
        }
    try:    
        return switch[o]()
    except:
        print("\nUnesite jednu od ponuđenih opcija!")
        print("\n{}".format("-"*47))
        meni(korisnik)
        return

def prikaz_svih_korisnika():
    print("Lista svih registrovanih korisnika: ");
    korisnici = crud.lista_korisnika()
    if korisnici:
        for k in korisnici:
            print('{} {}; username: {}'.format(k[3], k[4], k[1]))

def prikaz_izdatih_knjiga():
    global korisnik
    
    recnik = crud.izdate_chart()
    korisnici_tmp = crud.lista_korisnika()
    korisnici_imena = map(lambda x: x[3]+"\n"+x[4], korisnici_tmp)
    x = list(korisnici_imena)
    
    vrednosti = map(lambda k: (
            recnik[k[0]] if k[0] in recnik.keys() else
            0
        ), korisnici_tmp)
    y = list(vrednosti)
    
    plt.bar(x, y)
    plt.xlabel('Korisnici')
    plt.ylabel('Broj izdatih knjiga')
    plt.yticks(arange(0, max(y)+1, 1.0))
    
    plt.pause(15)
    meni(korisnik)
    # plt.show()          
    
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.1f}%({v:d})'.format(p=pct,v=val)
    return my_autopct
    
def prikaz_najomiljenijih_knjiga():
    global korisnik
    
    recnik = crud.omiljene_chart()
    
    sortirani_recnik = dict()
    sortirani = sorted(recnik, key=recnik.get, reverse = True)
    
    sortirani = sortirani[:5]
    
    for k in sortirani:
        sortirani_recnik[k] = recnik[k]
    
    print(sortirani_recnik)
    nazivi_knjiga = []
    for k in sortirani_recnik:
        pom = crud.nadji_knjigu(k)
        nazivi_knjiga.append(pom[1])
        
    x = nazivi_knjiga    
    y = list(sortirani_recnik.values()) 
    
    fig1, ax1 = plt.subplots()
    ax1.pie(y, labels = x, autopct=make_autopct(y))
    
    plt.pause(15)
    meni(korisnik)
    
def prihod_knjiga():
    global korisnik
    recnik = crud.najprodavanije_chart()
    sortirani_recnik = dict()
    sortirani = sorted(recnik, key=recnik.get, reverse = True)
    
    sortirani = sortirani[:5]
    
    for k in sortirani:
        sortirani_recnik[k] = recnik[k]

    nazivi_knjiga = []
    for k in sortirani_recnik:
        pom = crud.nadji_knjigu(k)
        nazivi_knjiga.append(pom[1])
        
    x = list(nazivi_knjiga)
    y = list(sortirani_recnik.values())
    
    c = list(zip(x,y))
    random.shuffle(c)
    x, y = zip(*c)
    
    plt.scatter(x, y)
    plt.plot(x,y)
    plt.xlabel("Nazivi knjiga")
    plt.ylabel("Prihod po prodatim knjigama")
    plt.yticks(arange(500, max(y)+100, 100.0))
    plt.ylim(ymin=500, ymax=2000)
    
    plt.pause(15)
    meni(korisnik)


def prikaz_knjige(k, idKat, brisanje_admin, azuriranje_admin):
    
    global brisanjeGlobal
    brisanjeGlobal = brisanje_admin
    
    global azuriranjeGlobal
    azuriranjeGlobal = azuriranje_admin
    
    if azuriranjeGlobal:
        azuriranje(k, idKat, brisanje_admin, azuriranje_admin)

    elif brisanjeGlobal:
        brisanje(k, idKat, brisanje_admin, azuriranje_admin)
    
    
def azuriranje_informacija():
    gf.prikaz_kategorija(azuriranje_admin = True)
        
def azuriranje(k, idKat, brisanje_admin, azuriranje_admin):
    global korisnik
    print("-"*47)
    print("\nOpcije za ažuriranje:")
    print("-"*47)
    print("1) Ažuriranje vrednosti poena")
    print("2) Ažuriranje broja primeraka")
    print("3) Ažuriranje cene")
    print("4) Vratite se na početni meni\n")
    print("-"*47)
    opcija = eval(input("\nUnesite željenu opciju ---> "))
    print("\n{}".format("-"*47))
    if opcija == 1:
        poen = eval(input("\nUnesite novu vrednost poena za knjigu ---> "))
        crud.azuriranje_poena(k[0], poen)
    elif opcija == 2:
        primerci = eval(input("\nUnesite novi broj primeraka knjige ---> "))
        crud.azuriranje_primeraka(k[0], primerci)
    elif opcija == 3:
        cena = eval(input("\nUnesite novu cenu knjige ---> "))
        crud.azuriranje_cene(k[0], cena)
    elif opcija == 4:
        meni(korisnik)
        return;
    else:
        print("\nUnesite jednu od ponuđenih opcija!\n")
        prikaz_knjige(k, idKat, brisanje_admin, azuriranje_admin)
        return
    print("\n{}".format("-"*47))
    input("Ažuriranje je uspešno izvršeno!\nZa povratak na meni, pritisnite ENTER ---> ")
    print("\n{}".format("-"*47))
    meni(korisnik)
    return

def brisanje_knjige():
    gf.prikaz_kategorija(brisanje_admin = True)

def brisanje(k, idKat, brisanje_admin, azuriranje_admin):
    global korisnik
    if crud.nadji_knjigu_u_omiljenim(k[0]) or crud.nadji_knjigu_u_iznajmljenim(k[0]) or crud.nadji_knjigu_u_narudzbenicama(k[0]):
        input("Ne možemo izbrisati knjigu.\nZa povratak na meni, pritisnite ENTER ---> ")
        print("\n{}".format("-"*47))
        meni(korisnik)
        return
    else:
        input("Za nastavak sa brisanjem knjige, pritisnite ENTER ---> ")
        crud.izbrisi_knjigu(k[0])
        print("-"*47)
        print("\nUspešno ste izbrisali knjigu!\n")
        print("-"*47)
        meni(korisnik)
 
def dodavanje_knjige():
    global korisnik
    nova_knjiga = dict()
    nova_knjiga['naziv'] = input("Unesite naziv knjige: ")
    nova_knjiga['pisac'] = input("Unesite pisca: ")
    nova_knjiga['godina_izdanja'] = eval(input("Unesite godinu izdanja: "))
    nova_knjiga['poeni'] = eval(input("Unesite vrednost poena za izdavanje: "))
    nova_knjiga['primerci'] = eval(input("Unesite broj primeraka: "))
    nova_knjiga['opis'] = input("Unesite kratak opis: ")
    nova_knjiga['cena'] = eval(input("Unesite cenu knjige: "));
    kategorije = crud.sve_kategorije()
    okej = False
    kategorija = None
    while not okej:
        i = 1
        print("Sve kategorije: ")
        for k in kategorije:
            print("{}) {}".format(i, k[1]))
            i+=1
        kat = eval(input("Izaberite kategoriju kojoj knjiga pripada---> "))
        try:
            kategorija = kategorije[kat-1]
            okej = True
        except:
            print("Izaberite jednu od ponuđenih kategorija!")
            
    if crud.dodavanje_nove_knjige(nova_knjiga, kategorija[0]):
        print("Uspešno ste dodali novu knjigu!")
    else:
        print("Knjiga već postoji u bazi podataka!\nOtkazuje se dodavanje.")
    meni(korisnik)
       
    

