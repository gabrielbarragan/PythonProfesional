from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        """Calcula el tiempo que demora la función en ejecutarse"""
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapse = final_time - initial_time
        print(f'Pasaron más de {time_elapse.total_seconds()} segundos')
    return wrapper 

@execution_time
def random_func():
    for _ in range(1, 1000000):
        pass

@execution_time
def suma(a: int, b:int) -> int:
    return a + b

@execution_time
def saludo(nombre = 'Gabriel'):
    return f'Hola {nombre}'

if '__main__' == __name__:
    
    random_func()
    suma(10,21)
    saludo('Andrés')

