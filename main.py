#   ---------   BIBLIOTECAS   ---------   #

# De Python:
import time # asctime
from openpyxl import Workbook, load_workbook

# Propias:
import init
import stdio # Standard Input-Output
import menu




#   ---------   MAIN   ---------   #


comando_borrar = init.obtener_comando_borrar()
wb, ws = init.abrir_excel()
f_turnos = open("Registro.txt", "a")


nombre_encargadx = menu.realizar_cambio_de_turno(f_turnos, comando_borrar)
monto_turno = 0

menu.imprimir(comando_borrar)
opcion = stdio.input_opcion()

while opcion != "3":
	if opcion == "1":
		monto_turno += menu.ingresar_nuevo_pedido(ws, monto_turno, comando_borrar)
	elif opcion == "2":
		f_turnos.write("OUT " + time.asctime() + " Encargad@ " + nombre_encargadx + " $" + str(monto_turno) + '\n' + "###############################################\n")
		monto_turno = 0
		nombre_encargadx = menu.realizar_cambio_de_turno(f_turnos, comando_borrar)

	menu.imprimir(comando_borrar)
	opcion = stdio.input_opcion()


f_turnos.write("OUT " + time.asctime() + " Encargad@ " + nombre_encargadx + " $" + str(monto_turno) + '\n' + "###############################################\n")
f_turnos.close()
menu.guardar_compras_confirmadas(wb)