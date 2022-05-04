# murakkab funksiayalar
from multiprocessing.sharedctypes import Value


def decorative_function(funs):
    def ichki(malumotlar):
        return[funs(value[0], value[1]) for value in malumotlar]
    return ichki    

    
@decorative_function
def raqam(a, b):
    print(a + b)
print(raqam([(10,20), (20,20), (30,30)]))        