import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import numpy as np

data = pd.read_csv("datlas.csv")


def get_id():
    with open('id.txt', 'r') as f:
        id = f.read().strip()
    return id


def set_id(n):
    with open('id.txt', 'w') as f:
        f.write(n)


def get_image(col):
    labels = list(data[col].value_counts().index)
    values = list(data[col].value_counts())

    plt.figure(figsize=(15, 15))
    plt.bar(labels, values, color="crimson")

    plt.title(f"Frecuencia de choques dependiendo de {col.lower()}")
    plt.xlabel(f"VARIABLE: {col.lower()}")
    plt.ylabel("Frecuencia")
    plt.xticks(rotation=80)

    n = get_id()
    set_id(f"{int(n)+1}")

    plt.savefig(f"static/result{n}.jpg")


def get_map(col):
    gdf = gpd.GeoDataFrame(
        data, geometry=gpd.points_from_xy(data.LONG, data.LAT))

    fig, ax = plt.subplots(figsize=(15, 15))
    street_map = gpd.read_file("maps/camf-nlg.shp")
    street_map.plot(ax=ax, alpha=0.3, color="black")

    values = list(gdf[col].unique())
    colors_r = np.random.randint(0, 255, len(values))
    colors_g = np.random.randint(0, 255, len(values))
    colors_b = np.random.randint(0, 255, len(values))
    c = [(x / 255, y / 255, z / 255) for x, y, z in zip(colors_r, colors_g, colors_b)]

    for i, value in enumerate(values):
        gdf[gdf[col] == value].plot(ax=ax, color=c[i], markersize=3, label=value)

    plt.title(f"Choques sobre el mapa de las carreteras de Nuevo León dependiendo de {col.lower()}")
    lgnd = plt.legend(loc="best", fontsize=10)
    for i in range(len(values)):
        lgnd.legendHandles[1]._sizes = [10]

    n = get_id()
    set_id(f"{int(n)+1}")

    plt.savefig(f"static/result{n}.jpg")


def get_map_m(col):
    gdf = gpd.GeoDataFrame(
        data, geometry=gpd.points_from_xy(data.LONG, data.LAT))

    fig, ax = plt.subplots(figsize=(15, 15))
    street_map = gpd.read_file("maps/camf-nlg.shp")
    street_map.plot(ax=ax, alpha=0.3, color="black")

    values = list(gdf[col].unique())
    colors_r = np.random.randint(0, 255, len(values))
    colors_g = np.random.randint(0, 255, len(values))
    colors_b = np.random.randint(0, 255, len(values))
    c = [(x / 255, y / 255, z / 255) for x, y, z in zip(colors_r, colors_g, colors_b)]

    for i, value in enumerate(values):
        gdf[gdf[col] == value].plot(ax=ax, color=c[i], markersize=3, label=value)

    plt.xlim([-100.5, -100])
    plt.ylim([25.5, 26])

    plt.title(f"Choques sobre el mapa de las carreteras de Monterrey dependiendo de {col.lower()}")
    lgnd = plt.legend(loc="best", fontsize=10)
    for i in range(len(values)):
        lgnd.legendHandles[1]._sizes = [10]

    n = get_id()
    set_id(f"{int(n)+1}")

    plt.savefig(f"static/result{n}.jpg")


def run(variable: str):

    histogram_column_names = {
        "h_hour": "HORA",
        "h_vehicle": "TIPO VEHICULO",
        "h_year": "AÑO",
        "h_month": "MES",
        "h_day_of_week": "DIA",
        "h_damage": "NIVEL DAÑO VEHICULO"
    }

    map_column_names = {
        "mnl_hour": "HORA",
        "mnl_vehicle": "TIPO VEHICULO",
        "mnl_damage": "NIVEL DAÑO VEHICULO",
        "mm_hour": "HORA",
        "mm_vehicle": "TIPO VEHICULO",
        "mm_damage": "NIVEL DAÑO VEHICULO"
    }

    if variable.startswith("h_"):
        col_name = histogram_column_names[variable]
        get_image(col=col_name)
    elif variable.startswith("mnl_"):
        col_name = map_column_names[variable]
        get_map(col=col_name)
    else:
        col_name = map_column_names[variable]
        get_map_m(col=col_name)


def get_probabilidad(day_of_week, weather, mes, ciudad, time):
    _mes = {
        'enero': 0.0906,
        'febrero': 0.0868,
        'marzo': 0.083,
        'abril': 0.07170,
        'mayo': 0.0918,
        'junio': 0.0742,
        'julio': 0.0792,
        'agosto': 0.0868,
        'septiembre': 0.0893,
        'octubre': 0.1132,
        'noviembre': 0.0629,
        'diciembre': 0.0704
    }

    _day_of_week = {
        'lunes': 0.1498,
        'martes': 0.1543,
        'miercoles': 0.1573,
        'jueves': 0.1604,
        'viernes': 0.1558,
        'sabado': 0.1483,
        'domingo': 0.0741
    }

    _weather = {
        'mala_visibilidad': 0.67927,
        'nublado': 0.16036,
        'despejado': 0.16036
    }

    _ciudad = {
        "monterrey": 0.4629,
        "apodaca": 0.0847,
        "garza_garcia": 0.0968,
        "general_escobedo": 0.0469,
        "guadalupe": 0.1362,
        "nicolas_garza": 0.1331,
        "santa_catarina": 0.0393
    }

    _time = {
        "0": 0.0091,
        "1": 0.0091,
        "2": 0.003,
        "3": 0.0061,
        "4": 0.003,
        "5": 0.0045,
        "6": 0.0061,
        "7": 0.0378,
        "8": 0.0666,
        "9": 0.059,
        "10": 0.059,
        "11": 0.0575,
        "12": 0.0772,
        "13": 0.0711,
        "14": 0.0847,
        "15": 0.0469,
        "16": 0.0711,
        "17": 0.0772,
        "18": 0.0847,
        "19": 0.0696,
        "20": 0.0363,
        "21": 0.0363,
        "22": 0.0106,
        "23": 0.0136,
    }

    probability_constant = 0.0000642728578

    probabilidad = _time[time] * _mes[mes] * _ciudad[ciudad] * _day_of_week[day_of_week] * _weather[weather]

    return (probabilidad-probability_constant)/probability_constant




