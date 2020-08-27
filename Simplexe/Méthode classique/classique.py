import numpy as np

#Initialisation
tab=np.array([
[10.,-57,-9,-24,100,0,0,0,0,0],
[0,0,0,0,1,1,0,0,0,1],
[0.5,-5.5,-2.5,9,1,0,1,0,0,1],
[0.5,-1.5,-0.5,1,1,0,0,1,0,1],
[1,0,0,0,1,0,0,0,0,2]])

def simplexeStandard(tab):
    #On crée un vecteur dont l'i-ème élément est l'indice de la variable dont la
    #valeur est à la fin de la i+1-ème ligne du tableau
    x=np.arange(tab.shape[1]-tab.shape[0],tab.shape[0]+1)
    #Tant que les coefficients de Lf sont positifs
    while (tab[0,:-1]>np.zeros((1,tab.shape[1]-1))).any():
        #Recherche de la variable entrante
        indiceVarEntrante=0
        for i in range(1,tab.shape[1]-1):
            if tab[0,i]>tab[0,indiceVarEntrante]:
                indiceVarEntrante=i
        #Recherche de la variable sortante
        indiceVarSortante=0
        rapportMin=np.inf
        for i in range(1,tab.shape[0]):
            if tab[i,indiceVarEntrante]>0:
                rapport=tab[i,tab.shape[1]-1]/tab[i,indiceVarEntrante]
                if rapport<rapportMin and rapport>=0:
                    indiceVarSortante=i
                    rapportMin=rapport
        if indiceVarSortante==0:
            print("Pas de variable sortante")
            exit()
        #Coefficient principal à 1
        tab[indiceVarSortante,:]=1/tab[indiceVarSortante,indiceVarEntrante]*tab[indiceVarSortante,:]
        #Coefficients secondaires à 0
        for i in range(tab.shape[0]):
            if i!=indiceVarSortante:
                tab[i,:]-=tab[i,indiceVarEntrante]*tab[indiceVarSortante,:]
        #Stockage de la position des différentes variables
        x[indiceVarSortante-1]=indiceVarEntrante
    return(tab,x)

tab,x=simplexeStandard(tab)
print(tab)
for i in range(x.size):
    if x[i]<tab.shape[1]-tab.shape[0]:
        print("x",x[i]+1,"=",tab[i+1,-1])
    else:
        print("y",x[i]+1-tab.shape[1]+tab.shape[0],"=",tab[i+1,-1])
print("Optimum de",-tab[0,-1])
