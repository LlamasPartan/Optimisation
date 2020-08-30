import numpy as np
np.set_printoptions(linewidth=99999) #Pour afficher les longues matrices dans la console sans aller à la ligne...

#Initialisation
tab1=np.array([
[142,241,0,0,0,0],
[0.23,0.7,1,0,0,20.21],
[0.015,0.015,0,1,0,0.705],
[1.8,1.1,0,0,1,75]])

def variableEntrante(tab):
    indiceVarEntrante=0
    for i in range(1,tab.shape[1]-1):
        if tab[0,i]>tab[0,indiceVarEntrante]:
            indiceVarEntrante=i
    return(indiceVarEntrante)

def variableSortante(tab,indiceVarEntrante):
    indiceVarSortante=0
    rapportMin=np.inf
    for i in range(1,tab.shape[0]):
        if tab[i,indiceVarEntrante]>0:
            rapport=tab[i,tab.shape[1]-1]/tab[i,indiceVarEntrante]
            if rapport<rapportMin and rapport>=0:
                indiceVarSortante=i
                rapportMin=rapport
    return(indiceVarSortante)

def normalisation(tab,indiceVarEntrante,indiceVarSortante):
    tab[indiceVarSortante,:]=1/tab[indiceVarSortante,indiceVarEntrante]*tab[indiceVarSortante,:]
    for i in range(tab.shape[0]):
        if i!=indiceVarSortante:
            tab[i,:]-=tab[i,indiceVarEntrante]*tab[indiceVarSortante,:]

def simplexeStandard(tab):
    #On crée un vecteur dont l'i-ème élément est l'indice de la variable dont la
    #valeur est à la fin de la i+1-ème ligne du tableau
    x=np.arange(tab.shape[1]-tab.shape[0],tab.shape[0]+1)
    #Tant que les coefficients de Lf sont positifs
    while (tab[0,:-1]>np.zeros((1,tab.shape[1]-1))).any():
        #Recherche de la variable entrante
        indiceVarEntrante=variableEntrante(tab)
        #Recherche de la variable sortante
        indiceVarSortante=variableSortante(tab,indiceVarEntrante)
        if indiceVarSortante==0:
            print("Pas de variable sortante")
            exit()
        #Coefficient principal à 1 et coefficients secondaires à 0
        normalisation(tab,indiceVarEntrante,indiceVarSortante)
        #Stockage de la position des différentes variables
        x[indiceVarSortante-1]=indiceVarEntrante
    return(tab,x)

tab,x=simplexeStandard(tab1)
print(tab)
for i in range(x.size):
    if x[i]<tab.shape[1]-tab.shape[0]:
        print("x",x[i]+1,"=",np.around(tab[i+1,-1],3))
    else:
        print("y",x[i]+1-tab.shape[1]+tab.shape[0],"=",np.around(tab[i+1,-1],3))
print("Optimum de",-np.around(tab[0,-1],3))
