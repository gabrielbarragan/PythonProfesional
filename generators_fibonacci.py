import time



def fibo_gen(max=None):
    n1 = 0
    n2 = 1
    counter = 0
    
    while not max or counter <= max:
        if counter == 0:
            counter+=1
            yield n1
        elif counter == 1:
            if max == 0:
                break
            counter += 1
            yield n2
        else :
            aux = n1 + n2 
            n1, n2 = n2, aux
            counter += 1
            yield aux

if '__main__'==__name__:
    list_fibonacci = fibo_gen()

    for element in list_fibonacci:
        print(element)
        time.sleep(1)