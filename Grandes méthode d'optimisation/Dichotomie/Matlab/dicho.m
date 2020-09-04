function [m] = dicho(a,b,eps)
 
 f=inline('x.*x -10;'); #definition de la fonction
  
  tic#début du chrono
  while (b-a >= eps)
      m=(a+b)/2;
      if f(a)*f(m)<0
        b=m;
      else
          a=m;
      endif
  endwhile

  toc#arret du chrono

endfunction

