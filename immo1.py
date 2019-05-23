import const
import csv

def csvtolist(fichier):
  return [line.rstrip('\n').split(',') for line in open(fichier)]

lineList2014=csvtolist('69_2014.csv')
lineList2015=csvtolist('69_2015.csv')
lineList2016=csvtolist('69_2016.csv')
lineList2017=csvtolist('69_2017.csv')
lineList2018=csvtolist('69_2018.csv')

def isinmetropole(list,nouvelleliste):
    for i in list:
        if i[9] in const.codes:
            nouvelleliste.append(i)

liste2014=[]
liste2015=[]
liste2016=[]
liste2017=[]
liste2018=[]

isinmetropole(lineList2014,liste2014)
isinmetropole(lineList2015,liste2015)
isinmetropole(lineList2016,liste2016)
isinmetropole(lineList2014,liste2014)
isinmetropole(lineList2014,liste2014)
isinmetropole(lineList2014,liste2014)


print(lineList2014[0])

#column 5:valeur fonciere column

#print(liste2014[0])


for i in range(100):
    print(liste2014[i][18:29])
"""
def listtocsv(name):
    with open(f'{name}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        #writer.writerow(lineList2014[0])
        writer.writerows(liste2014)

"""