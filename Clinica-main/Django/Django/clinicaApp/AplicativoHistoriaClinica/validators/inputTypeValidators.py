def stringValidator(string,element):
    if string=="" or string==None:
        raise Exception(element + " no tiene un valor valido")

def integerValidator(string,element):
    stringValidator(string,element)
    try:
        return int(string)
    except:
        raise Exception(element + " no es un numero valido")