from modules.search import *
from modules.book_module import *
import modules.login
import os
import time
from random import randint

global book_list
global bill
global price
book_list = []
bill = []

def bill_menu():
	"""Meni racuna."""
	x = True
	while x is True:
		print("Opcije:\n\n1.Dodaj na racun\n2.Otvori racun\n\n3.Povratak na glavni meni")
		ak = input("\nOdaberite opciju: ")
		if ak == "1":
			add_to_bill()
			x = False
		elif ak == "2":
			bill_open()
			x = False
		elif ak == "3":
			os.system("cls")
			x = False
		else:
			error("Neodogavarjuc unos!", 1.5)


def add_to_bill():
	"""Dodavanje knjige na racun."""
	global book_list
	global bill
	bk = {}
	os.system("cls")
	book_extract()
	print("="*60)
	x = True
	while x is True:
		isbn = input("Unesite ISBN: ")
		for book in book_list:
			if "1" in book["Stanje"]:
				os.system("cls")
				if isbn == book["ISBN"]:
					print("Knjiga: " + book["Autor"] + " - " + book["Naslov"] + "\nISBN: " + book["ISBN"] + 
					"\nRaspolozivo knjiga: " + book["Kolicina"])
					x = False
					while x is False:
						kol = input("\nKolicina: ")
						if kol.isdigit() and int(kol) > 0:
							if int(kol) > int(book["Kolicina"]) or book["Kolicina"] == 0:
								os.system("cls")
								print("Nema dovoljno knjiga na stanju.")
							else:
								book["Kolicina"] = int(book["Kolicina"]) - int(kol)
								book_update()
								bk["ime"] = book
								bk["kol"] = kol
								bill.append(bk)
								book_list = []
								break
						else:
							os.system("cls")
							print("Neodgovarajuc unos")
	os.system("cls")
	print("Knjiga je dodata na racun.\n\n1. Dodaj jos knjiga\n2. Otvori racun\n2. Povratak na meni")
	ak = input("\nOdaberite opciju: ")
	if ak == "1":
		add_to_bill()
	elif ak == "2":
		bill_open()
	elif ak == "3":
		os.system("cls")
		x = False

def bill_open():
	"""Otvaranje racuna. Postoji opcija za stampanje
	i brisanje racuna."""
	global bill
	global price
	price = 0
	os.system("cls")
	print("{:^86}\n".format("Racun:"))
	print("---" + "{:-^20}{:-^25}{:-^8}{:-^15}{:-^15}".format("Autor", "Naslov",
	 "Cena", "ISBN", "Kvantitet") )
	num = 1
	for m in bill:
		price += float(m["ime"]["Cena"]) * float(m["kol"])
		print(str(num) + ".)" + "{:^20}{:^25}{:^8}{:^15}{:^15}".format(m["ime"]["Autor"], 
			m["ime"]["Naslov"], m["ime"]["Cena"], m["ime"]["ISBN"], m["kol"]))
		num += 1
	print("="*86)
	print("\nProdavac: " + modules.login.kor["Ime"] + " " + modules.login.kor["Prezime"])
	print("\nUkupna cena: " + str(price) + " din")
	x = True
	while x is True:
		print("\n\n1. Stampaj racun\n2. Dodaj jos knjiga\n3. Isprazni racun\n4. Povratak na meni")
		ak = input("\nOdaberite opciju: ")
		if ak == "1":
			bill_publish()
			error("Uspesno ste izvrsili prodaju." , 2)
			bill_open()
			x = False
		elif ak == "2":
			add_to_bill()
		elif ak == "3":
			os.system("cls")
			bill = []
			bill_open()
		elif ak == "4":
			os.system("cls")
			bill_menu()
			x = False
		else:
			os.system("cls")
			print("Pogresan unos!")

def bill_publish():
	"""Stampanje racuna. Racun se upisuje 
	u arhivu i privremeni racun za stampanje."""
	br_racuna = randint(100000,999999)
	ti = time.strftime("%H:%M:%S")
	da = time.strftime("%d/%m/%Y")
	f = open("bills/bill.txt", "w")
	f.write("{:=^56}\n".format("Knjizara Vulkan"))
	f.write("\nProdavac: " + modules.login.kor["Ime"] + " " + modules.login.kor["Prezime"] + "\n")
	f.write(str(ti) + "\n")
	f.write(str(da) + "\n")
	f.write("-" * 56)
	for m in bill:
		f.write("\n\n" + m["ime"]["Autor"] + " -- " + m["ime"]["Naslov"] + "  " + m["ime"]["Cena"] + " RSD" + "  X  " + m["kol"])
	f.write("\n\n" + "-" * 56)
	f.write("\nCena: " + str(price) + "RSD")
	f.write("\n\nBroj racuna: " + str(br_racuna))
	f.write("\n\nHvala na poverenju.")
	f.write("\n" + "=" * 56)
	f.close()

	a = open("bills/archive.txt", "a")
	a.write("\n\n{:=^56}\n".format("Br. racuna: " + str(br_racuna)))
	a.write("\nProdavac: " + modules.login.kor["Ime"] + " " + modules.login.kor["Prezime"] + "\n")
	a.write(str(ti) + "\n")
	a.write(str(da) + "\n")
	a.write("-" * 56)
	for m in bill:
		a.write("\n" + m["ime"]["Autor"] + " -- " + m["ime"]["Naslov"] + "  " + m["ime"]["Cena"] + " RSD" + "  X  " + m["kol"])
	a.write("\n" + "-" * 56)
	a.write("\nCena: " + str(price) + " RSD")
	a.write("\n" + "=" * 56)
	a.close()
	
def book_extract():
	"""Funkcija otpakuje knjige iz baze
	i upisuje u listu."""
	f = open("data/books.txt", "r")
	for line in f:
		book_dict = {}
		line = line.strip()
		line = line.strip("\n")
		line = line.split("|")
		i = 0
		try:
			for x in book_data:
				book_dict[x] = line[i]
				i += 1
		except IndexError:
			print("Detektovana greska u bazi podataka\nPodaci sa greskom nece biti ispisani")
		book_list.append(book_dict)	

def book_update():
	"""Nadogradnja knjiga u bazu nakon neke izmene.""" 
	file_form = ""
	for book in book_list:
		for k in range(len(book_data) - 1):
		    file_form += "{}|".format(book[book_data[k]])
		file_form += "{}\n".format(book[book_data[-1]])

	f = open("data/books.txt", "w")
	f.write(file_form)
	f.close()