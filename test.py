from ast import Delete
import csv
with open('conso-annuelles_v1.csv',newline='') as f:
    tableau=[]
    lire=csv.reader(f,delimiter=";",quoting=csv.QUOTE_MINIMAL)
    print('',end='\n')
    print('Affichage des lignes du tableau',end='\n')

    
  

    for ligne in lire:
        print(ligne,end='\n')
        tableau.append(ligne)

len_tab = len(tableau)

for i in range (0,len_tab):
    for j in range(0,4):       
        #old_cell = tableau[i][j]
        #new_cell=old_cell.strip()   
        #if (tableau[i][j]) is None :
        #    Delete(tableau[i][j])    
   


print (len(tableau))

    



#Création d'un fichier à partir de la liste tableau
#with open('conso-clean.csv','w',newline='') as f:  #Ouverture du fichier CSV en écriture
#    ecrire=csv.writer(f)                        # préparation à l'écriture
#    for i in tableau:                           # Pour chaque ligne du tableau...  
#        ecrire.writerow(i)                # Mettre dans la variable ecrire cette nouvelle ligne      
#print('',end='\n')
#print('longueur du tableau : ',len(tableau))