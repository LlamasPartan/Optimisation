import numpy as np
import time

#Fonction
def conjgrad(A, b, x):
    """
    Variables:
    A : matrice definie positive
    b : membre droit de l'equation
    x : vecteur inconnu donnant la solution
    r : residu
    p : vecteur conjugué
    alpha : coefficient de descente du vecteur p
    """
    #Initialisation
    k = 0
    r_old = np.dot(A, x)-b
    p_old = -r_old

    #Traitement boucle
    while ((r_old != np.zeros(len(b))).all()):

        Apk = np.dot(A, p_old)
        alpha = -np.dot(np.transpose(r_old),p_old)/np.dot(np.transpose(p_old), Apk) #maj de alpha

        x = x + np.dot(alpha, p_old)#maj x
        r_new = np.dot(A, x) - b # maj r

        beta = np.dot(np.transpose(r_new),Apk) / np.dot(np.transpose(p_old), Apk)


        p_new = -r_new + np.dot(beta, p_old)#maj p

        #k = k+ 1
        r_old = r_new
        p_old = p_new
        k = k+1
    print("Nb d'itérations:", k)
    return x

#Données
A = np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])
b = np.array([5,-3,1])
x = np.array([0,0,0])


#Résultat

start_time = time.perf_counter_ns() #début du chrono


print("La solution du systeme Ax =b est:",conjgrad(A,b,x))

interval = time.perf_counter_ns() - start_time #calcul du temps

print("Temps d'execution de la fonction:", interval)
























