import time #pour le chrono

# Definition fonction
def f(x):
    return x**2 -10

## Sans recursivité



def regula_falsi(f, a, b, epsilon):
    nIter = 0 #nombre ditérations

    if f(a) * f(b) > 0:
        return None #TVI pas applicable ici
    u, v = float(a), float(b)
    while (abs(f(u)) > epsilon):
        i = i+1 #incrémentation compteur boucle
        w = u -f(u)*(v-u)/(f(v)-f(u))
        if f(u) * f(w) <= 0: #w remplace v
            v = w
        else: #w remplace u
            u = w
    print("Nb d'Itérations':", nIter)
    return w



# Lecture de l'intervalle
a = 0
b = 10


epsilon=1e-12


# Résultats
start_time = time.perf_counter_ns() #début du chrono
print("La valeur du zéro de cette fonction sur (a,b) est:",regula_falsi(f,a,b,epsilon))

interval = time.perf_counter_ns() - start_time #calcul du temps

print("Temps d'execution de la fonction:", interval*10**(-6))

## Avec recursivité


def regu_rec(f,a, b,prec):
    a, b = float(a), float(b) #convertion bornes en réels
    if (abs(f(a))<=prec): #alors a est racine
        return a -f(a)*(b-a)/(f(b)-f(a))
    else:
        c = a -f(a)*(b-a)/(f(b)-f(a)) #calcul nouvelle borne

    if f(a)*f(c) <= 0: #Si le TVI est applicable entre a et c, c remplace b
        return regu_rec(f,a,c,prec)
    else: #sinon c remplace b
        return regu_rec(f,c,b,prec)



# Résultats
start_time = time.perf_counter_ns() #début du chrono
print("La valeur du zéro de cette fonction sur (a,b) est:", regu_rec(f,a,b,epsilon))

interval = time.perf_counter_ns() - start_time #calcul du temps

print("Temps d'execution de la fonction:", interval*10**(-6))