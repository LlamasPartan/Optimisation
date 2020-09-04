function [y] = df(x)
  y = deriv(@(x0) x0**2-10, x);
endfunction