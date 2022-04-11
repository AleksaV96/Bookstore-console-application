from modules.book_module import *
import os
import copy

def book_data_menu():
	"""Meni za pretragu knjiga."""
	os.system("cls")
	print("OPCIJE:\n\n1.)Pretraga knjiga\n2.)Pretraga i menjanje knjiga\n\n3.)Povratak na glavni meni")
	x = False
	while x is False:
		ak = input("\nOdaberite broj opicije: ")
		ak = ak.strip(" ")
		if ak == "":
			error("Unos ne sme biti prazan!", 2)
		else:
			if ak.isdigit():
				if int(ak) == 1:
					search_menu_1()
					x = True
				if int(ak) == 2:
					search_menu_2()
					x = True
				if int(ak) == 3:
					x = True
			else:
				error("Unos mora biti broj!", 2)


def search_menu_1():
	"""Pretraga knjiga bez menjanja. Kjuc 
	se prosledjuje kao parametar prema kojem se 
	pretrazuje."""
	global book_list
	book_list = []
	book_extract()
	os.system("cls")
	x = True
	while x is True:
		print("     Pretraga knjiga:")
		print("="*26)
		print("1.Pretraga po ISBN-u")
		print("2.Pretraga po naslovu")
		print("3.Pretraga po autoru")
		print("4.Pretraga po zanru")
		print("\n5.Povratak na glavni meni")
		opcija = input("\nOdaberite redni broj opcije pretrage:\n")
		num_test = opcija.isdigit()
		if int(opcija) > 5 or int(opcija) < 1:
			error("Odabrali ste nepostojucu opciju", 1.5)
		elif num_test is False:
			error("Unos mora biti broj", 1.5)
		elif int(opcija) == 1:
			search_engine("ISBN")
			x = False
		elif int(opcija) == 2:
			search_engine("Naslov")
			x = False
		elif int(opcija) == 3:
			search_engine("Autor")
			x = False
		elif int(opcija) == 4:
			search_genre()
			x = False
		elif int(opcija) == 5:
			book_data_menu()
			x = False

def search_menu_2():
	"""Pretraga knjiga bez menjanja. Kjuc 
	se prosledjuje kao parametar prema kojem se 
	pretrazuje - sa menjanjem parametara."""
	global book_list
	book_list = []
	book_extract()
	os.system("cls")
	x = True
	while x is True:
		print("     Pretraga knjiga:")
		print("="*26)
		print("1.Pretraga po ISBN-u")
		print("2.Pretraga po naslovu")
		print("3.Pretraga po autoru")
		print("4.Pretraga po zanru")
		print("\n5.Povratak na glavni meni")
		opcija = input("\nOdaberite redni broj opcije pretrage:\n")
		num_test = opcija.isdigit()
		if int(opcija) > 5 or int(opcija) < 1:
			error("Odabrali ste nepostojucu opciju", 1.5)
		elif num_test is False:
			error("Unos mora biti broj", 1.5)
		elif int(opcija) == 1:
			search_engine_change("ISBN")
			x = False
		elif int(opcija) == 2:
			search_engine_change("Naslov")
			x = False
		elif int(opcija) == 3:
			search_engine_change("Autor")
			x = False
		elif int(opcija) == 4:
			search_genre_change()
			x = False
		elif int(opcija) == 5:
			book_data_menu()
			x = False


def search_engine_change(key):
	""" Endzin za pretragu knjiga koji dozvoljava
	i izmenu i brisanje knjige na licu mesta """
	global bk
	selected_books = []
	os.system("cls")
	parameter = input("Pretraga: ")
	for book in book_list:
		##b = 'Zanr' in book.keys()
		##print(b)
		if "1" in book["Stanje"]:
			if parameter.lower() in book[key].lower():
				selected_books.append(book)
	if selected_books == []:
		print("\n\nKnjiga nije pronadjena!")
		ak = input("\nPritisnite enter za povratak na meni pretrage")
		os.system("cls")
		search_menu_2()
	print("{:^111}\n".format("Rezultati pretrage:"))
	print("---" + "{:-^20}{:-^25}{:-^8}{:-^12}{:-^8}{:-^20}{:-^15}".format("Autor", "Naslov", "Godina",
	 "Cena", "Kolicina", "Zanr", "ISBN") )
	num = 1
	for book in selected_books:
		print(str(num) + ".)" + "{:^20}{:^25}{:^8}{:^12}{:^8}{:^20}{:^15}".format(book["Autor"], 
			book["Naslov"], book["Godina"], book["Cena"], book["Kolicina"], book["Zanr"], book["ISBN"]))
		num += 1
	print("="*111)

	ak = input("\nOdaberite redni broj knjige: ")
	bk = selected_books[int(ak) - 1]
	print("\n\n1. Obrisi knjigu\n2. Izmeni knjigu")
	ak = input("\nOdaberite opciju: ")
	if ak == "1":
		bk["Stanje"] = "0"
		book_update()
		ak = input("\nPritisnite enter za povratak na glavni meni")
	elif ak == "2":
		os.system("cls")
		book_change()
		book_update()

def search_engine(key):
	"""Obican endzin za pretragu po kljucu."""
	selected_books = []
	os.system("cls")
	parameter = input("Pretraga: ")
	for book in book_list:
		##b = 'Zanr' in book.keys()
		##print(b)
		if "1" in book["Stanje"]:
			if parameter.lower() in book[key].lower():
				selected_books.append(book)
	if selected_books == []:
		print("\n\nKnjiga nije pronadjena!")
		ak = input("\nPritisnite enter za povratak na meni pretrage")
		os.system("cls")
		search_menu_1()
	print("{:^111}\n".format("Rezultati pretrage:"))
	print("---" + "{:-^20}{:-^25}{:-^8}{:-^12}{:-^8}{:-^20}{:-^15}".format("Autor", "Naslov", "Godina",
	 "Cena", "Kolicina", "Zanr", "ISBN") )
	num = 1
	for book in selected_books:
		print(str(num) + ".)" + "{:^20}{:^25}{:^8}{:^12}{:^8}{:^20}{:^15}".format(book["Autor"], 
			book["Naslov"], book["Godina"], book["Cena"], book["Kolicina"], book["Zanr"], book["ISBN"]))
		num += 1
	print("="*111)

	ak = input("\nPritisnite enter za povratak na glavni meni")

def search_genre():
	"""Endzin za pretragu po zanru."""
	selected_books = []
	os.system("cls")
	zanrovi = ["Komedija", "SciFi", "Romantika", "Krimi", "Nauka", "Filozofija"]
	numb = 1
	x = True
	while x is True:
		for j in zanrovi:
			print(str(numb) + ".)" + j)
			numb += 1
		numb -= len(zanrovi)
		genre = input("\nOdaberite redni broj zanra:\n")	
		if genre.isdigit():
			if int(genre) <= len(zanrovi) and int(genre) > 0:
				parameter = zanrovi[int(genre) - 1]
				for book in book_list:
					if "1" in book["Stanje"]:
						if parameter in book["Zanr"]:
							selected_books.append(book)
				if selected_books == []:
					print("\n\nKnjiga nije pronadjena!")
					ak = input("\nPritisnite enter za povratak na meni pretrage")
					os.system("cls")
					search_menu_1()
				print("{:^111}\n".format("Rezultati pretrage:"))
				print("---" + "{:-^20}{:-^25}{:-^8}{:-^12}{:-^8}{:-^20}{:-^15}".format("Autor", "Naslov", "Godina",
				 "Cena", "Kolicina", "Zanr", "ISBN") )
				num = 1
				for book in selected_books:
					print(str(num) + ".)" + "{:^20}{:^25}{:^8}{:^12}{:^8}{:^20}{:^15}".format(book["Autor"], 
						book["Naslov"], book["Godina"], book["Cena"], book["Kolicina"], book["Zanr"], book["ISBN"]))
					num += 1
				print("="*111)

				ak = input("\nPritisnite enter za povratak na glavni meni")

				x = False
			else:
				error("Odabrali ste nepostojuci zanr", 2)
		else:
			error("Unos mora biti broj!", 2)

def search_genre_change():
	"""Endzin za pretragu po zanru sa opcijom
	menjanja ili brisanja knjige na licu mesta."""
	global bk
	selected_books = []
	os.system("cls")
	zanrovi = ["Komedija", "SciFi", "Romantika", "Krimi", "Nauka", "Filozofija"]
	numb = 1
	x = True
	while x is True:
		for j in zanrovi:
			print(str(numb) + ".)" + j)
			numb += 1
		numb -= len(zanrovi)
		genre = input("\nOdaberite redni broj zanra:\n")	
		if genre.isdigit():
			if int(genre) <= len(zanrovi) and int(genre) > 0:
				parameter = zanrovi[int(genre) - 1]
				for book in book_list:
					if "1" in book["Stanje"]:
						if parameter in book["Zanr"]:
							selected_books.append(book)
				if selected_books == []:
					print("\n\nKnjiga nije pronadjena!")
					ak = input("\nPritisnite enter za povratak na meni pretrage")
					os.system("cls")
					search_menu_2()
				print("{:^111}\n".format("Rezultati pretrage:"))
				print("---" + "{:-^20}{:-^25}{:-^8}{:-^12}{:-^8}{:-^20}{:-^15}".format("Autor", "Naslov", "Godina",
				 "Cena", "Kolicina", "Zanr", "ISBN") )
				num = 1
				for book in selected_books:
					print(str(num) + ".)" + "{:^20}{:^25}{:^8}{:^12}{:^8}{:^20}{:^15}".format(book["Autor"], 
						book["Naslov"], book["Godina"], book["Cena"], book["Kolicina"], book["Zanr"], book["ISBN"]))
					num += 1
				print("="*111)

				ak = input("\nOdaberite redni broj knjige: ")
				bk = selected_books[int(ak) - 1]
				print("\n\n1. Obrisi knjigu\n2. Izmeni knjigu")
				ak = input("\nOdaberite opciju: ")
				if ak == "1":
					bk["Stanje"] = "0"
					book_update()
					ak = input("\nPritisnite enter za povratak na glavni meni")
				elif ak == "2":
					os.system("cls")
					book_change()
					book_update()
					x = False
			else:
				error("Odabrali ste nepostojuci zanr", 2)
		else:
			error("Unos mora biti broj!", 2)

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

def book_change():
	"""Funkcija za izmenu podataka knjige. Podrzava
	preskakanje izmene podataka ukoliko se pritisne enter."""
	print("Izmena podataka o knjizi.\n\nUkoliko zelite da zadrzite stari parametar pritisnite enter.\n")
	print("="*42)
	x = True
	while x is True:
		print("Sadasnji autor: " + bk["Autor"])
		parameter = input("\nNovi autor: ")
		parameter = parameter.strip(" ")
		if parameter == "":
			bk["Autor"] = bk["Autor"]
			x = False
		else:
			if "|" in parameter:
				print("Unos ne sme sadrzati znak | ")
			else:
				bk["Autor"] = parameter
				x = False
	x = True
	while x is True:
		print("-"*42)
		print("Sadasnji naslov: " + bk["Naslov"])
		parameter = input("\nNovi naslov: ")
		parameter = parameter.strip(" ")
		if parameter == "":
			bk["Naslov"] = bk["Naslov"]
			x = False
		else:
			if "|" in parameter:
				error("Unos ne sme sadrzati znak | !", 2)
			else:
				bk["Naslov"] = parameter
				x = False
	x = True
	while x is True:
		print("-"*42)
		print("Sadasnja godina: " + bk["Godina"])
		parameter = input("\nNova godina: ")
		parameter = parameter.strip(" ")
		parameter = parameter.strip(".")
		if parameter == "":
			bk["Godina"] = bk["Godina"]
			x = False
		else:
			if "|" in parameter:
				error("Unos ne sme sadrzati znak | !", 2)
			else:
				if parameter.isdigit():
					bk["Godina"] = parameter
					x = False
				else:
					error("Unos mora biti broj!", 2)
	x = True
	while x is True:
		print("-"*42)
		print("Sadasnji kolicina: " + bk["Kolicina"])
		parameter = input("\nNova kolicina: ")
		parameter = parameter.strip(" ")
		if parameter == "":
			bk["Kolicina"] = bk["Kolicina"]
			x = False
		else:
			if "|" in parameter:
				error("Unos ne sme sadrzati znak | !", 2)
			else:
				if parameter.isdigit():
					bk["Kolicina"] = parameter
					x = False
				else:
					error("Unos mora biti broj!", 2)
	x = True
	while x is True:
		print("-"*42)
		print("Sadasnja cena: " + bk["Cena"])
		parameter = input("\nNova cena: ")
		parameter = parameter.strip(" ")
		if parameter == "":
			bk["Cena"] = bk["Cena"]
			x = False
		else:
			if "|" in parameter:
				error("Unos ne sme sadrzati znak | !", 2)
			else:
				if "," in parameter:
					parameter = parameter.split(",")
					if parameter[0].isdigit() and parameter[1].isdigit():
						price = float(parameter[0] + "." + parameter[1])
						bk["Cena"] = round(price, 2)
						x = False
					else:
						error("Unos mora biti broj!", 2)
				elif "." in parameter:
					parameter = parameter.split(".")
					if parameter[0].isdigit() and parameter[1].isdigit():
						price = float(parameter[0] + "." + parameter[1])
						bk["Cena"] = round(price, 2)
						x = False
					else:
						error("Unos mora biti broj!", 2)
				else:
					if parameter.isdigit():
						price = float(parameter)
						bk["Cena"] = round(price, 2)
						x = False
					else:
						error("Unos mora biti broj!", 2)
	print("-"*42)
	zanrovi = ["Komedija", "SciFi", "Romantika", "Krimi", "Nauka", "Filozofija"]
	numb = 1
	x = True
	while x is True:
		print("Sadasnji zanr: " + bk["Zanr"] + "\n")
		for j in zanrovi:
			print(str(numb) + ".)" + j)
			numb += 1
		numb -= len(zanrovi)
		zanr = input("\nOdaberite redni broj novog zanra:\n")	
		if zanr == "":
			bk["Zanr"] = bk["Zanr"] 
			x = False
		elif zanr.isdigit():
			if int(zanr) <= len(zanrovi) and int(zanr) > 0:
				bk["Zanr"] = zanrovi[int(zanr) - 1]
				x = False
			else:
				error("Odabrali ste nepostojuci zanr", 2)
		else:
			error("Unos mora biti broj!", 2)
	"""
	while x is False:
		print("-"*42)
		print("Sadasnji ISBN: " + bk["ISBN"])
		isbn = input("\nNovi ISBN: ")
		isbn = isbn.strip(" ")
		if isbn == "":
			bk["ISBN"] = bk["ISBN"]
			x = True
		elif len(isbn) == 13 and isbn.isdigit():
			bk["ISBN"] = isbn
			x = True
		else:
			error("Neodgovarajuc format ISBN-a", 2)
	"""

def book_extract():
	"""Funkcija za otpakivanje knjiga. Detektuje 
	gresku u bazi podataka ukoliko postoji."""
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
