def transformation(fichier):
  return [line.rstrip('\n').split(',') for line in open(fichier)]

liste2015=transformation('69_2015.csv')
print(liste2015)

"""
lineList = list()

lineList = [line.rstrip('\n') for line in open('valeursfoncieres-2014.txt')]

for i in range(len(lineList)):
  lineList[i]= lineList[i].split('|')

print(lineList[1])

liste= [69001, 69002, 69003, 69004, 69005, 69006, 69007,69008, 69009]
"""



