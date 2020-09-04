x =[0; 0; 0];
b = [5; -3; 1];
A = [2 -1 0; -1 2 -1; 0 -1 2];
tic
disp("La solution dy systeme Ax=b est:"), disp(grad(A, b, x));
toc

tic
disp("La solution dy systeme Ax=b est:"), disp(cgs (A, b));
toc