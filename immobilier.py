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
df = pandas.read_csv("69_2014.csv",header = 0)
#vérifions le type de df
print(type(df))
print(df)

#dimensions : nombre de lignes, nombre de colonnes
#la ligne d'en-tête n'est pas comptabilisée
#dans le nombre de lignes
print(df.shape)

#afficher les premières lignes du jeu de données
print(df.head())

#énumération des colonnes
print(df.columns)

#type de chaque colonne
print(df.dtypes)

#informations sur les données
print(df.info())

#description des données
print(df.describe(include='all'))

"""
Certains indicateurs statistiques ne sont valables que pour les variables numériques (ex. moyenne, min, etc. pour age,
tauxmax,...), et inversemment pour les non-numériques (ex. top, freq, etc. pour sexe, typedouleur, ...), d'où les NaN dans
certaines situations.
"""
"""
# Drop a row by condition
df[df.Name != 'Alisa']
"""