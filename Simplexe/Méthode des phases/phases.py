import numpy as np
np.set_printoptions(linewidth=99999)

#Initialisation
tab=np.array([
[142,241,0,0,0,0],
[0.23,0.7,1,0,0,20.21],
[0.015,0.015,0,1,0,0.705],
[1.8,1.1,0,0,1,75]])

tab2=np.array([
[1,2,0,0,0,0],
[-1,3,1,0,0,10],
[5,-4,0,1,0,1],
[-3,1,0,0,1,-1]])

def simplexeStandard(tab):
    #On crée un vecteur dont l'i-ème élément est l'indice de la variable dont la
    #valeur est à la fin de la i+1-ème ligne du tableau
    x=np.arange(tab.shape[1]-tab.shape[0],tab.shape[0]+1)
    #Tant que les coefficients de Lf sont positifs
    while (tab[0,:-1]>np.zeros((1,tab.shape[1]-1))).any():
        #Si une des variables est négative on applique la méthode des phases
        for i in range(1,tab.shape[0]):
            if tab[i,-1]<0:
                tab,x=simplexePhases(tab,x)
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

def simplexePhases(tab,x):
    #Construction du tableau du problème auxiliaire
    tabDelta=tab.copy()
    tabDelta[0,:]*=0
    tabGauche=tabDelta[:,:-1]
    tabMilieu=-np.ones((tabDelta.shape[0],1))
    tabDroite=tabDelta[:,-1:]
    tabDelta=np.concatenate((tabGauche,tabMilieu,tabDroite),axis=1)
    #Première phase
    #Choix de la variable entrante (delta)
    indiceVarEntrante=tabDelta.shape[1]-2
    #Recherche de la variable sortante (la plus petite)
    indiceVarSortante=1
    for i in range(2,tabDelta.shape[0]):
        if tabDelta[i,-1]<tabDelta[indiceVarSortante,-1]:
            indiceVarSortante=i
    #Coefficient principal à 1
    tabDelta[indiceVarSortante,:]=1/tabDelta[indiceVarSortante,indiceVarEntrante]*tabDelta[indiceVarSortante,:]
    #Coefficients secondaires à 0
    for i in range(tabDelta.shape[0]):
        if i!=indiceVarSortante:
            tabDelta[i,:]-=tabDelta[i,indiceVarEntrante]*tabDelta[indiceVarSortante,:]
    #Stockage de la position des différentes variables
    x[indiceVarSortante-1]=indiceVarEntrante
    #Tant que les coefficients de Lf sont positifs
    while (tabDelta[0,:-1]>np.zeros((1,tabDelta.shape[1]-1))).any():
        #Recherche de la variable entrante
        indiceVarEntrante=0
        for i in range(1,tabDelta.shape[1]-1):
            if tabDelta[0,i]>tabDelta[0,indiceVarEntrante]:
                indiceVarEntrante=i
        #Recherche de la variable sortante
        indiceVarSortante=0
        rapportMin=np.inf
        for i in range(1,tabDelta.shape[0]):
            if tabDelta[i,indiceVarEntrante]>0:
                rapport=tabDelta[i,tabDelta.shape[1]-1]/tabDelta[i,indiceVarEntrante]
                #On privilégie delta en cas d'égalité
                if rapport==rapportMin and x[i]==tabDelta.shape[1]-2:
                    indiceVarSortante=i
                    rapportMin=rapport
                elif rapport<rapportMin and rapport>=0:
                    indiceVarSortante=i
                    rapportMin=rapport
        if indiceVarSortante==0:
            print("Pas de variable sortante")
            exit()
        #Coefficient principal à 1
        tabDelta[indiceVarSortante,:]=1/tabDelta[indiceVarSortante,indiceVarEntrante]*tabDelta[indiceVarSortante,:]
        #Coefficients secondaires à 0
        for i in range(tabDelta.shape[0]):
            if i!=indiceVarSortante:
                tabDelta[i,:]-=tabDelta[i,indiceVarEntrante]*tabDelta[indiceVarSortante,:]
        #Stockage de la position des différentes variables
        x[indiceVarSortante-1]=indiceVarEntrante
    #On regarde si on peut passer à la seconde phase
    if tabDelta[0,-1]>0:
        print("Le problème n'a pas d'optimum")
        exit()
    #Seconde phase
    #Suppression de la colonne delta
    tabGauche=tabDelta[:,:-2]
    tabDroite=tabDelta[:,-1:]
    tabDelta=np.concatenate((tabGauche,tabDroite),axis=1)
    #Réécriture du critère initial
    for i in range(x.size):
        if x[i]<tabDelta.shape[1]-tabDelta.shape[0]:
            tabDelta[0,tabDelta.shape[1]-tabDelta.shape[0]:]-=tab[0,x[i]]*tabDelta[i+1,tabDelta.shape[1]-tabDelta.shape[0]:]
    return(tabDelta,x)

tab,x=simplexeStandard(tab)
print(tab)
for i in range(x.size):
    if x[i]<tab.shape[1]-tab.shape[0]:
        print("x",x[i]+1,"=",tab[i+1,-1])
    else:
        print("y",x[i]+1-tab.shape[1]+tab.shape[0],"=",tab[i+1,-1])
print("Optimum de",-tab[0,-1])
