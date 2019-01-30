class Persona(object):
	"""docstring for persona"""
	def __init__(self, nom, ape, edad):

		self.agregar_nombre = nom
		self.agregar_apellido = ape
		self.agregar_edad = int(edad)
	
	#Métodos agregar
	def agregar_nombre(self, nom):
		self.nombre = nom

	def agregar_apellido(self, ape):
		self.apellido = ape

	def agregar_edad(self, edad):
		self.edad = int(edad)

	#Métodos obtener
	def obtener_nombre(self):
		return self.nombre

	def obtener_apellido(self):
		return self.apellido

	def obtener_edad(self):
		return self.edad

def __str__(self):

	return "\nNombre: %s, Apellido: %s, Edad: %d"%(self.obtener_nombre(),self.obtener_apellido(),self.obtener_edad())
