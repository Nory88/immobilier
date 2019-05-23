#Première étape : il faut charger la librairie Pandas
import pandas
#par convenance pure, nous modifions le nombre de lignes
#à afficher dans les print. L'idée est d'éviter que le tutoriel
#se résume à de multples affichages de longs tableaux
#vous pouvez modifier cette option à votre guise
pandas.options.display.max_rows = 10
#vérifier la version
print(pandas.__version__)

#chargement du fichier
#df est le nom de l'objet de type data frame créé
#sep spécifie le caractère séparateur de colonnes
#header = 0 : la ligne numéro 0 = aux noms des champs
#éventuellement decimal permet d'indiquer le point décimal
df = pandas.read_csv("69_2014.csv")
#vérifions le type de df
print(type(df))