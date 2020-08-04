x=input(' Donner la valeur initiale : ');
eps=0.0001;
dif=2*eps;
nIter=0;

while abs(dif)>eps 
    x1=x-f(x)/df(x);
    dif=abs(x1-x);
    x= x1;
    nIter=nIter+1;
end
 
disp([' La solution est : ', num2str(x1)]);
disp([' Nb d''itérations : ', num2str(nIter)]);
clear