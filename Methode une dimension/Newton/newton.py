import numpy as np
import time #pour le chrono


def fonction(x):
    y = x*x - 10
    return (y)

def derivee(x):
    y = 2*x
    return (y)

def NewtonsMethod( x, epsilon=0.000001):
    n = 0 #initialisation du nombre d'itérations
    dif = 2*epsilon #initialisation de la variable difference
    while (dif > epsilon) :
        x1 = x - fonction(x) / derivee(x)#calcul recursif du prochain point
        dif = abs(x1 - x)
        x = x1
        n = n+1 #nombre d'itérations: +1
    return (x, n)


# Programme principal

x  = float(input("Quelle est la valeur de départ ? : ")) #Valeur départ


(x,n) = NewtonsMethod(x)

#Affichage
start = time.perf_counter_ns()
print('Solution : x=%f, Nombre ditérations: n=%d' % (x, n) )
interval = time.perf_counter_ns()  - start

print(interval*10**(-6))
