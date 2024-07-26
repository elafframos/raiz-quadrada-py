#from math import sqrt   #Desse modo só importaria a raiz quadrada, mas sem as outras funcionalidades da biblioteca.

import math #Biblioteca de matemática

num = int(input('Digite um número: '))
raiz = math.sqrt(num) #Para saber qual é a raiz quadrada do número digitado.

print('A raiz quadrada do número {} é {}'.format(num, raiz))
