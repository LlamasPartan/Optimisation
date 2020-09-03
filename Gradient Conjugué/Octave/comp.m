function [ok] = comp (x, y)
  #Postcondition:renvoi 1 si x == y, 0 sinon
  z = (x!=y); #z[i] =  1 si x[i] != y[i] et 0 si x[i]==y[i]
  ok = (sum(z)==0); #on fait la somme des éléments = nombre de cases différentes en x et y
endfunction
