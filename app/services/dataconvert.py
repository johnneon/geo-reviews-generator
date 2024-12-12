import joblib

import numpy as np
import os
import pandas as pd
#from sklearn import cluster

from geopy.geocoders import ArcGIS #Подключаем библиотеку
# для геокодирования используем ArcGIS

#from app.services.getroute import get_route
#from app.ml.data_preprocessing import get_haversine_distance # Функция определения расстояние Хаверсина



def dataconvert(data):
    """ Converting data into a dataset for prediction """

    geolocator = ArcGIS()
    
    # начинаем формировать датафрейм исходных данных

    rubrics = str(data.get('rubrics'))
    name_org = str(data.get('name_org'))
    # Получаем координаты (признак)
    org_address = str(data.get('org_address'))
    #org_address = org_address + ", Россия"
    org_coordinates = geolocator.geocode(org_address)
    rating = int(data.get('rating'))
    

    # возвращаем подготовленные данные для предсказания    
    return rubrics, name_org, org_address, org_coordinates, rating