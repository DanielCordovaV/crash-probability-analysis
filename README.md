# Plataforma interactiva  de consulta de accidentes viales en Monterrey - Alpha Tauri


[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Generic badge](https://img.shields.io/badge/HackMTY-Datlas%20Winner-green.svg)](https://hackmty.com/)
[![Plataforma](https://img.shields.io/badge/link-website-blue.svg)](https://hackmty-alpha-tauri.herokuapp.com/)
[![Version](https://img.shields.io/badge/version-v1.0-red.svg)](https://hackmty-alpha-tauri.herokuapp.com/)

## Autores
* [Daniel Cordova](https://github.com/DanielCordovaV) 
* [Pablo Blanco](https://github.com/pablo-blancoc)
* José Vázquez 
* [Oswaldo Hernández](https://github.com/OSWA00) 

## Resumen ejecutivo:
![alt text](https://github.com/DanielCordovaV/crash-probability-time-series-analysis/blob/master/images/01.png)
**“En Nuevo León se registran más del 20 por ciento de los accidentes [viales] que se reportan a nivel nacional.” - El Financiero**

Contamos con una basta cantidad de datos sobre accidentes automovilísticos; mismos que necesitan transformarse en información accionable que pueda ser utilizada por los diferentes actores clave del sistema, para así llevar a cabo una toma de decisiones efectiva que minimice el costo humano y económico, inherentes a dichas eventualidades. 

Nuestro objetivo es crear una plataforma de fácil consulta, con información procesada y lista para su interpretación. Promoviendo la toma de decisiones informada para mejorar la planificación urbana y optimizar los servicios de respuesta como ajustadores y rescatistas. Buscando generar un impacto en la eficiencia vial y en la reducción de fatalidades. 

Variable | Tipo | Detalles
------------ | ------------- | -------------
Año | Discreta | De 2016 al segundo trimestre de 2018
Día de la semana | Nominal | Rango de lunes a domingo
Hora | Discreta | Horas enteras en formato de 24 hrs.
Longitud | Continua | En el rango de -100.5 a -100.0
Latitud | Continua | En el rango de 25.5 a 26.0
Severidad de accidente | Nominal | Clasificada en: sin daño/ daño bajo / medio y alto.
Clima | Nominal | Abarcando: día despejado, nublado y mala visibilidad por clima (lluvia, tormenta, nieve y neblina)
Tipo de vehículo | Nominal | Comprendiendo el automóvil particular, camión ligero y camión. 

## Visualizando el conjunto de datos
Para que la información pueda generar un alto impacto debe haber una buena estrategia de datos que la sustente. Con ello en mente, utilizamos la base de datos proporcionada por DATLAS en combinación con datos meteorológicos de OpenWeather.org. Procesadas con diferentes herramientas como Pandas, Keras y análisis estadístico. 

Además, una correcta visualización de datos facilita la comprensión de los mismos, lo que aumenta la influencia de dicha información en la toma de decisiones. Por lo que decidimos usar el framework de Python Flask para montar la plataforma de consulta y Tableau para la visualización de datos.
![alt text](https://github.com/DanielCordovaV/crash-probability-time-series-analysis/blob/master/images/02.png)

### 1. Calculadora de cambio en esperanza de choque:
Para el desarrollo del cálculo de la esperanza de un choque, se obtuvo la probabilidad de las variables independientes: Hora, Día de la semana, Clima, Ciudad aproximada y Mes. Además, se obtuvo una constante de comparación al sumar los promedios de probabilidad de cada variable. Por último se obtiene el cambio en la esperanza de acuerdo al cumplimiento de condiciones, bajo las siguientes fórmulas:

__Esperanza = P1(Ciudad)*P2(Mes)*P3(Día)*P4(Hora)*P5(Clima)
Cambio = (Esperanza - Constante)/Constante__

### 2. Red Neuronal
Para calcular la probabilidad de accidente en ubicaciones más específicas, se utiliza una regresión realizada con una red neuronal profunda mediante Keras. Misma que calcula la distribución de probabilidad de choque en 25 cuadrantes que cubren la superficie de Monterrey y área metropolitana. Dicha red es alimentada con una muestra de los datos proporcionados por DATLAS y OpenWeather.org, reservando una parte de los datos para su validación. 

### 3. Heatmap de Choques
Se realizó la limpieza de datos con Python, mediante la librería Pandas. Para facilitar la visualización de los datos se tomó una muestra de 661 casos, para obtener un nivel de confianza del 99% con un margen de error del 5%. Posteriormente, se utilizaron las coordenadas individuales para georeferenciar los incidentes reportados en Monterrey y su área metropolitana, obteniendo las áreas geográficas de mayor concentración de accidentes. 
![alt text](https://github.com/DanielCordovaV/crash-probability-time-series-analysis/blob/master/images/03.png)


### 4. Frecuencia de accidentes por día y hora:
Para determinar los días y horarios con más incidentes reportados, se utilizó el dataset proporcionado por DATLAS, mismo que se limpió con Python. Posteriormente se cargó en Tableau para poder obtener el conteo de los casos en las variables cruzadas de Día y Hora. 
Monterrey y su área metropolitana, obteniendo las áreas geográficas de mayor concentración de accidentes. 
![alt text](https://github.com/DanielCordovaV/crash-probability-time-series-analysis/blob/master/images/04.png)

### 5. Choques georeferenciados y clasificados por nivel de daño:
Se utilizó el dataset previamente depurado,  en este caso georeferenciando los casos por su clasificación de nivel de daño. Misma que puede ser daño bajo, medio o alto. Cabe resaltar que los datos fueron filtrados para las ciudades de Monterrey, Apodaca, General Escobedo, Guadalupe, San Nicolás de los Garza, Garza García y Santa Catarina. 
![alt text](https://github.com/DanielCordovaV/crash-probability-time-series-analysis/blob/master/images/05.png)


### 6. Tipos de vehículos involucrados en los accidentes:
Comprendiendo que proporcionalmente es mucho mayor el número de automóviles particulares frente al de camiones de carga ligera y pesada, se decide obtener la visualización de la georreferenciación de los accidentes en Tableau. A fin de identificar los lugares de mayor incidencia de acuerdo al tipo de vehículo. 
![alt text](https://github.com/DanielCordovaV/crash-probability-time-series-analysis/blob/master/images/06.png)

## Conclusiones
Los principales actores clave considerados en este proyecto: gobierno, aseguradores y equipos de respuesta. Podrán verse beneficiados al comprender que la mayor probabilidad de colisiones se da en Monterrey; para así reducir costos y tiempos de transportación. También podrán optimizar las rondas de patrullaje, considerando que en especial los días lunes, martes y viernes de 18:00 a 20:00 hrs, han mostrado ser los momentos con mayores colisiones. 

El despliegue de las fuerzas de tránsito y de respuesta, puede volverse más eficiente al  comprender los aumentos de probabilidad de choque de acuerdo a la zona y las condiciones climatológicas. Ya que más del 67% de los casos mostraron ocurrir con condiciones de mala visibilidad atribuidos al clima. 

Por último, se puede validar que el tipo de accidente de acuerdo al vehículo tiene variaciones en las geografías donde ocurren. Lo que puede ayudar a las aseguradoras a destinar ajustadores especializados en las colisiones de camiones en los puntos de mayor incidencia. Así como apoyar al gobierno a tomar medidas de optimización vial para reducir el número de casos. 


