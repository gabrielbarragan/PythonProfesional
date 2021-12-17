def is_prime(number: int) -> bool:
    counter = 0
    for i in range(2, number):

        if number % i == 0:
            counter +=1

    if counter == 0:
        return True
    else:
        return False


def run():
    if is_prime(4):
        print('El número es primo')
    else:
        print('El número no es primo')


if '__main__'== __name__:
    run()