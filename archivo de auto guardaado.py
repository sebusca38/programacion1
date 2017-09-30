import colorama
import decode
import os
def guardar(ubicacion,nombre,formato,*arg):
	try:
		archivo=open(ubicacion+nombre+formato, "a")
		datos1={id for id in range(len(arg)) : datos for datos in arg )
		
		archivo.close()
		print("guardado exitoso")
	except:
		archivo.close()
		print("algo fallo")
		
		
def abrir(a,*arg):