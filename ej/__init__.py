from random import randrange

NUM_CANALES = 99

def minmax(a, b):
    if a < b:
        return [b, a]
    return [a, b]

def calcularPasos(canalA, canalB):
    dif = canalA - canalB
    return NUM_CANALES - canalA + canalB if dif > NUM_CANALES / 2 else dif

# Main
for i in range(3):
    canales = [randrange(1, NUM_CANALES), randrange(1, NUM_CANALES)]
    print(canales)
    
    [canalA, canalB] = minmax(canales[0], canales[1])
    print(calcularPasos(canalA, canalB))