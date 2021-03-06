%Initialisation
tab1=[
142,241,0,0,0,0;
0.23,0.7,1,0,0,20.21;
0.015,0.015,0,1,0,0.705;
1.8,1.1,0,0,1,75]

tab2=[
1,2,0,0,0,0;
-1,3,1,0,0,10;
5,-4,0,1,0,1;
-3,1,0,0,1,-1]

function indiceVarEntrante=variableEntrante(tab)
    indiceVarEntrante=1
    for i=2:size(tab)(2)-1
        if tab(1,i)>tab(1,indiceVarEntrante)
            indiceVarEntrante=i
        endif
    endfor
endfunction

function indiceVarSortante=variableSortante(tab,indiceVarEntrante)
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
endfunction

function tab=normalisation(tab,indiceVarEntrante,indiceVarSortante)
    tab(indiceVarSortante,:)=1/tab(indiceVarSortante,indiceVarEntrante)*tab(indiceVarSortante,:)
    for i=1:size(tab)(1)
        if i!=indiceVarSortante
            tab(i,:)-=tab(i,indiceVarEntrante)*tab(indiceVarSortante,:)
        endif
    endfor
endfunction
    
function [tab,x]=simplexeStandard(tab)
    %On crée un vecteur dont l'i-ème élément est l'indice de la variable dont la
    %valeur est à la fin de la i+1-ème ligne du tableau
    x=size(tab)(2)-size(tab)(1)+1:size(tab)(1)+1
    %Tant que les coefficients de Lf dont positifs
    while sum(tab(1,1:end-1)>0)>0
        %Si une des variables est négative on applique la méthode des phases
        for i=2:size(tab)(1)
            if tab(i,end)<0
                [tab,x]=simplexePhases(tab,x)
            endif
        endfor
        %Recherche de la variable entrante
        indiceVarEntrante=variableEntrante(tab)
        %Recherche de la variable sortante
        indiceVarSortante=variableSortante(tab,indiceVarEntrante)
        if indiceVarSortante==1
            disp("Pas de variable sortante")
            return
        endif
        %Coefficient principal à 1 et coefficients secondaires à 0
        tab=normalisation(tab,indiceVarEntrante,indiceVarSortante)
        %Stockage de la position des différentes variables
        x(indiceVarSortante-1)=indiceVarEntrante
    end
endfunction

function [tabDelta,x]=simplexePhases(tab,x)
    %Construction du tableau du problème auxiliaire
    tabDelta=auxiliaire(tab)
    %Première phase
    [tabDelta,x]=phase1(tabDelta,x)
    %On regarde si on peut passer à la seconde phase
    if tabDelta(1,end)>0
        disp("Le problème n'a pas d'optimum")
        return
    endif
    %Seconde phase
    [tabDelta,x]=phase2(tabDelta,x,tab)
endfunction

function tabDelta=auxiliaire(tab)
    tabDelta=tab
    tabDelta(1,:)*=0
    tabGauche=tabDelta(:,1:end-1)
    tabMilieu=-ones(size(tabDelta)(1),1)
    tabDroite=tabDelta(:,end)
    tabDelta=[tabGauche,tabMilieu,tabDroite]
endfunction

function [tabDelta,x]=phase1(tabDelta,x)
    %Choix de la variable entrante (delta)
    indiceVarEntrante=size(tabDelta)(2)-1
    %Recherche de la variable sortante (la plus petite)
    indiceVarSortante=2
    for i=2:size(tabDelta)(1)
        if tabDelta(i,end)<tabDelta(indiceVarSortante,end)
            indiceVarSortante=i
        endif
    endfor
    %Coefficient principal à 1 et coefficients secondaires à 0
    tabDelta=normalisation(tabDelta,indiceVarEntrante,indiceVarSortante)
    %Stockage de la position des différentes variables
    x(indiceVarSortante-1)=indiceVarEntrante
    %Tant que les coefficients de Lf dont positifs
    while sum(tabDelta(1,1:end-1)>0)>0
        %Recherche de la variable entrante
        indiceVarEntrante=variableEntrante(tabDelta)
        %Recherche de la variable sortante en privilégiant delta
        indiceVarSortante=1
        rapportMin=Inf
        for i=2:size(tabDelta)(1)
            if tabDelta(i,indiceVarEntrante)>0
                rapport=tabDelta(i,size(tabDelta)(2))/tabDelta(i,indiceVarEntrante)
                if x(i-1)==size(tabDelta)(2)-1 && rapport==rapportMin
                    indiceVarSortante=i
                    rapportMin=rapport
                endif
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
        %Coefficient principal à 1 et coefficients secondaires à 0
        tabDelta=normalisation(tabDelta,indiceVarEntrante,indiceVarSortante)
        %Stockage de la position des différentes variables
        x(indiceVarSortante-1)=indiceVarEntrante
    end
endfunction

function [tabDelta,x]=phase2(tabDelta,x,tab)
    %Suppression de la colonne delta
    tabGauche=tabDelta(:,1:end-2)
    tabDroite=tabDelta(:,end)
    tabDelta=[tabGauche,tabDroite]
    %Réécriture du critère initial
    for i=1:size(x)(2)
        if x(i)<size(tabDelta)(2)-size(tabDelta)(1)+1
            tabDelta(1,size(tabDelta)(2)-size(tabDelta)(1)+1:end)-=tab(1,x(i))*tabDelta(i+1,size(tabDelta)(2)-size(tabDelta)(1)+1:end)
        endif
    endfor
endfunction

[tabRes,xRes]=simplexeStandard(tab2)
disp(tabRes)
for i=1:size(xRes)(2)
    if xRes(i)<size(tabRes)(2)-size(tabRes)(1)+1
        fprintf("x %d = %d\n",xRes(i),tabRes(i+1,end))
    else
        fprintf("y %d = %d\n",xRes(i)-size(tabRes)(2)+size(tabRes)(1),tabRes(i+1,end))
    endif
endfor
fprintf("Optimum de %d\n",-tabRes(1,end))
