
import time #pour le chrono

# Definition fonction
def f(x):
    return x**2 -10

## Dicho sans recursivité



def dicho(f, a, b, epsilon):
    i = 0
    if f(a) * f(b) > 0:
        return None
    u, v = float(a), float(b)
    while abs(v - u) > 2 * epsilon:
        i = i+1
        w = (u + v) / 2
        if f(u) * f(w) <= 0:
            v = w
        else:
            u = w
    return (u + v) / 2
    print("i",i)

# Lecture de l'intervalle
a = 0
b = 10

epsilon=1e-12



# Résultats
start_time = time.time() #début du chrono
print("La valeur du zéro de cette fonction sur (a,b) est:",dicho(f,a,b,epsilon))

interval = time.time() - start_time #calcul du temps

print("Temps d'execution de la fonction:", interval)


## Dicho avec recursivité



def dicho_rec(f,a, b,prec):
    a, b = float(a), float(b)
    if b-a<=prec:
        return (a+b)/2
    else:
        c = (a+b)/2
    if f(a)*f(c) <= 0:
        return dicho_rec(f,a,c,prec)
    else:
        return dicho_rec(f,c,b,prec)



# Lecture de l'intervalle
a = 0
b = 10
prec = 1e-12



# Résultats
start_time = time.time() #début du chrono
print("La valeur du zéro de cette fonction sur (a,b) est:", dicho_rec(f,a,b,prec))

interval = time.time() - start_time #calcul du temps

print("Temps d'execution de la fonction:", interval)


























