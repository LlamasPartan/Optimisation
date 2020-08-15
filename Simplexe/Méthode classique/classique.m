%Initialisation
tab=[
142,241,0,0,0,0;
0.23,0.7,1,0,0,20.21;
0.015,0.015,0,1,0,0.705;
1.8,1.1,0,0,1,75]

function [tab,x]=simpleStandard(tab)
  x=zeros(1,size(tab)(2)-size(tab)(1))
  %Tant que les coefficients de Lf dont positifs
  while sum(tab(1,:)>0)>0
    %Recherche de la variable entrante
    indiceVariableEntrante=1
    for i=2:size(tab)(2)-1
      if tab(1,i)>tab(1,indiceVariableEntrante)
        indiceVariableEntrante=i
      endif
    endfor
    %Recherche de la variable sortante
    indiceVariableSortante=1
    rapportMin=-1
    while rapportMin<0
      indiceVariableSortante+=1
      if indiceVariableSortante<size(tab)(1)-1
        if tab(indiceVariableSortante,indiceVariableEntrante)!=0
          rapportMin=tab(indiceVariableSortante,size(tab)(2))/tab(indiceVariableSortante,indiceVariableEntrante)
         endif
      else
        disp("Pas de variable sortante")
        return
      endif
    end
    for i=indiceVariableSortante:size(tab)(1)
      if tab(i,indiceVariableEntrante)!=0
        rapport=tab(i,size(tab)(2))/tab(i,indiceVariableEntrante)
        if rapport<rapportMin && rapport>=0
          indiceVariableSortante=i
          rapportMin=rapport
        endif
      endif
    endfor
    %Coefficient principal à 1
    tab(indiceVariableSortante,:)=1/tab(indiceVariableSortante,indiceVariableEntrante)*tab(indiceVariableSortante,:)
    %Coefficients secondaires à 0
    for i=1:size(tab)(1)
      if i!=indiceVariableSortante
        tab(i,:)-=tab(i,indiceVariableEntrante)*tab(indiceVariableSortante,:)
      endif
    endfor
    %Stockage de la position des différentes variables
    x(indiceVariableEntrante)=indiceVariableSortante
  end
endfunction

[tabRes,xRes]=simpleStandard(tab)
disp(tabRes)
for i=1:size(xRes)(2)
  fprintf("x %d = %d\n",i,tabRes(xRes(i),end))
endfor
