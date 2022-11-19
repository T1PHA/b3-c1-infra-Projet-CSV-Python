
import csv
from operator import itemgetter, attrgetter
import codecs


tableau_init_csv = "conso-annuelles_v1.csv"

tableau_clean_csv = "conso-clean.csv"


tableau_clean = []
count = 0

        

    
# methodes qu'on va apeller a la fin pour pouvoir ecrire dans le fichier final
def ecrire_csv(tableau_clean):

    with open(tableau_clean_csv, 'w', newline='', encoding="iso-8859-1") as csv_file:

        fieldnames=['Appareil suivi','Consommation annuelle AN1+AN2','Type']
        
        ecrire= csv.DictWriter(csv_file, fieldnames=fieldnames)
        ecrire.writeheader()
        
        
        ecrire = csv.writer(csv_file)
        ecrire.writerows(tableau_clean)
        
  #### FONCTIONS ####
  
  
  

# def Empty_cell(tableau):
#     len_tab = len(tableau)
#     IndexLigne=0

#     for ligne in tableau:
#         for cell in ligne:
#             if not (cell) :
#                 tableau.remove(tableau[IndexLigne])
#         IndexLigne=IndexLigne+1 
#     return tableau 


 # def tri(tableau_clean) -> list:
#     for key in tableau_clean:
  
   
def colonnes(tableau_clean):

    # Supprime la colonne id logement
    tableau_clean.pop(1)

    
    #"fonction" qui ne prends seulement en compte les lignes ou il n'y a pas de case vide; donc les lignes vides ne sont pas affichées
    #len_tab = len(tableau_clean)
    IndexLigne=0
    for ligne in tableau_clean:
        if len(ligne) == 0:
            IndexLigne = 1          
    if IndexLigne==0 and count == 0:
        
        #conso N1 + conso n2 dans une nouvelle colonne qui les fusionne
        consoN12 = float(tableau_clean[1].replace(',','.').replace('-','0')) + float(tableau_clean[2].replace(',','.').replace('-','0'))
        # 2 fois 1 car la colonne se décale et devient 1
        tableau_clean.pop(1) and tableau_clean.pop(1) and tableau_clean.insert(1, consoN12) 
        
        #test tri
        # tableau_tri = str(tableau_clean)
        # sorted(tableau_tri, key=itemgetter(1), reverse=True)

        return tableau_clean
    count+1    
    
    
       

#### FIN FONCTIONS  #####



def lire_csv():
    
    with open(tableau_init_csv, 'r', encoding="iso-8859-1") as csv_file:
        lire = csv.reader(csv_file, delimiter = ';')
        # pour lire tt les lignes
       
        next(lire, 0)
            
        for i in lire:
            test = colonnes(i)
            # test_tri = tri(tableau_clean)
            if type(test) is list:
                tableau_clean.append(test)

            # if type(test_tri) is list:
            #     tableau_clean.append(test_tri)

                
                
            # if type(test_tri) is list:
            #     tableau_clean.append(test_tri)
            
            
    #Ecrire dans le nv csv avec les donnees de tableau_clean       
    ecrire_csv(tableau_clean)
lire_csv()

