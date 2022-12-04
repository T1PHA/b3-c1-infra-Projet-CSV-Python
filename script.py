
import csv
from operator import itemgetter, attrgetter
import codecs
import unicodedata

#variables qui sont les fichiers d'entrée et de sortie
tableau_init_csv = "conso-annuelles_v1.csv"

tableau_clean_csv = "conso-clean.csv"

#Tableau qui aura les données
tableau_clean = []
count = 0

        

    
# fonction qu'on va apeller a la fin pour pouvoir ecrire dans le fichier final
def ecrire_csv(tableau_clean):

    with open(tableau_clean_csv, 'w', newline='', encoding="utf-8") as csv_file:
        #On déclare l'en tête qu'on écrira a la fin dans le fichier
        fieldnames=['Appareil suivi | ' 'Consommation annuelle AN1+AN2 | ' 'Type']
        
        ecrire= csv.DictWriter(csv_file, fieldnames=fieldnames)
        ecrire.writeheader()
        
        #Ecriture des lignes dans la variable tableau et dans le fichier final
        ecrire = csv.writer(csv_file)
        ecrire.writerows(tableau_clean)
        
  #### FONCTIONS ####

#Fonction principale qui va effectuer les modifications du fichier
def colonnes(tableau_clean):
    
    
    # On commence par supprimer la colonne id logement
    tableau_clean.pop(1)

    #Va remplacer les ? par la lettre e (qui sera en accord avec le mot)
    tableau_clean[0] = unicodedata.normalize('NFKD', tableau_clean[0]).replace('�', 'e')
    tableau_clean[1] = unicodedata.normalize('NFKD', tableau_clean[1]).replace('�', 'e')
    tableau_clean[2] = unicodedata.normalize('NFKD', tableau_clean[2]).replace('�', 'E')
    tableau_clean[3] = unicodedata.normalize('NFKD', tableau_clean[3]).replace('�', 'E')
    
    #"fonction" qui ne prends seulement en compte les lignes ou il n'y a pas de case vide; donc les lignes vides ne sont pas affichées et pas prises en compte
    #len_tab = len(tableau_clean)
    IndexLigne=1
    for ligne in tableau_clean:
        # si une case est vide, on ne lui exécute pas la suite du code (elle est donc mise de coté) carr il prend seulement les IndexLigne = 1
        if len(ligne) == 0:
            IndexLigne = 0

    
    # count = 0 pour exécuter le code qu'une seule fois      
    if IndexLigne==1 and count == 0:
        #On déclare les variables qui vont remplacer les colonnes
        l1 = tableau_clean[1].replace(',','.').replace('-','0')
        l2 = tableau_clean[2].replace(',','.').replace('-','0')

        #On effectue l'opération conso N1 + conso n2 dans une nouvelle colonne qui les fusionne
        consoN12 = float(l1) + float(l2)
        
        # On supprime les 2 colonnes an1 et an2 pour les remplacer par une seule qui contient la fusion des deux
        # 2 fois pop(1) car la colonne se décale et devient position 1 dans le tableau
        tableau_clean.pop(1) and tableau_clean.pop(1) and tableau_clean.insert(1, consoN12)

        return tableau_clean
count+1    
print("Fonction exécutée")

#### FIN FONCTIONS  #####


#Fonction qui va lire le fichier de base et prendre la fonction d'écriture qui elle écrit dans le fichier final en exécutant notre programme
def lire_csv():
    
    with open(tableau_init_csv, 'r', encoding="utf-8") as csv_file:
        
        lire = csv.reader(csv_file, delimiter = ';')  
        next(lire, 0)
        
        #Va exécuter mes fonctions pour chaque ligne de mon tab leau 
        for i in lire:
            #On met la fonction principale dans une variable pour pouvoir l'exécuter sur toutes les lignes
            test = colonnes(i)
            
                
            if count == 0:
                #On spécifie que le type soit bien une liste pour pouvoir opérer sur la variable
                if type(test) is list:
                    #On ajoute au tableau notre variable qui va exécuter notre fonction
                    tableau_clean.append(test)
                    #Tri d'abord par Type en  ordre décroissant puis par conso par ordre décroissant
                    tableau_clean.sort(key=lambda x: (x[2], x[1]), reverse=True)
            else: 
                print("erreur")
            
    #Ecrire dans le nouveau csv avec les donnees de tableau_clean selon les opérations précédentes       
    ecrire_csv(tableau_clean)
lire_csv()

