import csv
with open('conso-annuelles_v1.csv',newline='') as f:
    tableau=[]
    lire=csv.reader(f)
    print('',end='\n')
    print('Affichage des lignes du tableau',end='\n')
    for ligne in lire:
        print(ligne,end='\n')
        tableau.append(ligne)

#Création d'un fichier à partir de la liste tableau
with open('tableur1.csv','w',newline='') as f:  #Ouverture du fichier CSV en écriture
    ecrire=csv.writer(f)                        # préparation à l'écriture
    for i in tableau:                           # Pour chaque ligne du tableau...  
        ecrire.writerow(i)                # Mettre dans la variable ecrire cette nouvelle ligne      
print('',end='\n')
print('longueur du tableau : ',len(tableau))