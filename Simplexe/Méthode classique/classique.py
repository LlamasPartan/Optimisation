import numpy as np

#Initialisation
tab=np.array([
[10.,-57,-9,-24,100,0,0,0,0,0],
[0,0,0,0,1,1,0,0,0,1],
[0.5,-5.5,-2.5,9,1,0,1,0,0,1],
[0.5,-1.5,-0.5,1,1,0,0,1,0,1],
[1,0,0,0,1,0,0,0,0,2]])

def simplexeStandard(tab):
    x=np.zeros(tab.shape[1]-tab.shape[0])
    #Tant que les coefficients de Lf sont positifs
    while (tab[0,:]>np.zeros((1,tab.shape[1]))).any():
        #Recherche de la variable entrante
        indiceVarEntrante=0
        for i in range(1,tab.shape[1]-1):
            if tab[0,i]>tab[0,indiceVarEntrante]:
                indiceVarEntrante=i
        #Recherche de la variable sortante
        indiceVarSortante=0
        rapportMin=-1
        while rapportMin<0:
            indiceVarSortante+=1
            if indiceVarSortante<tab.shape[0]:
                if tab[indiceVarSortante,indiceVarEntrante]!=0:
                    rapportMin=tab[indiceVarSortante,tab.shape[1]-1]/tab[indiceVarSortante,indiceVarEntrante]
            else :
                print("Pas de variable sortante")
                exit()
        for i in range(indiceVarSortante+1,tab.shape[0]):
            if tab[i,indiceVarEntrante]!=0:
                rapport=tab[i,tab.shape[1]-1]/tab[i,indiceVarEntrante]
                if rapport<rapportMin and rapport>=0:
                    indiceVarSortante=i
                    rapportMin=rapport
        #Coefficient principal à 1
        tab[indiceVarSortante,:]=1/tab[indiceVarSortante,indiceVarEntrante]*tab[indiceVarSortante,:]
        #Coefficients secondaires à 0
        for i in range(tab.shape[0]):
            if i!=indiceVarSortante:
                tab[i,:]-=tab[i,indiceVarEntrante]*tab[indiceVarSortante,:]
        #Stockage de la position des différentes variables
        x[indiceVarEntrante]=indiceVarSortante
    return(tab,x)

res=simplexeStandard(tab)
print(res[0])
for i in range(res[1].size):
    print("x",i+1,"=",res[0][int(res[1][i]),-1])
