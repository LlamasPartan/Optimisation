function [y]= regu_rec(a,b,eps)
  
  c =  0;
  if (abs(f(a))<eps)
    y = a - ((f(a).*(b-a))./(f(b) - f(a)))
  else
    c =  a - ((f(a).*(b-a))./(f(b) - f(a)));
    if (f(a).*f(c)<=0)
      y = regu_rec(a,c, eps);
    else 
      y = regu_rec(c,b,eps);
    endif
  endif
  
  
  
endfunction