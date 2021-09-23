﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronológicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Transportar obras de un departamento")
    print("7- Proponer una nueva exposición en el museo")
    print("8- Salir del Menu")

def initCatalog():
    return controller.initCatalog()

def loadData(catalog):
    controller.loadData(catalog)

catalog = None
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog ()
        loadData (catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['artist'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))

    elif int(inputs[0]) == 2:
        A_I = input ("Ingresa el año inicial: ")
        A_FN = input ("Ingresa el año final: ")
        lista = controller.listar_artist_date(A_I , A_FN , catalog)
        print ("Se cargaron un total de", len(lista), "Artistas")
        print ("Los primeros 3 artistas son:" , lista[0],lista[1],lista[2])
        print ("Los últimos 3 artistas son:" , lista[len(lista)-1],lista[len(lista)-2],lista[len(lista)-3])

    elif int(inputs[0]) == 3:
        F_I = input ("Ingresa la fecha inicial (AAAA-MM-DD): ")
        F_FN = input ("Ingresa la fecha final (AAAA-MM-DD): ")
        lista = controller.listar_artwork_date(F_I, F_FN, catalog)
        print ("Se cargaron un total de", len(lista[0]), "Obras de Arte, en donde un total de", lista[1], "fueron compradas")
        print ("Los primeros 3 artistas son:" , lista[0][0],lista[0][1],lista[0][2])
        print ("Los últimos 3 artistas son:" , lista[0][len(lista[0])-1],lista[0][len(lista[0])-2],lista[0][len(lista[0])-3])

    elif int(inputs[0]) == 4:
        Name = input ("Ingresa el nombre del artista: ")
        l_t= controller.l(Name,catalog)
        
        print("Obras de un artista por técnica: ")
        print(l_t)
        
       
    elif int(inputs[0]) == 5:
        print("Obras por la nacionalidad de sus creadores: ")

    elif int(inputs[0]) == 6:
        DEP = input("Ingresa el departamento a consultar: ")
        print("Costo de transporte: ")

    elif int(inputs[0]) == 7:
        A_IO = input("Ingresa el año inicial de las obras: ")
        A_FO = input("Ingresa el año final de las obras: ")
        Area_D = input("Ingresa el área disponible: ")
        print("Propuesta de una nueva exposición:  ")

    else:
        sys.exit(8)
sys.exit(8)
