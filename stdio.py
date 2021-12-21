from colorama import Fore, init


def output(string):
	print(string, end = "")


def def_input(string = ""):
	init(convert = True) # <--- Necesario para el colorama
	output(string)
	output("\033[91m")
	string = input()
	output(Fore.WHITE)
	return string


def input_opcion():
	opcion = def_input() # <--- Lo puedo pasar sin parametros porque en la funcion original en caso de no pasar parametros se iguala a algo; si no fuera asi, esto romperia.
	while opcion != "1" and opcion != "2" and opcion != "3":
		opcion = def_input("Opcion no valida, ingrese otra porfavor: ")

	return opcion


def input_str(mensaje):
	mensaje = def_input(mensaje) 
	while mensaje == "":
		mensaje = def_input("Opcion no valida, ingrese otra porfavor: ")

	return mensaje


def input_int(mensaje):
	mensaje = def_input(mensaje)
	while mensaje.isdecimal() != True:
		mensaje = def_input("Lo ingresado no es un numero, ingrese un numero entero porfavor: ")

	return int(mensaje)