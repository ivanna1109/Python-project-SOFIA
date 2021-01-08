-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: pythondb
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `izdataknjiga`
--

DROP TABLE IF EXISTS `izdataknjiga`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `izdataknjiga` (
  `idIzdataKnjiga` int NOT NULL AUTO_INCREMENT,
  `Korisnik_idKorisnik` int NOT NULL,
  `Knjiga_idKnjiga` int NOT NULL,
  `datum_izdavanja` datetime NOT NULL,
  `rok_vracanja` datetime NOT NULL,
  PRIMARY KEY (`idIzdataKnjiga`),
  KEY `fk_Korisnik_has_Knjiga_Knjiga1_idx` (`Knjiga_idKnjiga`),
  KEY `fk_Korisnik_has_Knjiga_Korisnik1_idx` (`Korisnik_idKorisnik`),
  CONSTRAINT `fk_Korisnik_has_Knjiga_Knjiga1` FOREIGN KEY (`Knjiga_idKnjiga`) REFERENCES `knjiga` (`idKnjiga`),
  CONSTRAINT `fk_Korisnik_has_Knjiga_Korisnik1` FOREIGN KEY (`Korisnik_idKorisnik`) REFERENCES `korisnik` (`idKorisnik`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `izdataknjiga`
--

LOCK TABLES `izdataknjiga` WRITE;
/*!40000 ALTER TABLE `izdataknjiga` DISABLE KEYS */;
INSERT INTO `izdataknjiga` VALUES (1,1,7,'2021-01-02 19:44:08','2021-01-12 19:44:08'),(2,1,18,'2021-01-02 20:15:04','2021-01-12 20:15:04'),(3,2,13,'2021-01-02 20:34:19','2021-01-12 20:34:19'),(4,1,16,'2021-01-04 16:40:14','2021-01-14 16:40:14'),(5,5,16,'2021-01-05 13:03:50','2021-01-15 13:03:50');
/*!40000 ALTER TABLE `izdataknjiga` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kategorija`
--

DROP TABLE IF EXISTS `kategorija`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kategorija` (
  `idKategorija` int NOT NULL AUTO_INCREMENT,
  `naziv` varchar(45) NOT NULL,
  `opis` varchar(45) NOT NULL,
  PRIMARY KEY (`idKategorija`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kategorija`
--

LOCK TABLES `kategorija` WRITE;
/*!40000 ALTER TABLE `kategorija` DISABLE KEYS */;
INSERT INTO `kategorija` VALUES (1,'naučna fantastika','opis naucne fantastike'),(2,'triler','opis trilera'),(3,'ljubavni','opis ljubavni'),(4,'drama','opis drama'),(6,'horor','opis horor'),(7,'biografija','opis biografija'),(8,'komedija','opis komedije'),(9,'istorijske','opis istorijske'),(10,'poezija','opis poezija'),(11,'klasika','opis klasike');
/*!40000 ALTER TABLE `kategorija` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `knjiga`
--

DROP TABLE IF EXISTS `knjiga`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `knjiga` (
  `idKnjiga` int NOT NULL AUTO_INCREMENT,
  `naziv` varchar(45) NOT NULL,
  `pisac` varchar(45) NOT NULL,
  `godina_izdanja` varchar(45) NOT NULL,
  `vrednost_poena` int NOT NULL,
  `broj_primeraka` int NOT NULL,
  `kratak_opis` varchar(400) DEFAULT NULL,
  `cena` int NOT NULL,
  PRIMARY KEY (`idKnjiga`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `knjiga`
--

LOCK TABLES `knjiga` WRITE;
/*!40000 ALTER TABLE `knjiga` DISABLE KEYS */;
INSERT INTO `knjiga` VALUES (1,'Rat i mir','L. N. Tolstoj','2018',15,30,'Tolstoj daje sliku ruskog društva u Napoleonovo doba i prati živote tri glavna junaka: Pjera Bezuhova, nezakonitog sina seoskog kneza, koji neočekivano dobija pozamašno nasledstvo i titulu; kneza Andreja Bolkonskog, koji napušta porodicu da bi se borio u ratu protiv Napoleona; i Nataše Rostove, prelepe i čarobne devojke koja za Tolstoja oličenje savršene žene. ',1300),(2,'Roman o Londonu','Milos Crnjanski','2010',10,20,'Rjepnin i njegova supruga tumaraju gradom koji ih ne poznaje, pokušavaju da postoje u beznađu nepripadanja. A već na počeku njihove priče, pod žrvnjem svesti o tome šta znači ne biti niko, ukazuje se jezovit Rjepninov put ka izlazu iz očaja. Njegova neumitnost odrediće tok ovog epohalnog romana, opominjući modernog čoveka na njegovu sopstvenu bezdomnost u komešanju savremenog doba.',1200),(3,'Zločin i kazna','F.M. Dostojevski','2019',15,29,'Radnja romana Zločin i kazna se vrti oko mladog i siromašnog studenta Radiona Raskoljnikova koji ubija i pljačka bogatu staricu Aljonu Ivanovnu. ',1200),(4,'Hiljadu čudesnih sunaca','Haled Hoseini','2017',10,15,'Marijam je tek petnaest godina kada je šalju u Kabul da se uda za nesrećnog i ogorčenog Rašida, trideset godina starijeg od nje. Gotovo dve decenije kasnije, u zemlji koja ubrzano tone u propast, tragedija pogađa petnaestogodišnju Lejlu, koja mora da napusti svoj dom i stupi u Marijamino nesrećno domaćinstvo.',1000),(5,'Devojka od papira','Gijom Muso','2016',10,15,'Pre samo nekoliko meseci, Tom Bojd je imao sve u životu: bio je slavni pisac bestselera, živeo u mondenskom kvartu Los Anđelesa i uživao u srećnoj vezi sa svetski poznatom pijanistkinjom. Međutim, nakon ružnog raskida, Tom se zatvorio u svoj svet. Zbog slomljenog srca, ponestalo mu je inspiracije, a društvo mu prave samo poroci.',900),(6,'Sa pašnjaka do naučenjaka','Mihajlo I. Pupin','2015',10,10,'Autobiografija jednog od najvecih svetskih naucnika naseg doba, nagradjena prestiznpm Pulicerovovom nagradom! Knjiga koja se u SAD izucava kao obavezna lektira! Istinita prica o srpskom pastiru iz malog sela Idvor koji je postao jedan od preteca ere telekomunikacija.',900),(7,'Pink Flojd – Kad svinje polete','Mark Blejk','2017',10,15,'Spajajući mišljenja i uspomene očevidaca, ova knjiga prati priču grupe počev od njenih korena u Kembridžu do globalnog uspeha albumom The Dark Side Of the Moon i gorkog raspada osamdesetih godina XX veka, od njihovog istorijskog okupljanja na „Lajv ejtu“ do smrti osnivača Sida Bareta 2006. i sve nakon toga.',700),(8,'Digitalni ugljenik','Ričard Morgan','2013',5,10,'Bivši pripadnik Poslanstva UN Takeši Kovač ginuo je i ranije, ali njegova poslednja smrt bila je izuzetno bolna. Odaslan sto osamdeset svetlosnih godina od kuće, učitan u telo u Bej Sitiju, Kovač uranja u mračno srce mutne, dalekosežne zavere gnusne čak i po merilima društva koje se prema „postojanju“ ophodi kao prema nečemu što se može kupiti i prodati..',800),(9,'Problem tri tela','Liju Cisin','2019',10,19,'Nakon niza nerazjašnjenih ubistava koja potresaju naučnu zajednicu, fizičar Vang Miao pokušava da u virtuelnom svetu, koji naseljavaju Galileo, Njutn, Konfucije, Ajnštajn, reši astrodinamički problem tri tela. Pojava sablasnog časovnika i saznanje da je tokom Kulturne revolucije pokrenut tajni vojni projekat slanja signala u potrazi za vanzemaljcima.',800),(10,'Čovek po imenu Uve','Fredrik Bakman','2017',10,29,'Upoznajte Uvea. On je džangrizalo – jedan od onih koji upiru prstom u ljude koji mu se ne dopadaju kao da su provalnici zatečeni pod njegovim prozorom. Svakog jutra Uve ide u inspekciju po naselju u kom živi. Premešta bicikle i proverava da li je đubre pravilno razvrstano – iako je već nekoliko godina prošlo otkako je razrešen dužnosti predsednika kućnog saveta.',1000),(11,'Tito i ja','Goran Marković','2020',15,20,'Nezaboravni likovi dečaka Zorana i njegovih školskih drugova, tvrdokornog nastavnika Raje koji ih vodi na ekskurziju u Titov rodni kraj u Hrvatskom Zagorju, njihovih domaćina i vršnjaka koje Zoranov razred upoznaje na tom hodočašću u zapadne krajeve zemlje, humorno i melanholično evociraju detinjstvo i odrastanje čitavih generacija „Titovih pionira“, bez pomodnog odricanja od sosptvene prošlosti.',900),(12,'Savin osvetnik','Vanja Bulić','2020',15,30,'Inspiraciju za ovu priču Vanja Bulić nalazi u sukobu opštih duhovnih vrednosti, koje ovde simbolizuje ikona Svetog Save ostavljena na mestu zločina, i stvarnosti, koja je i dalje opterećena kriminalnim i zločinačkim nasleđem ratnih zbivanja devedesetih godina prošlog veka. Na tragu ovog sukoba naziru se i motivi zločina, u kom su svi akteri istovremeno i izvršioci i žrtve',1100),(13,'Smrt u Vavilonu, ljubav u Istanbulu','Iskender Pala','2019',10,14,'Od Hile do Istanbula, od Istanbula do Rima, celom Evropom, vrelim podnebljima Istoka, zaljubljena knjiga vekovima putuje tražeći svoju Lejlu. Menjajući gospodare, upoznajući pesnike i naučnike, velike putnike i moćne ličnosti, praćena lopovima koji žele zlato Vavilona i učenjacima koji žele tajne vavilonskih mudraca, ta knjiga o ljubavi i patnji posmatra kako i sam svet voli, pati i kako se menja.',800),(14,'Garavi sokak','Miroslav Antić','2018',15,29,'Garavi sokak je tinjajući venac slika o odrastanju i prebogatoj nemaštini, o bolnoj sreći i gutanju sudbine, o alhemiji tuge i kosmičkoj radosti. Bogata potresnim lirskim obrtima, ovo je jedinstvena zbirka u opusu originalnog pesnika.',700),(15,'Plavi žaket','Dusan Radović','2018',15,30,'Dušan Radović je pisao za mnoge medije: radio, televiziju, film, pozorište... Ovaj izbor iz tog opusa je nezaobilazan ako volite izazovne i neuobičajene prikaze složenosti ljudskih osećanja. Jer Radović je izuzetno duhovit u nadrealnim pričama, maestralan stilista u žanrovskom mešanju i poeziji, savršeni pesnik u dramskim minijaturama i apsurdnim scenama.',700),(16,'Uznemireni ljudi','Fredrik Bakman','2019',10,18,'Tokom razgledanja stana koji se nudi na prodaju jedan propali pljačkaš banke zaključaće se s iritantno entuzijastičnim agentom za prodaju nekretnina, dvojicom ogorčenih zavisnika od Ikee, trudnicom, samoubilački nastrojenim multimilionerom i prokletim zecom. Kada policija konačno bude upala u stan, zateći će ga... praznog.',800),(17,'Besnilo','Borislav Pekić','2011',15,30,'Biološka katastrofa, u razmerama nepoznatim savremenoj istoriji, pogađa londonski aerodrom Hitrou u jeku letnje sezone. Usled mutacije virusa besnila u jednoj naučnoj laboratoriji, epidemija se širi zastrašujućom brzinom jer nijedna vakcina ne deluje. U karantinu, koji obuhvata ogroman kompleks, zateklo se na desetine hiljada putnika i nameštenika aerodroma',900),(18,'Grozničavi san','Džordž R. R. Martin','2017',15,20,'Kada Abner Marš, propali rečni kapetan i brodovlasnik, dobije ponudu da se uortači s bogatim aristokratom, posumnjaće da tu nešto smrdi. A kada se upozna sa avetinjski bledim Džošuom Jorkom, čovekom čeličnosivih očiju, znaće da je bio u pravu. Jer Jorka nije briga što je ledena zima 1857. zbrisala gotovo sve Maršove brodove s lica zemlje.',900),(19,'Veliki Getsbi','F. Skot Ficdžerald','2011',10,20,'Treba biti Frensis Skot Ficdžerald pa umeti sa malo reči reći velike i važne stvari. Radnja romana dešava se dvadesetih godina XX veka – u doba džeza – kako ga Ficdžerald naziva, i prikaz je razočaranja urbane populacije u američki san.',1200);
/*!40000 ALTER TABLE `knjiga` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `knjiga_has_kategorija`
--

DROP TABLE IF EXISTS `knjiga_has_kategorija`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `knjiga_has_kategorija` (
  `Knjiga_idKnjiga` int NOT NULL,
  `Kategorija_idKategorija` int NOT NULL,
  PRIMARY KEY (`Knjiga_idKnjiga`,`Kategorija_idKategorija`),
  KEY `fk_Knjiga_has_Kategorija_Kategorija1_idx` (`Kategorija_idKategorija`),
  KEY `fk_Knjiga_has_Kategorija_Knjiga1_idx` (`Knjiga_idKnjiga`),
  CONSTRAINT `fk_Knjiga_has_Kategorija_Kategorija1` FOREIGN KEY (`Kategorija_idKategorija`) REFERENCES `kategorija` (`idKategorija`),
  CONSTRAINT `fk_Knjiga_has_Kategorija_Knjiga1` FOREIGN KEY (`Knjiga_idKnjiga`) REFERENCES `knjiga` (`idKnjiga`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `knjiga_has_kategorija`
--

LOCK TABLES `knjiga_has_kategorija` WRITE;
/*!40000 ALTER TABLE `knjiga_has_kategorija` DISABLE KEYS */;
INSERT INTO `knjiga_has_kategorija` VALUES (8,1),(9,1),(18,1),(12,2),(17,2),(5,3),(13,3),(4,4),(10,4),(11,4),(13,4),(16,4),(19,4),(17,6),(18,6),(6,7),(7,7),(10,8),(16,8),(13,9),(14,10),(15,10),(1,11),(2,11),(3,11);
/*!40000 ALTER TABLE `knjiga_has_kategorija` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `korisnik`
--

DROP TABLE IF EXISTS `korisnik`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `korisnik` (
  `idKorisnik` int NOT NULL AUTO_INCREMENT,
  `korisnicko_ime` varchar(45) NOT NULL,
  `sifra` varchar(45) NOT NULL,
  `ime` varchar(45) NOT NULL,
  `prezime` varchar(45) NOT NULL,
  `adresa` varchar(45) NOT NULL,
  `broj_poena` int DEFAULT NULL,
  `Uloga_idUloga` int NOT NULL,
  PRIMARY KEY (`idKorisnik`,`Uloga_idUloga`),
  KEY `fk_Korisnik_Uloga_idx` (`Uloga_idUloga`),
  CONSTRAINT `fk_Korisnik_Uloga` FOREIGN KEY (`Uloga_idUloga`) REFERENCES `uloga` (`idUloga`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `korisnik`
--

LOCK TABLES `korisnik` WRITE;
/*!40000 ALTER TABLE `korisnik` DISABLE KEYS */;
INSERT INTO `korisnik` VALUES (1,'lexa','asdf123','Aleksa','Novkovic','bul. despota Stefana 5a',75,1),(2,'ivanaCar','asdf123','Ivana','Milutinovic','bul. despota Stefana 5a',90,1),(3,'radnik1','radnik1','Mile','Milovanovic','Somborska 3',NULL,2),(5,'lakica','lakica','Lana','Slovic','Prijepoljska 2',90,1),(6,'kuzmo','kuzmOo321','Zoran','Kuzmanovic','Zvornicka 51',100,1),(7,'maki11','Maki123','Marija','Milutinovic','Banjska 12',100,1),(8,'radnik2','radnik2','Jovana','Jovic','Prizrenska 35a',NULL,2);
/*!40000 ALTER TABLE `korisnik` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `narudzbenica`
--

DROP TABLE IF EXISTS `narudzbenica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `narudzbenica` (
  `idNarudzbenica` int NOT NULL AUTO_INCREMENT,
  `Korisnik_idKorisnik` int NOT NULL,
  `Knjiga_idKnjiga` int NOT NULL,
  `cena` int NOT NULL,
  `datum` datetime NOT NULL,
  PRIMARY KEY (`idNarudzbenica`),
  KEY `fk_Korisnik_has_Knjiga_Knjiga3_idx` (`Knjiga_idKnjiga`),
  KEY `fk_Korisnik_has_Knjiga_Korisnik3_idx` (`Korisnik_idKorisnik`),
  CONSTRAINT `fk_Korisnik_has_Knjiga_Knjiga3` FOREIGN KEY (`Knjiga_idKnjiga`) REFERENCES `knjiga` (`idKnjiga`),
  CONSTRAINT `fk_Korisnik_has_Knjiga_Korisnik3` FOREIGN KEY (`Korisnik_idKorisnik`) REFERENCES `korisnik` (`idKorisnik`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `narudzbenica`
--

LOCK TABLES `narudzbenica` WRITE;
/*!40000 ALTER TABLE `narudzbenica` DISABLE KEYS */;
INSERT INTO `narudzbenica` VALUES (1,1,13,800,'2021-01-02 20:07:08'),(7,5,10,1000,'2021-01-04 16:51:38'),(8,2,14,700,'2021-01-05 13:09:34'),(9,2,3,1200,'2021-01-05 13:14:08'),(10,7,9,800,'2021-01-05 18:37:52'),(11,5,14,700,'2021-01-06 18:37:52');
/*!40000 ALTER TABLE `narudzbenica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `omiljenaknjiga`
--

DROP TABLE IF EXISTS `omiljenaknjiga`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `omiljenaknjiga` (
  `Korisnik_idKorisnik` int NOT NULL,
  `Knjiga_idKnjiga` int NOT NULL,
  KEY `fk_Korisnik_has_Knjiga_Knjiga2_idx` (`Knjiga_idKnjiga`),
  KEY `fk_Korisnik_has_Knjiga_Korisnik2_idx` (`Korisnik_idKorisnik`),
  CONSTRAINT `fk_Korisnik_has_Knjiga_Knjiga2` FOREIGN KEY (`Knjiga_idKnjiga`) REFERENCES `knjiga` (`idKnjiga`),
  CONSTRAINT `fk_Korisnik_has_Knjiga_Korisnik2` FOREIGN KEY (`Korisnik_idKorisnik`) REFERENCES `korisnik` (`idKorisnik`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `omiljenaknjiga`
--

LOCK TABLES `omiljenaknjiga` WRITE;
/*!40000 ALTER TABLE `omiljenaknjiga` DISABLE KEYS */;
INSERT INTO `omiljenaknjiga` VALUES (1,15),(1,16),(5,15),(7,15),(6,15),(6,13),(6,6),(7,5);
/*!40000 ALTER TABLE `omiljenaknjiga` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `uloga`
--

DROP TABLE IF EXISTS `uloga`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `uloga` (
  `idUloga` int NOT NULL AUTO_INCREMENT,
  `naziv` varchar(45) NOT NULL,
  `plata` int DEFAULT NULL,
  PRIMARY KEY (`idUloga`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uloga`
--

LOCK TABLES `uloga` WRITE;
/*!40000 ALTER TABLE `uloga` DISABLE KEYS */;
INSERT INTO `uloga` VALUES (1,'Registrovani',NULL),(2,'Radnik',30000);
/*!40000 ALTER TABLE `uloga` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-08 16:40:42
