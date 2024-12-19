# Team №5 - geo-reviews-generator
Проектный практикум - учебная задача. Нейронная сеть, способная генерировать текстовые отзывы о различных местах на основе определенных входных параметров, таких как категория места, средний рейтинг и ключевые слова.

Данные: https://github.com/yandex/geo-reviews-dataset-2023

## Структура проекта

### ML

В [geo-reviews-generation.ipynb](./geo-reviews-generation.ipynb) находится весь код связанный с ML, загрузка датасета, исследование и предобработка, обучение модели и ее улучшения.

### Приложение

В `app` расположился код прототипа нашего приложения для демонстрации работы модели.
Приложение состоит из двух частей:
- Оболочка пользователя реализованная на streamlit;
- Непосредственно сервис генерации отзывов реализованный на FastAPI.

#### Запуск приложения:

После загрузки исходных файлов в диерктории проекта:
1) Скачиваем итоговую модель 
https://drive.google.com/file/d/1sLzZBLG1ATn-MkDAsJiJLvR37viLvgtq/view?usp=drive_link
2) Расспаковываем в каталог ./model
Итоговый путь к файлам модели должен выглядеть ./model/train-model-2/
3) Подготавливаем среду 
````bash
# Создание виртуального окружения
python -m venv env

# Активация виртуального окружения в Linux
source env/bin/activate

# Активация виртуального окружения в Windows
env\Scripts\activate.bat

# Устанавливаем библиотеки
pip install -r requirements.txt

# Устанавливаем локальные пакеты
pip install -e .
````

4) Отдельно устанавливаем PyThorch.

Комманду для установки на Вашу ОС и аппаратную конфигурацию можно уточнить на сайте PyThorch
https://pytorch.org/get-started/locally/

5) Переходим в каталог приложения
````bash
cd app
````

6) Запускаем uvicorn сервер:  

````bash
uvicorn app.main:app
````
Данный сервер доступен по адресу 127.0.0.1:8000 
Обрабатывает post запросы на http://127.0.0.1:8000/generation следующей структуры:

````
    rubrics: str # тип организации (магазин, кафе, гостиница...)
    name_org: str # название организации
    org_address: str # адрес организации
    rating: int # оценка организации (от 1 до 5)    
````
Ответ содержит:

````
    'result': str # сгенерированный отзыв
    'latitude': int # географические широта и
    'longitude': int # долгота организации
````
7) Запускаем streamlit сервер реализующий web-интерфейс 

````bash
streamlit run apps.py
````

### Документация

Директория `docs` хранит в себе документацию и презентацию.
Так же там можно найти наш [план работы](./docs/README.md).


## Команда:
1) Ilyin V.B. (https://github.com/Viktor-125142)
2) Kravtsov A.V. (https://github.com/Baddogel)
3) Efimovich E.A. (https://github.com/johnneon)
4) Kryuchkov V.V. (https://github.com/Tifles)
5) Chashnikov S.Yu. (https://github.com/SergeyChashnikov)
6) Salov A.S. (https://github.com/TonyStranger404)
