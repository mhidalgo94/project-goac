

def lectura(mes):
    doc = open('Ddifusa.csv', 'r')
    datos = doc.readlines()
    array = datos[mes].split(',')
    # del (array[-1])
    array.remove("\n")
    return array