import config as conf
import csv
from ADT import list as lt
from DataStructures import listiterator

# 1) Cargar archivos

casting = lt.newList('SINGLE_LINKED', None)

with open('Data/MoviesCastingRaw-small.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        lt.addFirst(casting, row)


details = lt.newList('SINGLE_LINKED', None)

with open('Data/SmallMoviesDetailsCleaned.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        lt.addFirst(details, row)


#2) Filtrar

casting_por_director = lt.newList('SINGLE_LINKED', None)

director = input("Ingrese el director\n")

iter = listiterator.newIterator(casting)
while listiterator.hasNext(iter):
    a = listiterator.next(iter)
    if a["director_name"] == director:
        lt.addFirst(casting_por_director, a)


details_buenos = lt.newList('SINGLE_LINKED', None)

iter2 = listiterator.newIterator(details)
while listiterator.hasNext(iter2):
    a = listiterator.next(iter2)
    if a["vote_average"] > 6:
        lt.addFirst(details_buenos, a)
    
# 3) Unir las listas



# iter3 = listiterator.newIterator(details_buenos)
# while listiterator.hasNext(iter3):
#     a = listiterator.next(iter3)

#     iter4 = listiterator.newIterator()
#     while listiterator.hasNext(iter3):
#         a = listiterator.next(iter3)
    

# print(lt.size(casaails))

