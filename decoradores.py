def mayusculas(func):
	def envoltura(texto):
		return func(texto).upper()
	return envoltura

@mayusculas
def mensaje(nombre):
	return f'{nombre}, recibiste un mensaje'

def run():
    print(mensaje('Gabriel'))

if '__main__' == __name__:
    run()