x = 10;
nIter = 0;
[x, nIter] = newton(x, nIter);
disp([' La solution est : ', num2str(x)]);
disp([' Nb d''itérations : ', num2str(nIter)]);