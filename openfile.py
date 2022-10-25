#Lecture du fichier
import csv
with open('conso-annuelles_v1.csv',newline='') as f:
    tableau=[]
    lire=csv.reader(f)
    print('',end='\n')
    print('Affichage des lignes du tableau',end='\n')
    # -> test tri //  print("Sorting based on the type:\n", sorted(tableau, key=lambda i: i['Type']))
    
    for ligne in lire:
        print(ligne,end='\n')
        tableau.append(ligne)

#Création d'un fichier à partir de la liste tableau
with open('conso-clean.csv','w',newline='') as f:  #Ouverture du fichier CSV en écriture
    ecrire=csv.writer(f)                        # préparation à l'écriture
    for i in tableau:                           # Pour chaque ligne du tableau...
        ecrire.writerow(i)                # Mettre dans la variable ecrire cette nouvelle ligne
print('',end='\n')
print('longueur du tableau : ',len(tableau))

#Tri fichier
    # sorted_tab = sorted(tableau, key=lambda x: x[4])
    #     print(sorted_tab)
        
#         tableau = list(lire)

# for conso in tableau:
#     conso['Type'] = int(conso['Type'])

# tableau.sort(key= lambda x: x['Type'])

# # affichage:
# for conso in conso:
#     print(conso['Appareil suivi'], conso['ID logement'], conso['Consommation annuelle AN1'], conso['Consommation annuelle AN2'], conso['Type'])

