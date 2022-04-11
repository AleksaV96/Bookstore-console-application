from modules.book_module import *
from modules.users import *
from modules.search import *
from modules.bills import *
import os
import os
import time


users = []

global kor
kor = {}

def login():
        """Login funkcija, detektuje dal je pogresno
        korisnicko ime ili lozinka. Dozvoljava
        neogranicen broj ponavljanja lozinke."""
        user_extract()
        x = False
        while x is False:
                kor_ime = input("Korisnicko ime:\n")
                print("-"*15)
                for korisnik in users:
                        if korisnik["Korisnicko ime"] == kor_ime:
                                x = True
                                pass_counter = 4
                                while x is True:
                                        lozinka = input("Lozinka:\n")
                                        pass_counter -= 1
                                        if pass_counter < 1:
                                                error("Pogresna lozinka!\n\nPreostalo pokusaja: " + str(pass_counter), 1.5)
                                                pass_error()
                                        else:
                                                if korisnik["Lozinka"] == str(lozinka): 
                                                        x = False
                                                        os.system("cls")
                                                        if korisnik["Uloga"] == "Menadzer":
                                                                kor["Ime"] = korisnik["Ime"]
                                                                kor["Prezime"] = korisnik["Prezime"]
                                                                kor["Uloga"] = korisnik["Uloga"]
                                                                menu_m()
                                                                return True

                                                        elif korisnik["Uloga"] == "Prodavac":
                                                                kor["Ime"] = korisnik["Ime"]
                                                                kor["Prezime"] = korisnik["Prezime"]
                                                                kor["Uloga"] = korisnik["Uloga"]
                                                                menu_t()
                                                                return True
                                                os.system("cls")
                                                print("Pogresna lozinka! Pokusajte ponovo.")
                                                print("\nPreostalo pokusaja: " + str(pass_counter) + "\n")
                                                time.sleep(2)
                                                os.system("cls")

                error("Korisnicko ime ne postoji!", 2)

def pass_error():
        """Funkcija gasi softver pri
        3 neuspela pokusaja unosa lozinke."""
        os.system("cls")
        print("Detektovana zloupotreba softvera! Gasennje za...")
        time.sleep(1)
        for i in range(5, -1, -1):
                print(str(i) + "...")
                time.sleep(1)
        exit()

def user_extract():
        f = open("data/users.txt", "r")
        for line in f:
                user_dict = {}
                line = line.strip()
                line = line.strip("\n")
                line = line.split("|")
                i = 0
                for x in user_data:
                        user_dict[x] = line[i]
                        i += 1
                users.append(user_dict)


def menu_m():
        """Menadzerski meni. Ovaj meni
        se prikazuje korisnicima cije je
        uloga definisana kao menadzer.
        Neke funkcije su jos u izradi."""
        print("Ime/Prezime: " + kor["Ime"] + " " + kor["Prezime"])
        print("Ovlascenje: " + kor["Uloga"] + "\n")
        options = ["1.Pretraga i menjanje knjiga", "2.Dodavanje knjiga/korisnika", "3.Izloguj se", "4.Izlaz iz aplikacije"] 
        for opt in options:
                print(opt)
        opt_num = input("\nOdaberite redni broj opcije:\n")
        if opt_num.isdigit():
                if int(opt_num) <5 and int(opt_num) >0:
                        if int(opt_num) == 1:
                                book_data_menu()
                                os.system("cls")
                                menu_m()
                        elif int(opt_num) == 2:
                                os.system("cls")
                                print("1.Dodaj knjigu\n2.Dodaj novog korisnika\n3.Povratak na meni")
                                opt_num1 = input("\nOdaberite redni broj opcije:\n")
                                if int(opt_num1) == 1:
                                        os.system("cls")
                                        book_add()
                                        ak = input("\nPritisnite enter za povratak na glavni meni ")
                                        os.system("cls")
                                        menu_m()
                                elif int(opt_num1) == 2:
                                        os.system("cls")
                                        user_add()
                                        ak = input("\nPritisnite enter za povratak na glavni meni: ")
                                        os.system("cls")
                                        menu_m()
                                elif int(opt_num1) == 3:
                                        os.system("cls")
                                        menu_m()
                                else:
                                        error("Opcija ne postoji!", 1.5)
                                        menu_m()
                        elif int(opt_num) == 3:
                                os.system("cls")
                                yn = input("Da li ste sigurni? Y/N: \n")
                                if yn == "Y" or yn == "y":
                                        os.system("cls")
                                        login()
                                elif yn == "N" or yn == "n":
                                        os.system("cls")
                                        menu_m()
                        elif int(opt_num) == 4:
                                os.system("cls")
                                yn = input("Da li ste sigurni? Y/N: \n")
                                if yn == "Y" or yn == "y":
                                        exit()
                                elif yn == "N" or yn == "n":
                                        os.system("cls")
                                        menu_m()

                else:
                        error("Odabrali se nepostojucu opciju!", 1.5)
                        menu_m()
        else:
                error("Dozvoljen je unos samo brojeva!", 1.5)
                menu_m()

def menu_t():
        """Trgovacki meni. Ovaj meni
        se prikazuje korisnicima cije je
        uloga definisana kao trgovac.
        Neke funkcije su jos u izradi."""
        print("Ime/Prezime: " + kor["Ime"] + " " + kor["Prezime"])
        print("Ovlascenje: " + kor["Uloga"] + "\n")
        options = ["1.Pretraga knjiga", "2.Prodaja knjiga", "3.Izloguj se", "4.Izlaz iz aplikacije"]
        for opt in options:
                print(opt)
        opt_num = input("\nOdaberite redni broj opcije:\n")
        if opt_num.isdigit():
                if int(opt_num) <5 and int(opt_num) >0: 
                        if int(opt_num) == 1:
                                search_menu_1()
                                os.system("cls")
                                menu_t()
                        elif int(opt_num) == 2:
                                os.system("cls")
                                bill_menu()
                                menu_t()

                        elif int(opt_num) == 3:
                                os.system("cls")
                                yn = input("Da li ste sigurni? Y/N: \n")
                                if yn == "Y" or yn == "y":
                                        os.system("cls")
                                        login()
                                elif yn == "N" or yn == "n":
                                        os.system("cls")
                                        menu_m()
                        elif int(opt_num) == 4:
                                os.system("cls")
                                yn = input("Da li ste sigurni? Y/N:\n")
                                if yn == "Y" or yn == "y":
                                        exit()
                                elif yn == "N" or yn == "n":
                                        os.system("cls")
                                        menu_t()
                else:
                        error("Odabrali ste nepostojucu opciju!", 1.5)
                        menu_t()
        else: 
                error("Dozvoljen je unos samo brojeva!", 1.5)
                menu_t()