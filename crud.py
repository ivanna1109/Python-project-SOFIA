import mysql.connector
import datetime as dt

db = mysql.connector.connect(host='localhost',user='root', password='ivanna1109', database='pythondb')

kursor = db.cursor()

def pronadji_korisnika(user, passw):
    vrednosti = (user, passw)
    kursor.execute("select * from Korisnik where korisnicko_ime like %s and sifra like %s", vrednosti)
    korisnik = kursor.fetchall()
    if korisnik:
        return korisnik[0]
    return 0

def registrovanje_korisnika(korisnicko_ime, sifra1, ime, prezime, adresa):
    vrednosti = (korisnicko_ime, sifra1, ime, prezime, adresa, 100, 1)
    kursor.execute('insert into Korisnik (korisnicko_ime, sifra, ime, prezime, adresa, broj_poena, Uloga_idUloga) \
                     values (%s, %s, %s, %s, %s, %s, %s)', vrednosti)
    db.commit()

def sve_kategorije():
    kursor.execute('select * from Kategorija')
    return kursor.fetchall()

def sve_knjige_za_kat(idKat):
    kursor.execute('select * from Knjiga where idKnjiga in (select Knjiga_has_Kategorija.Knjiga_idKnjiga from Knjiga_has_Kategorija\
                   where Knjiga_has_kategorija.Kategorija_idKategorija like %s)' , (idKat,))
    return kursor.fetchall()

def proveri_omiljene(idK, idKnjige):
    vrednosti = (idK, idKnjige)
    kursor.execute('select * from OmiljenaKnjiga where Korisnik_idKorisnik like %s and Knjiga_idKnjiga like %s', vrednosti)
    if kursor.fetchall():
        return True
    return False

def dodaj_omiljene(idK, idKnjige):
    if proveri_omiljene(idK, idKnjige):
        return False
    vrednosti = (idK, idKnjige)
    kursor.execute('insert into OmiljenaKnjiga (Korisnik_idKorisnik, Knjiga_idKnjiga) \
                     values (%s, %s)', vrednosti)
    db.commit()
    return True

def omiljene_knjige(idKorisnika):
    vrednost = (idKorisnika,)
    kursor.execute('select * from OmiljenaKnjiga where Korisnik_idKorisnik like %s', vrednost)
    return kursor.fetchall()

def narucene(idKorisnika):
    vrednost = (idKorisnika,)
    kursor.execute('select * from Narudzbenica where Korisnik_idKorisnik like %s', vrednost)
    return kursor.fetchall()


def nadji_knjigu(idKnjige):
    vrednost = (idKnjige,)
    kursor.execute('select * from Knjiga where idKnjiga like %s', vrednost)
    knjiga = kursor.fetchall()
    if knjiga:
        return knjiga[0]
    return None

def iznajmi_knjigu(idK, poeniKorisnika, idKnjige,  poeni, primerci):
    vrednosti = (idK, idKnjige, dt.datetime.now(), dt.datetime.now()+dt.timedelta(10))
    kursor.execute('insert into IzdataKnjiga (Korisnik_idKorisnik, Knjiga_idKnjiga, datum_izdavanja, rok_vracanja) \
                     values (%s, %s, %s, %s)', vrednosti)
    vrednosti = (poeniKorisnika - poeni, idK)
    kursor.execute('update Korisnik set broj_poena = %s where idKorisnik = %s', vrednosti)
    vrednosti = (primerci-1, idKnjige)
    kursor.execute('update Knjiga set broj_primeraka = %s where idKnjiga = %s', vrednosti)
    db.commit()
    
def naruci_knjigu(idK, idKnjige, primerci, cena):
    vrednosti = (idK, idKnjige, dt.datetime.now(), cena)
    kursor.execute('insert into Narudzbenica (Korisnik_idKorisnik, Knjiga_idKnjiga, datum, cena) values (%s, %s, %s, %s)', vrednosti)
    vrednosti = (primerci-1, idKnjige)
    kursor.execute('update Knjiga set broj_primeraka = %s where idKnjiga = %s', vrednosti)
    db.commit()
    
#crud operacije za radnika
def lista_korisnika():
    kursor.execute('select * from Korisnik where Uloga_idUloga not like 2')
    return kursor.fetchall()

def dodavanje_nove_knjige(nova_knjiga, kat):
    vrednost = (nova_knjiga['naziv'],)
    kursor.execute('select * from Knjiga where naziv like %s', vrednost)
    if kursor.fetchall():
        return False
    vrednost = (nova_knjiga['naziv'], nova_knjiga['pisac'], nova_knjiga['godina_izdanja'], nova_knjiga['poeni'], nova_knjiga['primerci'], nova_knjiga['opis'], nova_knjiga['cena'])
    kursor.execute('insert into Knjiga (naziv, pisac, godina_izdanja, vrednost_poena, broj_primeraka, kratak_opis, cena)\
                   values (%s, %s, %s, %s, %s, %s, %s)', vrednost)
    db.commit()
    vrednost = (nova_knjiga['naziv'],)
    kursor.execute('select * from Knjiga where naziv like %s', vrednost)
    knjiga = kursor.fetchall()[0]
    vrednost = (knjiga[0], kat)
    kursor.execute('insert into Knjiga_has_Kategorija (Knjiga_idKnjiga, Kategorija_idKategorija) values (%s,%s)', vrednost)
    db.commit()
    return True

def azuriranje_poena(idKnjige, poeni):
    vrednosti = (poeni, idKnjige)
    kursor.execute('update Knjiga set vrednost_poena = %s where idKnjiga = %s', vrednosti)
    db.commit()
    
def azuriranje_primeraka(idKnjige, primerci):
    vrednosti = (primerci, idKnjige)
    kursor.execute('update Knjiga set broj_primeraka = %s where idKnjiga = %s', vrednosti)
    db.commit()
    
def azuriranje_cene(idKnjige, cena):
    vrednosti = (cena, idKnjige)
    kursor.execute('update Knjiga set cena = %s where idKnjiga = %s', vrednosti)
    db.commit()
    
def nadji_knjigu_u_omiljenim(idKnjige):
    vrednost = (idKnjige,)
    kursor.execute('select * from OmiljenaKnjiga where Knjiga_idKnjiga = %s', vrednost)
    if kursor.fetchall():
        return True
    return False

def nadji_knjigu_u_iznajmljenim(idKnjige):
    vrednost = (idKnjige,)
    kursor.execute('select * from IzdataKnjiga where Knjiga_idKnjiga like %s', vrednost)
    if kursor.fetchall():
        return True
    return False

def nadji_knjigu_u_narudzbenicama(idKnjige):
    vrednost = (idKnjige, )
    kursor.execute('select * from Narudzbenica where Knjiga_idKnjiga = %s', vrednost)
    if kursor.fetchall():
        return True
    return False

def izbrisi_knjigu(idKnjiga):
    vrednost = (idKnjiga, )
    try:
        kursor.execute('delete from Knjiga_has_Kategorija where Knjiga_idKnjiga = %s', vrednost)
        db.commit()
    except Exception as e:
        print("Exception u brisanju u Knjiga has kategorija: {}".format(e))
    try:
        kursor.execute("delete from Knjiga where (idKnjiga like '%s')", vrednost)
        db.commit()
    except Exception as e:
        print("Exception u brisanju knjige: {}".format(e))
    
    
def izdate_chart():
    sql = "select distinct Korisnik_idKorisnik from IzdataKnjiga"
    kursor.execute(sql)
    korisnici = kursor.fetchall()
    recnik = dict()
    for k in korisnici:
        sql = "select count(Knjiga_idKnjiga) from IzdataKnjiga where Korisnik_idKorisnik like %s"
        kursor.execute(sql, k)
        broj_za_k = kursor.fetchall()[0]
        recnik[k[0]] = broj_za_k[0]
    return recnik

def omiljene_chart():
    try:
        kursor.execute("select distinct Knjiga_idKnjiga from OmiljenaKnjiga")
        knjige = kursor.fetchall()
    except Exception as e:
        print("Greska u pribavljanju omiljenih knjiga: {}".format(e))
    recnik = dict()
    if knjige:
        for k in knjige:
            try:
                sql = "select count(Korisnik_idKorisnik) from OmiljenaKnjiga where Knjiga_idKnjiga like %s"
                kursor.execute(sql, k)
                broj_korisnika_knjige = kursor.fetchall()[0]
                recnik[k[0]] = broj_korisnika_knjige[0]
            except Exception as e:
                print("Exception u brojanju korisnika: {}".format(e))
    return recnik

def najprodavanije_chart():
    try:
        kursor.execute('select distinct Knjiga_idKnjiga from Narudzbenica')
        knjige = kursor.fetchall()
    except Exception as e:
        print("Greska u pribavljanju knjiga iz narudzbenice: {}".format(e))
    recnik = dict()
    if knjige:
        for k in knjige:
            try:
                sql = "select sum(cena) from Narudzbenica where Knjiga_idKnjiga = %s"
                kursor.execute(sql, k)
                suma_prihoda = kursor.fetchall()[0]
                recnik[k[0]] = int(suma_prihoda[0])
            except Exception as e:
                print("Exeption u sumiranju prihoda: {}".format(e))
    return recnik