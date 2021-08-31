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
catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")

    elif int(inputs[0]) == 2:
        A_IN =input ("Ingrese el año inicial: ")
        A_FN =input ("Ingrese el año final: ")
        print("Lista cronologica de artistas: ")

    elif int(inputs[0]) == 3:
        F_IN =input ("Ingrese la fecha inicial (AAAA-MM-DD): ")
        F_FN =input ("Ingrese la fecha final (AAAA-MM-DD): ")
        print("Lista cronologica de adquisiciones: ")

    elif int(inputs[0]) == 4:
        Name =input ("Ingrese el nombre del artista: ")
        print("Obras de un artista por técnica: ")

    elif int(inputs[0]) == 5:
        print("Obras por la nacionalidad de sus creadores: ")

    elif int(inputs[0]) == 6:
        DEP =input("Ingrese el departamento a consultar: ")
        print("Costo de transporte: ")

    elif int(inputs[0]) == 7:
        A_IO =input("Ingrese el año inicial de las obras: ")
        A_FO =input("Ingrese el año final de las obras: ")
        Area_D =input("Ingrese el área disponible: ")
        print("Propuesta de una nueva exposición:  ")

    else:
        sys.exit(8)
sys.exit(8)
