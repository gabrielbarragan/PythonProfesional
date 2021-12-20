import random

def remove_duplicate_of_list(lista: list)-> list:
    return list(set(lista))

def run():
    my_list = [random.randint(0,100) for i in range(0,10) ]
    print(f'con duplicados: {my_list}')
    my_list_new = remove_duplicate_of_list(my_list)
    print(f'sin duplicados: {my_list_new}')

if '__main__' == __name__:
    run()