#Fonction
function [x] = grad(A, b, x)
   
    #Variables:
    #A : matrice definie positive
    #b : membre droit de l'equation
    #x : vecteur inconnu donnant la solution
    #r : residu
    #p : vecteur conjugué
    #alpha : coefficient de descente du vecteur p
    
    
    #Initialisation
    r_old = A*x-b;
    p_old = -r_old;

    #Traitement boucle
    while ((comp(r_old, zeros(length(b),1))==0))
        Apk = A*p_old;
        alpha = -(r_old')*p_old/((p_old')* Apk); #maj de alpha

        x = x + alpha* p_old; #maj x
        r_new = A*x - b; # maj r

        beta = ((r_new')*Apk) / ((p_old')* Apk);

        p_new = -r_new + beta* p_old; #maj p
        
        #k = k+ 1
        r_old = r_new;
        p_old = p_new;
        
    endwhile
endfunction