import json
import requests
import streamlit as st
import pandas as pd
import folium
import streamlit.components.v1 as components

# Import folium MarkerCluster plugin
from folium.plugins import MarkerCluster
# Import folium MousePosition plugin
from folium.plugins import MousePosition
# Import folium DivIcon plugin
from folium.features import DivIcon

def serialize_datetime(obj): 
    if isinstance(obj, datetime.datetime): 
        return obj.isoformat() 
    raise TypeError("Type not serializable") 

# Заголок
st.title('Генератор обзоров для организаций')

# Запрашиваем исходные данные

# Тип организации
rubrics = st.text_input(
    "Введите тип организации",
    value = "Кафе"
    )

#Название организации
name_org = st.text_input(
    "Введите название организации 👇",
    value = "Плакучая ива", 
    )

# Адрес организации
org_address = st.text_input(
    "Введите адрес организации 👇",
    value = "г. Сочи, ул. Войкова, 3", 
    )

# Оценка заведения
rating  = st.slider(
    "Выберите оценку организации (от 1 до 5) 👇",
    1,5,1
    )

if (st.button('Сгенерировать отзыв')):
    res = {
            'rubrics': rubrics,
            'name_org': name_org,
            'org_address':org_address,
            'rating': rating
            }
    # отправляем данные, получаем отзыв
    requestpost = requests.post(url="http://127.0.0.1:8000/generation", data=json.dumps(res))
    response_data = requestpost.json()
    
    generation_result = response_data['result']
    latitude = response_data['latitude']
    longitude = response_data['longitude']    
    st.write("Ваш отзыв:")
    st.write(generation_result)
    # Наносим на карту
    
    # Создаём карту
    Maps = folium.Map(
        location = [latitude, longitude],    # широта и долгота организации
        zoom_start = 15
        )                    

    # Сохдаём маркеры точек
    org_point = folium.Marker(
                        [latitude,longitude],
                        popup = (name_org),
                        icon=folium.Icon(color='green',icon='ok-sign')
                        ).add_to(Maps)

    
    components.html(folium.Figure().add_child(Maps).render(), height=500) 