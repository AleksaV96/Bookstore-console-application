from modules.book_module import error

user_data = ["Korisnicko ime", "Ime", "Prezime", "Lozinka", "Uloga"]
def user_add():
	"""Dodavanje novog korisnika i 
	upisivanje u fajl."""
	global user
	print("     Unesite podatke o novom korisniku: ")
	print("="*47)
	user = {}
	user_role = ["Prodavac", "Menadzer"]
	x = True
	while x is True:
		for i in range(len(user_data) - 1):
			parameter = input(user_data[i] + ": ")
			print("-"*47)
			paremeter = parameter.strip(" ")
			if paremeter == "":
				error("Unos ne sme biti prazan!", 2)
			elif "|" in parameter:
				error("Unos ne sme sadrzati znak | !", 2)
			else:
				user[user_data[i]] = parameter
				x = False
	numb = 1
	x = True
	while x is True:
		for i in user_role:
			print(str(numb) + ".)" + i)
			numb += 1
		numb -= len(user_role)
		role = input("\nOdaberite redni broj uloge: ")
		if role.isdigit():
			role = int(role)
			if int(role) > 0 and int(role) <3:
				user["Uloga"] = user_role[role - 1]
				print(user)
				user_file()
				x = False
			else:
				error("Odabrali ste nepostojucu ulogu!", 2)
		else:
			error("Unos mora biti broj!", 2)

def user_file():
	"""Upisivanje korisnika u bazu
	u upakovanom obliku."""
	user_form = ""
	for k in range(len(user_data) - 1):
	    user_form += "{}|".format(user[user_data[k]])
	user_form += "{}\n".format(user[user_data[-1]])
	print("="*80)
	print("Ispis u bazu:" + "\n" + "-"*13)
	print(user_form)

	f = open("data/users.txt", "a")
	f.write(user_form)
	f.close()


