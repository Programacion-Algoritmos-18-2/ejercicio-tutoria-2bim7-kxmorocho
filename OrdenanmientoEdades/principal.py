from modelado.mimodelo import Persona
from data.miarchivo import MiArchivo
from ordenamiento.ordenamiento import *

arch = MiArchivo()

lista = arch.obtener_info()
lista = [l.split(";") for l in lista]

listEdades = [] # Lista que va a guardar las edades
lista1 = []


for i in lista:
	p = Persona(i[0],i[1],i[2]) # Creamos el objeto de tipo Persona y le enviamos los parametros
	listEdades.append(p.obtener_edad()) # Agregamos en la lista las edades

	listEdades.append(p)
	lista1.append(p.edad)

merge_sort_result = merge_sort(listEdades)  # Guardamos en 'merge_sort_result' lo que retorna el metodo 'merge_sort' y le enviamos la lista de edades

print(merge_sort_result)
m.cerrar_archivo() # Cerramos el archivo
