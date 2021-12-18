import time

class FiboIter():

    """Iterador que representa a la suceción de fibonacci"""
    
    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if not self.max or self.counter <= self.max:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                # self.n1 = self.n2 esta línea y la de abajo se pueden reemplazar usando swapping
                # self.n2 = self.aux
                self.n1 , self.n2 = self.n2, self.aux #uso de swapping
                self.counter += 1
                return self.aux
        else:
            raise StopIteration

if '__main__' == __name__:
    fibonacci = FiboIter(7)

    for element in fibonacci:
        print(element)
        time.sleep(0.5)