import os
from modules.book_module import *

def autor_change():
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
				bk["Autor"] = parameter
				x = False

def naslov_change():
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

def godina_change():
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

def kolicina_change():
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

def cena_change():
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
	
def zanrovi_change():
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

def ISBN_change():
	while x is False:
		print("-"*42)
		isbn = input("ISBN: ")
		isbn = isbn.strip(" ")
		if len(isbn) == 13 and isbn.isdigit():
			book["ISBN"] = isbn
			book["Stanje"] = "1"
			book_list.append(book)
			book_file()
			x = True
		else:
			error("Neodgovarajuc format ISBN-a", 2)

