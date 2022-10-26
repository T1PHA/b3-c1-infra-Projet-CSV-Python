
import csv


tableau_init_csv = "conso-annuelles_v1.csv"

#tableau_init_csv.to_csv(f'conso-clean.csv',index =False, sep= ';', header = True, na_rep="")
tableau_clean_csv = "conso-clean.csv"



#lire et écrire sur notre variable tableau
def lire_ecrire_csv():
    #tableau csv qui prends les données finales
    tableau_clean = []
    #Ouverture tableau init afin de lire ses données
    with open(tableau_init_csv, 'r') as csv_file:
        lire = csv.reader(csv_file, delimiter = ';')
        #Mettre les données du tableau init dans notre variable tableau
        for ligne in lire:
            print(ligne,end='\n')
            tableau_clean.append(ligne)
            
    #        
    #Fonctions parsing print a mettre
    #
    #Ouverture et création tableau clean en mettant à jour notre variable tableau
    #en mettant la variable tableau clean csv, il ne connait pas le fichier qui lui ait associé (normal puisque il n'existe pas), il le créer
    with open(tableau_clean_csv, 'w', newline='') as csv_file:
    #Ecriture dans nouveau tableau
        ecrire = csv.writer(csv_file)
    #Mise à jour de notre variable tableau
        ecrire.writerows(tableau_clean)
lire_ecrire_csv()



#def tri




#def supprimer lignes vides



# def combiner colonnes