%Initialisation
tab=[
142,241,0,0,0,0;
0.23,0.7,1,0,0,20.21;
0.015,0.015,0,1,0,0.705;
1.8,1.1,0,0,1,75]

function [tab,x]=simplexeStandard(tab)
    %On crée un vecteur dont l'i-ème élément est l'indice de la variable dont la
    %valeur est à la fin de la i+1-ème ligne du tableau
    x=size(tab)(2)-size(tab)(1)+1:size(tab)(1)+1
    %Tant que les coefficients de Lf dont positifs
    while sum(tab(1,1:end-1)>0)>0
        %Recherche de la variable entrante
        indiceVarEntrante=1
        for i=2:size(tab)(2)-1
            if tab(1,i)>tab(1,indiceVarEntrante)
                indiceVarEntrante=i
            endif
        endfor
        %Recherche de la variable sortante
        indiceVarSortante=1
        rapportMin=Inf
        for i=2:size(tab)(1)
            if tab(i,indiceVarEntrante)>0
                rapport=tab(i,size(tab)(2))/tab(i,indiceVarEntrante)
                if rapport<rapportMin && rapport>=0
                    indiceVarSortante=i
                    rapportMin=rapport
                endif
            endif
        endfor
        if indiceVarSortante==1
            disp("Pas de variable sortante")
            return
        endif
        %Coefficient principal à 1
        tab(indiceVarSortante,:)=1/tab(indiceVarSortante,indiceVarEntrante)*tab(indiceVarSortante,:)
        %Coefficients secondaires à 0
        for i=1:size(tab)(1)
            if i!=indiceVarSortante
                tab(i,:)-=tab(i,indiceVarEntrante)*tab(indiceVarSortante,:)
            endif
        endfor
        %Stockage de la position des différentes variables
        x(indiceVarSortante-1)=indiceVarEntrante
    end
endfunction

[tabRes,xRes]=simplexeStandard(tab)
disp(tabRes)
for i=1:size(xRes)(2)
    if xRes(i)<size(tabRes)(2)-size(tabRes)(1)+1
        fprintf("x %d = %d\n",xRes(i),tabRes(i+1,end))
    else
        fprintf("y %d = %d\n",xRes(i)-size(tabRes)(2)+size(tabRes)(1),tabRes(i+1,end))
    endif
endfor
fprintf("Optimum de %d\n",-tabRes(1,end))
