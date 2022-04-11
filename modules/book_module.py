import os
import time
import copy

book_data = ["Stanje", "Autor", "Naslov", "Godina", "Cena", "Kolicina", "Zanr", "ISBN"]
book_list = []

def book_add():
	"""Ova funkcija uzima od korisnika parametre za knjigu i ugradjuje 
	ih u recnik book. Radi u paru sa funkcijom book_file."""
	global book
	global book_list
	book_extract_1()
	book = {}
	book["Stanje"] = "1"
	print("     Unesite podatke o novoj knjizi")
	print("="*42)
	x = True
	while x is True:
		parameter = input("Autor: ")
		parameter = parameter.strip(" ")
		if parameter == "":
			print("Unos ne sme biti prazan!")
		else:
			if "|" in parameter:
				print("Unos ne sme sadrzati znak | ")
			else:
				book["Autor"] = parameter
				x = False
	x = True
	while x is True:
		print("-"*42)
		parameter = input("Naslov: ")
		parameter = parameter.strip(" ")
		if parameter == "":
			error("Unos ne sme biti prazan!", 2)
		else:
			if "|" in parameter:
				error("Unos ne sme sadrzati znak | !", 2)
			else:
				book["Naslov"] = parameter
				x = False
	x = True
	while x is True:
		print("-"*42)
		parameter = input("Godina: ")
		parameter = parameter.strip(" ")
		parameter = parameter.strip(".")
		if parameter == "":
			error("Unos ne sme biti prazan!", 2)
		else:
			if "|" in parameter:
				error("Unos ne sme sadrzati znak | !", 2)
			else:
				if parameter.isdigit():
					book["Godina"] = parameter
					x = False
				else:
					error("Unos mora biti broj!", 2)
	x = True
	while x is True:
		print("-"*42)
		parameter = input("Kolicina: ")
		parameter = parameter.strip(" ")
		if parameter == "":
			error("Unos ne sme biti prazan!", 2)
		else:
			if "|" in parameter:
				error("Unos ne sme sadrzati znak | !", 2)
			else:
				if parameter.isdigit():
					book["Kolicina"] = parameter
					x = False
				else:
					error("Unos mora biti broj!", 2)
	x = True
	while x is True:
		print("-"*42)
		parameter = input("Cena: ")
		parameter = parameter.strip(" ")
		if parameter == "":
			error("Unos ne sme biti prazan!", 2)
		else:
			if "|" in parameter:
				error("Unos ne sme sadrzati znak | !", 2)
			else:
				if "," in parameter:
					parameter = parameter.split(",")
					if parameter[0].isdigit() and parameter[1].isdigit():
						price = float(parameter[0] + "." + parameter[1])
						book["Cena"] = round(price, 2)
						x = False
					else:
						error("Unos mora biti broj!", 2)
				elif "." in parameter:
					parameter = parameter.split(".")
					if parameter[0].isdigit() and parameter[1].isdigit():
						price = float(parameter[0] + "." + parameter[1])
						book["Cena"] = round(price, 2)
						x = False
					else:
						error("Unos mora biti broj!", 2)
				else:
					if parameter.isdigit():
						price = float(parameter)
						book["Cena"] = round(price, 2)
						x = False
					else:
						error("Unos mora biti broj!", 2)
	print("-"*42)
	zanrovi = ["Komedija", "SciFi", "Romantika", "Krimi", "Nauka", "Filozofija"]
	numb = 1
	x = True
	while x is True:
		for j in zanrovi:
			print(str(numb) + ".)" + j)
			numb += 1
		numb -= len(zanrovi)
		zanr = input("\nOdaberite redni broj zanra:\n")	
		if zanr.isdigit():
			if int(zanr) <= len(zanrovi) and int(zanr) > 0:
				book["Zanr"] = zanrovi[int(zanr) - 1]
				x = False
			else:
				error("Odabrali ste nepostojuci zanr", 2)
		else:
			error("Unos mora biti broj!", 2)
	isbn_fun()

def isbn_fun():
	"""Funkcija za kontrolu i unos ISBN-a.
	Detektuje ponavljanje ISBN-a."""
	x = False
	while x is False:
		print("-"*42)
		isbn = input("ISBN: ")
		isbn = isbn.strip(" ")
		for m in book_list:
			if isbn == m["ISBN"]:
				error("Uneti ISBN vec postoji!", 2)
				isbn = "sifra1"
				isbn_fun()
		if len(isbn) == 13 and isbn.isdigit():
			book["ISBN"] = isbn
			book_list.append(book)
			book_file()
			x = True
		elif isbn == "sifra1":
			x = True
		else:
			error("Neodgovarajuc format ISBN-a", 2)

def book_file():
	"""Ova funkcija konvertuje recnik book u string.
	String je oblika: "autor|naslov|godina|cena|kolicina|zanr|isbn"
	Upakovani podatak se cuva u fajlu books.txt."""
	file_form = ""
	for k in range(len(book_data) - 1):
	    file_form += "{}|".format(book[book_data[k]])
	file_form += "{}\n".format(book[book_data[-1]])
	print("="*80)
	print("Ispis u bazu:" + "\n" + "-"*13)
	print(file_form)

	f = open("data/books.txt", "a")
	f.write(file_form)
	f.close()

def error(e_text, t):
	"""Funckija ispisuje gresku i blokira
	program na odredjeno vreme.
	Parametri su: tekst ispisa i vreme."""
	os.system("cls")
	print(e_text)
	time.sleep(t)
	os.system("cls")

def book_extract_1():
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









    



