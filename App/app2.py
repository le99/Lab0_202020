import config as conf
import csv
from ADT import list as lt
from DataStructures import listiterator

# 0) Imprimir menu

print("1- Req 1 - Encontrar buenas películas de un director")

# 1) Cargar archivos

casting = lt.newList('SINGLE_LINKED', None)

with open('Data/MoviesCastingRaw-small.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        lt.addFirst(casting, row)


details = lt.newList('SINGLE_LINKED', None)

with open('Data/SmallMoviesDetailsCleaned.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        lt.addFirst(details, row)


#2) Filtrar

casting_por_director = lt.newList('SINGLE_LINKED', None)
director = input("Ingrese el director\n")

iter = listiterator.newIterator(casting)
while listiterator.hasNext(iter):
    c = listiterator.next(iter)
    if c["director_name"] == director:
        lt.addFirst(casting_por_director, c)


details_buenos = lt.newList('SINGLE_LINKED', None)

iter = listiterator.newIterator(details)
while listiterator.hasNext(iter):
    d = listiterator.next(iter)
    if float(d["vote_average"]) > 6:
        lt.addFirst(details_buenos, d)
    
# 3) Unir las listas

union_listas = lt.newList('SINGLE_LINKED', None)

iter1 = listiterator.newIterator(details_buenos)
while listiterator.hasNext(iter1):
    d = listiterator.next(iter1)

    iter2 = listiterator.newIterator(casting_por_director)
    while listiterator.hasNext(iter2):
        c = listiterator.next(iter2)

        if d["id"] == c["id"]:
            union_d_con_c = {**d, **c}
            lt.addFirst(union_listas, union_d_con_c)
            break

# 4) Calcular numero de peliculas y promedio
numero_de_peliculas_director = lt.size(union_listas)
suma_vote_average = 0.0

iter = listiterator.newIterator(union_listas)
while listiterator.hasNext(iter):
    u = listiterator.next(iter)
    suma_vote_average = suma_vote_average + float(u["vote_average"])

promedio_peliculas = suma_vote_average/numero_de_peliculas_director

# 5) Imprimir resultados

print("Peliculas con vote_average >= 6: " + str(numero_de_peliculas_director))
print("Promedio (Peliculas con vote_average >= 6): " + str(promedio_peliculas))