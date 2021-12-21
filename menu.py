import subprocess # run
import time # sleep
from openpyxl import Workbook

import stdio


def imprimir(comando_borrar):
	subprocess.run([comando_borrar, ""], shell = True)

	print("McDowell's\nRecuerda que siempre hay que recibir al cliente con una sonrisa :)\n")
	print("1 - Ingreso de nuevo pedido")
	print("2 - Cambio de turno")
	print("3 - Apagar sistema\n\n")


def ingresar_nuevo_pedido(ws, monto_turno, comando_borrar):
	subprocess.run([comando_borrar, ""], shell = True)

	nombre_cliente = stdio.input_str("Ingrese el nombre del cliente: ")
	cant_s = stdio.input_int("Ingrese cantidad Combo S: ")
	cant_d = stdio.input_int("Ingrese cantidad Combo D: ")
	cant_t = stdio.input_int("Ingrese cantidad Combo T: ")
	cant_f = stdio.input_int("Ingrese cantidad Flurby: ")

	total = cant_s*650 + cant_d*700 + cant_t*800 + cant_f*250
	ws.append([nombre_cliente, time.asctime(), str(cant_s), str(cant_d), str(cant_t), str(cant_f), str(total)])

	print("\nTotal $" + str(total))
	abono = stdio.input_int("Abona con $ ")
	print("vuelto $ " + str(abono - total) + "\n\nVolviendo al menu principal...")

	time.sleep(3)

	return total


def realizar_cambio_de_turno(f_turnos, comando_borrar):
	subprocess.run([comando_borrar, ""], shell = True)

	print("Bienvenido a McDowell's\n")
	nombre_encargadx = stdio.input_str("Ingrese su nombre encargad@: ")
	f_turnos.write("IN " + time.asctime() + " Encargad@ " + nombre_encargadx + '\n')
	return nombre_encargadx


def print_close_file_error():
	print("\n\nERROR: Asegurese de cerrar el archivo \"Compras confirmadas.xlsx\" antes de cerrar el programa, sino los datos no se podran actualizar.\n")
	print("1) Cerrar el archivo y volver a intentar.")
	print("2) Salir sin guardar.\n")


def guardar_compras_confirmadas(wb):
	try:
		wb.save("Compras confirmadas.xlsx")
	except PermissionError:
		opcion = "0"
		while opcion != "2":
			try:
				wb.save("Compras confirmadas.xlsx")
				break;
			except PermissionError:
				print_close_file_error()
				opcion = stdio.input_str()