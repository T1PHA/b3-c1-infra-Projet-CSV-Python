from ast import Delete
import csv
with open('conso-annuelles_v1.csv',newline='') as f:
    tableau=[]
    lire=csv.reader(f,quoting=csv.QUOTE_NONE)
    print('',end='\n')
    print('Affichage des lignes du tableau',end='\n')

    len_tab = len(tableau)
    print("azezefzfzfzfsdf")
    for i in range (0,len_tab):
        for j in range(0,len(tableau[i])): 
            old_cell = tableau[i][j]
            new_cell=old_cell.strip('"')   
            print (new_cell)
            tableau[i][j] = new_cell
        if tableau[i][j] is None:
            Delete(tableau[i][j])

    for ligne in lire:
        print(ligne,end='\n')
        tableau.append(ligne)





print (len(tableau))

    



#Création d'un fichier à partir de la liste tableau
#with open('conso-clean.csv','w',newline='') as f:  #Ouverture du fichier CSV en écriture
#    ecrire=csv.writer(f)                        # préparation à l'écriture
#    for i in tableau:                           # Pour chaque ligne du tableau...  
#        ecrire.writerow(i)                # Mettre dans la variable ecrire cette nouvelle ligne      
#print('',end='\n')
#print('longueur du tableau : ',len(tableau))