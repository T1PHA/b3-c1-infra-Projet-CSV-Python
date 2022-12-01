from ast import Delete
import csv
from queue import Empty
from operator import itemgetter, attrgetter

with open('conso-annuelles_v1.csv',newline='') as f:
    tableau=[]
    lire=csv.reader(f,delimiter=";",quoting=csv.QUOTE_NONE)
    print('',end='\n')
    print('Affichage des lignes du tableau',end='\n')

    for ligne in lire:
        #print(ligne,end='\n')
        tableau.append(ligne)

        
########################### Affichage du tableau ############################
def ShowTab(tableau):
    lire = tableau
    for ligne in lire:
        print(ligne,end='\n')
        
########################### Test case vide ############################
def Empty_cell(tableau):
    IndexLigne=0 
    lire = tableau  
    for ligne in lire:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",tableau[IndexLigne])
        for cell in ligne:
            if not (cell) :  
                print(tableau[IndexLigne])     
                tableau.remove(tableau[IndexLigne])
        IndexLigne=IndexLigne+1 
    return tableau    

###########################Suppression de la colonne ID logement ############################   
def DelId(tableau):
    IndexLigne=0
    for row in tableau:      
        del tableau[IndexLigne][1]
        IndexLigne=IndexLigne+1
    return tableau

########################### Addition des 2 consommations ############################
def fusion(tableau):
    IndexLigne=0
    for row in tableau:
        CA1= tableau[IndexLigne][1]        
        CA2= tableau[IndexLigne][2]        
        CAT= CA1 +CA2     
        tableau.pop(1) and tableau.pop(1) and tableau.insert(1, CAT) 
        IndexLigne=IndexLigne+1 
    return tableau

########################### Rangement du tableau ############################
def tri(tableau):
    #tableau.sort()
    sorted(tableau, key=itemgetter(2), reverse=False)


########################### Run ############################
Empty_cell(tableau)
ShowTab(tableau)
print(len(tableau))
print('######################################################')
print('######################################################')
print('######################################################')


print(len(tableau))

#DelId(tableau)
#fusion(tableau)
#tri(tableau)
#ShowTab(tableau)




########################### Création du nouveau fichier csv ############################ 


#Création d'un fichier à partir de la liste tableau
#with open('conso-clean.csv','w',newline='') as f:  #Ouverture du fichier CSV en écriture
#    ecrire=csv.writer(f)                        # préparation à l'écriture
#    for i in tableau:                           # Pour chaque ligne du tableau...  
#        ecrire.writerow(i)                # Mettre dans la variable ecrire cette nouvelle ligne      
#print('',end='\n')
#print('longueur du tableau : ',len(tableau))