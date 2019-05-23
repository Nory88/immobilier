 #indiquer que l'on veut voir apparaître les graphiques dans le notebook
#/!\ très important, sinon on ne verrait rien
#matplotlib inline
#importation de la librairie
import matplotlib.pyplot as plt
import pandas
import const
import immobilier2

#histogramme de l'âge
immobilier2.dflyon_2014.hist(column='metre_carre')
plt.show()