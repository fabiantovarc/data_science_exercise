"""
def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura


@mayusculas
def mensaje(nombre):
    print('se imprime el mensaje')
    return f'{nombre}, recibiste un mensaje'

print(mensaje('Pablo'))

"""
"""
def decorador(func):
    def envoltura1():
        print('Esto se añade a mi funcion original')
        func()
    return envoltura1

def saludo(n):
    print('Hola')

saludo()

saludo = decorador(saludo)
saludo()
"""

from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {time_elapsed.total_seconds()} segundos')
    return wrapper


@execution_time
def random_func():
    for _ in range(1, 10000000):
        pass


random_func()