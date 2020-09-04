import numpy as np
np.set_printoptions(linewidth=99999)

#Initialisation
tab1=np.array([
[142,241,0,0,0,0],
[0.23,0.7,1,0,0,20.21],
[0.015,0.015,0,1,0,0.705],
[1.8,1.1,0,0,1,75]])

tab2=np.array([
[1.,2,0,0,0,0],
[-1,3,1,0,0,10],
[5,-4,0,1,0,1],
[-3,1,0,0,1,-1]])

tab3=np.array([
[150.,600,0,0,0],
[6,20,1,0,69],
[2,4,0,1,19]])

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
    tab[indiceVarSortante,:]*=1/tab[indiceVarSortante,indiceVarEntrante]
    for i in range(tab.shape[0]):
        if i!=indiceVarSortante:
            tab[i,:]-=tab[i,indiceVarEntrante]*tab[indiceVarSortante,:]
    return(tab)

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
        indiceVarEntrante=variableEntrante(tab)
        #Recherche de la variable sortante
        indiceVarSortante=variableSortante(tab,indiceVarEntrante)
        if indiceVarSortante==0:
            print("Pas de variable sortante")
            exit()
        #Coefficient principal à 1 et coefficients secondaires à 0
        tab=normalisation(tab,indiceVarEntrante,indiceVarSortante)
        #Stockage de la position des différentes variables
        x[indiceVarSortante-1]=indiceVarEntrante
    return(tab,x)

def simplexePhases(tab,x):
    #Construction du tableau du problème auxiliaire
    tabDelta=auxiliaire(tab)
    #Première phase
    tabDelta,x=phase1(tabDelta,x)
    #On regarde si on peut passer à la seconde phase
    if tabDelta[0,-1]>0:
        print("Le problème n'a pas d'optimum")
        exit()
    #Seconde phase
    tabDelta,x=phase2(tabDelta,x,tab)
    #Retour à la méthode standard
    return(tabDelta,x)

def auxiliaire(tab):
    tabDelta=tab.copy()
    tabDelta[0,:]*=0
    tabGauche=tabDelta[:,:-1]
    tabMilieu=-np.ones((tabDelta.shape[0],1))
    tabDroite=tabDelta[:,-1:]
    tabDelta=np.concatenate((tabGauche,tabMilieu,tabDroite),axis=1)
    return(tabDelta)

def phase1(tabDelta,x):
    #Choix de la variable entrante (delta)
    indiceVarEntrante=tabDelta.shape[1]-2
    #Recherche de la variable sortante (la plus petite)
    indiceVarSortante=1
    for i in range(2,tabDelta.shape[0]):
        if tabDelta[i,-1]<tabDelta[indiceVarSortante,-1]:
            indiceVarSortante=i
    #Coefficient principal à 1 et coefficients secondaires à 0
    tabDelta=normalisation(tabDelta,indiceVarEntrante,indiceVarSortante)
    #Stockage de la position des différentes variables
    x[indiceVarSortante-1]=indiceVarEntrante
    #Tant que les coefficients de Lf sont positifs
    while (tabDelta[0,:-1]>np.zeros((1,tabDelta.shape[1]-1))).any():
        #Recherche de la variable entrante
        indiceVarEntrante=variableEntrante(tabDelta)
        #Recherche de la variable sortante en privilégiant delta
        indiceVarSortante=0
        rapportMin=np.inf
        for i in range(1,tabDelta.shape[0]):
            if tabDelta[i,indiceVarEntrante]>0:
                rapport=tabDelta[i,tabDelta.shape[1]-1]/tabDelta[i,indiceVarEntrante]
                #On privilégie delta en cas d'égalité
                if rapport==rapportMin and x[i]==tabDelta.shape[1]-2:
                    indiceVarSortante=i
                    rapportMin=rapport
                if rapport<rapportMin and rapport>=0:
                    indiceVarSortante=i
                    rapportMin=rapport
        if indiceVarSortante==0:
            print("Pas de variable sortante")
            exit()
        #Coefficient principal à 1 et coefficients secondaires à 0
        tabDelta=normalisation(tabDelta,indiceVarEntrante,indiceVarSortante)
        #Stockage de la position des différentes variables
        x[indiceVarSortante-1]=indiceVarEntrante
    return(tabDelta,x)

def phase2(tabDelta,x,tab):
    #Suppression de la colonne delta
    tabGauche=tabDelta[:,:-2]
    tabDroite=tabDelta[:,-1:]
    tabDelta=np.concatenate((tabGauche,tabDroite),axis=1)
    #Réécriture du critère initial
    for i in range(x.size):
        if x[i]<tabDelta.shape[1]-tabDelta.shape[0]:
            tabDelta[0,tabDelta.shape[1]-tabDelta.shape[0]:]-=tab[0,x[i]]*tabDelta[i+1,tabDelta.shape[1]-tabDelta.shape[0]:]
    return(tabDelta,x)

def simplexeCoupes(tab):
    #On résout le tableau par la méthode standard
    tabCoupe,x=simplexeStandard(tab)
    #On repère les coefficients non entiers de la dernière colonne
    indiceCoefsFrac=[]
    for i in range(1,tabCoupe.shape[0]):
        if np.around(tabCoupe[i,-1]%1,5)!=0 and np.around(tabCoupe[i,-1]%1,5)!=1:
            indiceCoefsFrac.append(i)
    #Tant qu'il y a des coefficients non entiers sur la dernière colonne on continue
    while len(indiceCoefsFrac)>0:
        #Recherche de la plus grande partie fractionnaire
        indiceFracMax=indiceCoefsFrac[0]
        fracMax=tabCoupe[indiceCoefsFrac[0],-1]%1
        for i in indiceCoefsFrac:
            frac=tabCoupe[i,-1]%1
            if frac>fracMax:
                indiceFracMax=i
                fracMax=frac
        #Insertion de la ligne coupe
        ligneCoupe=-(tabCoupe[[indiceFracMax],:]%1)
        tabCoupe=np.concatenate((tabCoupe,ligneCoupe))
        #Insertion de la colonne de la nouvelle variable z
        tabGauche=tabCoupe[:,:-1]
        tabMilieu=np.zeros((tabCoupe.shape[0],1))
        tabMilieu[-1,0]=1
        tabDroite=tabCoupe[:,-1:]
        tabCoupe=np.concatenate((tabGauche,tabMilieu,tabDroite),axis=1)
        #Choix de la variable sortante
        indiceVarSortante=tabCoupe.shape[0]-1
        #Choix de la variable entrante
        rapportMin=np.inf
        for i in range(tabCoupe.shape[1]-1):
            if tabCoupe[indiceVarSortante,i]*tabCoupe[0,i]!=0:
                rapport=tabCoupe[0,i]/tabCoupe[indiceVarSortante,i]
                if rapport<rapportMin:
                    indiceVarEntrante=i
                    rapportMin=rapport
        #Coefficient principal à 1 et coefficients secondaires à 0
        tabCoupe=normalisation(tabCoupe,indiceVarEntrante,indiceVarSortante)
        #Stockage de la position des différentes variables
        x=np.concatenate((x,np.array([indiceVarEntrante])))
        #On repère les coefficients non entiers de la dernière colonne
        indiceCoefsFrac=[]
        for i in range(1,tabCoupe.shape[0]):
            if np.around(tabCoupe[i,-1]%1,5)!=0 and np.around(tabCoupe[i,-1]%1,5)!=1:
                indiceCoefsFrac.append(i)
    return(tabCoupe,x)

tab,x=simplexeCoupes(tab3)
print(tab)
for i in range(x.size):
    if x[i]<tab.shape[1]-tab.shape[0]:
        print("x",x[i]+1,"=",np.around(tab[i+1,-1],3))
    else:
        print("y",x[i]+1-tab.shape[1]+tab.shape[0],"=",np.around(tab[i+1,-1],3))
print("Optimum de",-np.around(tab[0,-1],3))
