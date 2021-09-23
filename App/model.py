"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

from typing import BinaryIO
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as mrgs
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorías de
los mismos.
"""

# Construccion de modelos

def newCatalog():

    catalog = {'artist': None,
               'artworks': None,}

    catalog['artist'] = lt.newList('ARRAY_LIST')
    catalog['artworks'] = lt.newList('ARRAY_LIST')

    return catalog

# Funciones para agregar informacion al catalogo

def addArtist (catalog, artist):
    art = newArtist(artist['ConstituentID'], artist['DisplayName'],
                    artist['ArtistBio'], artist['Nationality'],
                    artist['Gender'], artist['BeginDate'],
                    artist['EndDate'], artist['WikiQID'], artist['ULAN'])
    lt.addLast(catalog['artist'], art)

def addArtworks (catalog, artworks):
    artw = newArtwork(artworks['ObjectID'], artworks['Title'], artworks['ConstituentID'],
                    artworks['Date'], artworks['Medium'], artworks['Dimensions'],
                    artworks['CreditLine'], artworks['AccessionNumber'], artworks['Classification'],
                    artworks['Department'], artworks['DateAcquired'], artworks['Cataloged'],
                    artworks['URL'], artworks['Circumference'], artworks['Depth'],
                    artworks['Diameter'], artworks['Height'], artworks['Length'],
                    artworks['Weight'], artworks['Width'], artworks['SeatHeight'],
                    artworks['Duration'])
    lt.addLast(catalog['artworks'], artw)	

# Funciones para creacion de datos

def newArtist(ConstituentID, DisplayName, ArtistBio, Nationality, Gender, BeginDate, EndDate, WikiQID, ULAN):
    artist = {'ConstituentID': '', 'DisplayName': '', 'ArtistBio': '',
            'Nacionality': '', 'Gender': '', 'BeginDate': '',
            'EndDate': '', 'WikiQID': '', 'ULAN': ''}
    artist['ConstituentID'] = ConstituentID
    artist['DisplayName'] = DisplayName
    artist['ArtistBio'] = ArtistBio
    artist['Nationality'] = Nationality
    artist['Gender'] = Gender
    artist['BeginDate'] = BeginDate
    artist['EndDate'] = EndDate
    artist['WikiQID'] = WikiQID
    artist['ULAN'] = ULAN
    
    return artist

def newArtwork(ObjectID, Title, ConstituentID, Date, Medium, Dimensions, CreditLine, AccessionNumber, Classification,
            Department, DateAcquired, Cataloged, URL, Circumference, Depth, Diameter, Height, Length, Weight, Width,
            SeatHeight, Duration):

    artworks = {'ObjectID': '', 'Title': '', 'ConstituentID': '', 'Date': '',
                'Medium': '', 'Dimensions': '', 'CreditLine': '', 'AccessionNumber': '',
                'Classification': '', 'Department': '', 'DateAcquired': '', 'Cataloged': '',
                'URL': '', 'Circumference': '', 'Depth': '', 'Diameter': '', 'Height': '',
                'Length': '', 'Weight': '', 'Width': '', 'SeatHeight': '', 'Duration': ''}
    artworks['ObjectID'] = ObjectID
    artworks['Title'] = Title
    artworks['ConstituentID'] = ConstituentID
    artworks['Date'] = Date
    artworks['Medium'] = Medium
    artworks['Dimensions'] = Dimensions
    artworks['CreditLine'] = CreditLine
    artworks['AccessionNumber'] = AccessionNumber
    artworks['Classification'] = Classification
    artworks['Department'] = Department
    artworks['DateAcquired'] = DateAcquired
    artworks['Cataloged'] = Cataloged
    artworks['URL'] = URL
    artworks['Circumference'] =  Circumference
    artworks['Depth'] = Depth
    artworks['Diameter'] = Diameter
    artworks['Height'] = Height
    artworks['Length'] = Length 
    artworks['Weight'] = Weight
    artworks['Width'] = Width
    artworks['SeatHeight'] = SeatHeight
    artworks['Duration'] = Duration
    
    return artworks

# Funciones de consulta

def listar_artist_date(A_I, A_FN, catalog):
    sorted_list = ordenamiento_artist_AI(catalog)
    artist_list = sorted_list ['elements']
    list_date = []
    for artist in artist_list:
        fecha = artist['BeginDate']
        if (fecha >= A_I) and (fecha <= A_FN):
            datos_artist = [artist['DisplayName'], artist['BeginDate'], artist['EndDate'], artist['Nationality'], artist['Gender']]
            list_date.append(datos_artist)
    
    return list_date

def listar_artwork_date(F_I, F_FN, catalog):
    sorted_list = ordenamiento_artworks(catalog)
    artwork_list = sorted_list ['elements']
    contador = 0
    list_date = []
    for artwork in artwork_list:
        fecha = artwork['DateAcquired']
        if (fecha >= F_I) and (fecha <= F_FN):
            artistas = artwork['ConstituentID']
            compra = artwork ['CreditLine']
            datos_artworks = [artwork['Title'], Buscar_artistas (artistas, catalog), artwork['Date'], artwork['DateAcquired'], artwork['Medium'], artwork['Dimensions']]
            list_date.append(datos_artworks)
            if 'Purchase' in compra or 'purchase' in compra:
                contador += 1
    
    return list_date, contador

def Nacionalidad(catalog):
    Lista_final = []
    nacionalidades_f = []
    nacionalidades = []
    artistas = catalog ['artist']['elements']
    obras = catalog ['artworks']['elements']
    Ids = []
    for obra in obras:
        Id = obra['ConstituentID']
        Id = Id.replace('[', '').replace(']', '').replace(' ', '')
        Id = Id.split(',')
        Ids.append(Id)
    for i in Ids:
        for j in i:
            for artista in artistas:
                if (artista['ConstituentID'] == j):
                    nacionalidades.append(artista['Nationality'])
                    for k in nacionalidades:
                        if k not in nacionalidades_f:
                            nacionalidades_f.append (k)
    
    for h in nacionalidades_f:
        if h == '' or h == 'Nationality unknown':
            frecuencia = nacionalidades.count ('') + nacionalidades.count ('Nationality unknown')
            tupla = 'Unknown', frecuencia
            Lista_final.append(tupla)
            nacionalidades_f.remove('')
            nacionalidades_f.remove('Nationality unknown')
        else:
            frecuencia = nacionalidades.count (h)
            tupla = h, frecuencia
            Lista_final.append(tupla)
    
    Lista = Ordenar_lista (Lista_final)

    Lista_1 = MayorNacionalidad (Lista [::-1], catalog)
    
    return Lista [::-1], Lista_1

def MayorNacionalidad (lista, catalog):
    obra_nacionalidad = []
    nacionalidad = lista [0][0]
    obras = catalog ['artworks']['elements']
    artistas = catalog ['artist']['elements']
    for artista in artistas:
        if (artista['Nationality'] == nacionalidad):
            nombre = artista ['DisplayName']
            ide = artista ['ConstituentID']
            for obra in obras:
                if ide in obra ['ConstituentID']:
                    obra_nacionalidades = [obra['Title'], nombre, obra['Date'], obra['Medium'], obra['Dimensions']]
                    obra_nacionalidad.append (obra_nacionalidades)

    return obra_nacionalidad


def Ordenar_lista (Lista_final):
    lista = []
    frec = []
    for i in Lista_final:
        frec.append (i[1])
        frec.sort ()

    for k in frec:
        for j in Lista_final:
            if j [1] == k:
                if j not in lista:
                    lista.append (j)
    return lista


def l(Name,catalog):
    lista_tecnicas=[]
    lista_ide=[]
    lista_datos_t= []
    contador = 0
    
    for artista in catalog["artist"]["elements"]:
        if Name in  artista["DisplayName"]:
            ide= artista["ConstituentID"]
            lista_ide.append(ide)
    for obra in catalog["artworks"]["elements"]:
        for ide in lista_ide:
            if ide in obra["ConstituentID"]:
                tecnica = obra["Medium"]
                obra= obra["ObjectID"]
                if tecnica not in lista_tecnicas:
                    lista_tecnicas.append(tecnica)
             
                if obra not in lista_datos_t:
                    lista_datos_t.append(obra)
        
    t_tec=len(lista_tecnicas)
    t_dat=len(lista_datos_t)
    respuesta= "Total de tecnicas es: " , t_tec ,"Total de obras es :", t_dat

    return respuesta


# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired(artwork1, artwork2):
    if artwork1["DateAcquired"] < artwork2["DateAcquired"]:
        r = True
    else:
        r = False 
    return r


def cmpA_I(artist1, artist2):
    if artist1["BeginDate"] < artist2["BeginDate"]:
        r = True
    else:
        r = False 
    return r

def Buscar_artistas (artistas, catalog):
    nombres = []
    catalog_2 = catalog ['artist']
    for i in artistas:
        for j in catalog_2 ['ConstituentID']:
            if i == j:
                nombres.append(catalog_2['DisplayName'])
    return nombres

# Funciones de ordenamiento

def ordenamiento_artist_AI(catalog):
    sorted_list = mrgs.sort(catalog['artist'], cmpfunction=cmpA_I)
    return sorted_list   

def ordenamiento_artworks (catalog):
    sorted_list = mrgs.sort(catalog['artworks'], cmpfunction=cmpArtworkByDateAcquired)
    return sorted_list 

