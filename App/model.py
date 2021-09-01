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


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():

    catalog = {'artist': None,
               'artworks': None,}

    catalog['artist'] = lt.newList('SINGLE_LINKED')
    catalog['artworks'] = lt.newList('SINGLE_LINKED')

    return catalog

# Funciones para agregar informacion al catalogo

def addArtist (catalog, artist):
    art = newArtist(artist['artist_Id'], artist['artist_Name'],
                    artist['artist_Bio'], artist['artist_Nacionality'],
                    artist['artist_Gender'], artist['artist_BeginDate'],
                    artist['artist_EndDate'], artist['artist_WikiQID'], artist['artist_ULAN'])
    lt.addLast(catalog['artist'], art)

def addArtworks (catalog, artworks):
    artw = newArtwork(artworks['artworks_ObjectID'], artworks['artworks_Title'], artworks['artworks_ConstituentID'],
                    artworks['artworks_Date'], artworks['artworks_Medium'], artworks['artworks_Dimensions'],
                    artworks['artworks_CreditLine'], artworks['artworks_AccessionNumber'], artworks['artworks_Classification'],
                    artworks['artworks_Department'], artworks['artworks_DateAcquired'], artworks['artworks_Cataloged'],
                    artworks['artworks_URL'], artworks['artworks_Circumference'], artworks['artworks_Depth'],
                    artworks['artworks_Diameter'], artworks['artworks_Height'], artworks['artworks_Length'],
                    artworks['artworks_Weight'], artworks['artworks_Width'], artworks['artworks_Seat Height'],
                    artworks['artworks_Duration'])
    lt.addLast(catalog['artworks'], artw)			

# Funciones para creacion de datos

def newArtist(Id, Name, Bio, Nacionality, Gender, BeginDate, EndDate, WikiQID, ULAN):
    artist = {'Id': '', 'Name': '', 'Bio': '',
            'Nacionality': '', 'Gender': '', 'BeginDate': '',
            'EndDate': '', 'WikiQID': '', 'ULAN': ''}
    artist['artist_Id'] = Id
    artist['artist_Name'] = Name
    artist['artist_Bio'] = Bio
    artist['artist_Nacionality'] = Nacionality
    artist['artist_Gender'] = Gender
    artist['artist_BeginDate'] = BeginDate
    artist['artist_EndDate'] = EndDate
    artist['artist_WikiQID'] = WikiQID
    artist['artist_ULAN'] = ULAN
    
    return artist

def newArtwork(ObjectID, Title, ConstituentID, Date, Medium, Dimensions, CreditLine, AccessionNumber, Classification,
            Department, DateAcquired, Cataloged, URL, Circumference, Depth, Diameter, Height, Length, Weight, Width,
            SeatHeight, Duration):

    artworks = {'ObjectID': '', 'Title': '', 'ConstituentID': '', 'Date': '',
                'Medium': '', 'Dimensions': '', 'CreditLine': '', 'AccessionNumber': '',
                'Classification': '', 'Department': '', 'DateAcquired': '', 'Cataloged': '',
                'URL': '', 'Circumference': '', 'Depth': '', 'Diameter': '', 'Height': '',
                'Length': '', 'Weight': '', 'Width': '', 'SeatHeight': '', 'Duration': ''}
    artworks['artworks_ObjectID'] = ObjectID
    artworks['artworks_Title'] = Title
    artworks['artworks_ConstituentID'] = ConstituentID
    artworks['artworks_Date'] = Date
    artworks['artworks_Medium'] = Medium
    artworks['artworks_Dimensions'] = Dimensions
    artworks['artworks_CreditLine'] = CreditLine
    artworks['artworks_AccessionNumber'] = AccessionNumber
    artworks['artworks_Classification'] = Classification
    artworks['artworks_Department'] = Department
    artworks['artworks_DateAcquired'] = DateAcquired
    artworks['artworks_Cataloged'] = Cataloged
    artworks['artworks_URL'] = URL
    artworks['artworks_Circumference'] =  Circumference
    artworks['artworks_Depth'] = Depth
    artworks['artworks_Diameter'] = Diameter
    artworks['artworks_Height'] = Height
    artworks['artworks_Length'] = Length 
    artworks['artworks_Weight'] = Weight
    artworks['artworks_Width'] = Width
    artworks['artworks_Seat Height'] = SeatHeight
    artworks['artworks_Duration'] = Duration
    
    return artworks

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento