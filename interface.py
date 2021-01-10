import crud as crud
import interface_user as user
import interface_admin as admin
import globalne_funkc as gf
import re

trenutni_korisnik = None

def pocetni_meni():
    dobrodoslica()
    print("\n{}Početni meni{}".format("-"*17, "-"*18))
    print("\n1) Uloguj se \n2) Registruj se \n3) Završi program\n")
    print("-"*47)
    opc = eval(input("Unesite željenu opciju ---> "))
    print("\n{}".format("-"*47))
    if opc == 1:
        logovanje()
    elif opc == 2:
        registrovanje()
    elif opc == 3:
        gf.zavrsi_program()
    else:
        print("\nUnesite jednu od ponuđenih opcija!!!\n")
        pocetni_meni() 
        
def dobrodoslica():
    print("="*47)
    print("{:<46}|".format("|"))
    print("{:<5} DOBRO DOŠLI U IZDAVAČKU KUĆU 'SOFIA' {:>4}".format("|", "|"))
    print("{:<46}|".format("|"))
    print("="*47)

def logovanje():
    global trenutni_korisnik 
    account = input("Unesite korisničko ime: ")
    passw = input("Unesite šifru: ")
    print("\n{}".format("-"*47))
    trenutni_korisnik = crud.pronadji_korisnika(account, passw)
    try:
        uloga = trenutni_korisnik[7]
    except:
        uloga = 3
    if uloga == 1:
        print("\n{}".format("-"*47))
        print("Zdravo, {}! Uspešno ste se ulogovali!".format(trenutni_korisnik[3]))
        print("-"*47)
        gf.inicijalno(trenutni_korisnik)
        user.meni(trenutni_korisnik)
    elif uloga == 2:
        print("\n{}".format("-"*47))
        print("Zdravo, {}! Uspešno ste se ulogovali!".format(trenutni_korisnik[3]))
        print("-"*47)
        gf.inicijalno(trenutni_korisnik)
        admin.meni(trenutni_korisnik)
    else:
        print("{}".format("-"*47))
        print("\nNeuspešno logovanje!\n")
        print("{}".format("-"*47))
        print("\n1) Pokušajte ponovo\n2) Vratite se na početni meni")
        print("\n{}".format("-"*47))
        opc = eval(input("Unesite željenu opciju ---> "))
        print("\n{}".format("-"*47))
        if opc == 1:
            logovanje()
            return
        else:
            pocetni_meni()


def registrovanje():
    korisnicko_ime = input("Unesite korisničko ime: ")
    sifra1 = input("Unesite šifru: ")
    while not re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,10}$", sifra1):
        print("Šifra mora sadržati velika i mala slova, brojeve i biti dužine bar 6. Pokušajte ponovo.")
        sifra1 = input("Unesite šifru: ");
    sifra2 = input("Potvrdite unetu šifru: ");
    while sifra1 != sifra2:
        print("Nepoklapaju se šifre, probajte ponovo!")
        sifra1 = input("Unesite šifru: ")
        while not re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,10}$", sifra1):
            print("Šifra mora sadržati velika i mala slova, brojeve i biti dužine bar 6. Pokušajte ponovo.")
            sifra1 = input("Unesite sifru: ");
        sifra2 = input("Potvrdite unetu šifru: ");
    ime_prezime = input("Unesite ime i prezime: ")
    while not ime_prezime.split(" "):
        print("Ime i prezime mora biti odvojeno razmakom!")
        ime_prezime = input("Unesite ime i prezime: ")
    ime, prezime = ime_prezime.split(" ")
    adresa = input("Unesite adresu: ")
    crud.registrovanje_korisnika(korisnicko_ime, sifra1, ime, prezime, adresa)
    print("Uspešno ste se registrovali!")
    pocetni_meni()
    



    