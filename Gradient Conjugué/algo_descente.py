    Variables
        ri //residu à l itération i
        xi // ième terme de la suite convergent
        pi // vecteurs conjugués
        αi // coefficient de descente du vecteur pi
        βk // coefficient de mise a jour pi
        A // matrice du systeme d equation

    Début
        r0 ← Ax0 − b //initialisation residu
        p0 ← −r0 //initialisation de la direction de descente
        k ← 0 //initialisation nombre itérations

        Tant que rk != 0

            αk ← −(trans(rk)*pk)/(trans(pk)*A*pk)

            xk+1 ← xk + αkpk //nouvel iteration de xk
            rk+1 ← A*xk+1 − b// mise a jour residu

            βk+1 ← −(trans(rk+1)*A*pk)/(trans(pk)*A*pk)

            pk+1 ← −rk+1 + βk+1*pk //mise a jour vecteur conjugué
            k ← k + 1 //incrementation de k

        Fin tant que
    Fin