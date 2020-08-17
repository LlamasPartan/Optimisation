function [y]=regula(a, b, eps, nIter)
  
  nIter = 0;

  if (f(a).*f(b)>0)
    disp('TVI non applicable');
  endif
  while (abs(f(a))>eps) #condition d'arret
    nIter = nIter+1; #incrémentation compteur boucle
    c = a - ((f(a)*(b-a))/(f(b) - f(a)));
    if (f(a).*f(c) <= 0) #c remplace b
        b = c;
    else #c remplace a
        a = c;
    endif
  endwhile
  y = c;
  disp("Nb d'Itérations':"),disp( nIter);

endfunction