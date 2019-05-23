import pandas
import const

import matplotlib.pyplot as plt
import pandas
import const

print(pandas.__version__)

def nettoyage(doc):
    dataframe = pandas.read_csv(f"{doc}.csv" , header=0)
    dataframe = dataframe.loc[dataframe['code_postal'].isin(const.codes2)]
    dataframe = dataframe.loc[dataframe['type_local']== "Appartement"]
    dataframe= dataframe.drop(['numero_disposition' , 'nature_mutation' , 'adresse_numero' , 'adresse_suffixe' ,
                          'adresse_nom_voie' , 'adresse_code_voie' , 'code_commune' ,
                          'nom_commune' , 'code_departement' , 'ancien_code_commune' ,
                          'ancien_nom_commune' , 'id_parcelle' , 'ancien_id_parcelle' ,
                          'numero_volume' , 'lot1_numero' , 'lot1_surface_carrez' , 'lot2_numero' ,
                          'lot2_surface_carrez' , 'lot3_numero' , 'lot3_surface_carrez' ,
                          'lot4_numero' , 'lot4_surface_carrez' , 'lot5_numero' ,
                          'lot5_surface_carrez' , 'nombre_lots' , 'code_type_local' , 'type_local' ,
                          'nombre_pieces_principales' ,
                          'code_nature_culture' , 'nature_culture' , 'code_nature_culture_speciale' ,
                          'nature_culture_speciale' , 'surface_terrain'] , axis=1)
    dataframe['metre_carre'] = dataframe.valeur_fonciere / dataframe.surface_reelle_bati
    dataframe=dataframe.dropna()
    return dataframe

dflyon_2014=nettoyage('69_2014')
dflyon_2015=nettoyage('69_2015')
dflyon_2016=nettoyage('69_2016')
dflyon_2017=nettoyage('69_2017')
dflyon_2018=nettoyage('69_2018')

#pandas.set_option('display.max_columns', 10)
print(dflyon_2014)

#histogramme de l'âge
#dflyon_2014.hist(column='metre_carre')

#scatterplot
dflyon_2014.plot.scatter(x='surface_reelle_bati',y='valeur_fonciere')#valeur_fonciere / dataframe.surface_reelle_bati
plt.show()








