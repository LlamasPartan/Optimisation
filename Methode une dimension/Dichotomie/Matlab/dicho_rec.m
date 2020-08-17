function [y]= dicho_rec(a,b, eps)
  
  c=0;
  if (b-a<eps)
    y=(a+b)./2;
  else
    c = (a+b)./2;
  endif
  
  if (f(a).*f(c)<0)
    y = dicho_rec(a,c, eps);
  else 
    y = dicho_rec(c,b, eps);
  endif
  
endfunction