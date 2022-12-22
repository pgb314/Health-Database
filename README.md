# Health-Database
## CONTENIDO 📑
[1 - Objetivo 🎯](#O)<br />
[2 - Extracción, Transformación y Carga ⚙](#ETL) <br />
[3 - Feature Importances🔝](#FI)<br />
[4 - Machine Learning 🤖 ](#ML)<br />
[5 - Streamlit📡 ](#SL)<br />
 
## 1 - OBJETIVO 🎯<a name="O"/>   
#### -Usar todas las herramientas necesarias de extracion y limpieza de datos mas intentar automatizar el proceso de aprendizaje supervisado de los modelos:<br />
#### -Construir un modelo de machine learning capaz de predecir una variable medica con la ayuda de una base de datos de informacion medica por año y pais.<br />
#### -Construir una pagina streamlit que contenga toda la informacion necesaria para ilustrar las relaciones entre las variables.<br />





## 2 - EXTRACCIÓN, TRANSFORMACIÓN Y CARGA ⚙️ <a name="ETL"/>
### Obtenemos datos de cuatro fuentes utilizando 4 métodos de extracción.
1. Descargamos un csv desde Kaggle https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who este archivo contiene la base de nuestros datos, vamos suplementandolos
2. Usamos Beautiful Soup para scrapping de http://www.geoba.se/population.php para conseguir datos de poblacion y creamos a traves de esos datos metricas per capita de nuestros datos originales
3. De Wikipedia sacamos con el Instant Data Scrapper el Producto Interior Bruto de cada pais por año y se lo añadimos a nuestra base de datos
4. Hacemos una API desde la OMS https://www.who.int/data/gho/info/gho-odata-api , contiene mas de 2000 columnas, mas adelante tendremos que separar las columnas viables para conseguir algo que se asemeje a una base de datos utilizable.
5. Por ultimo añadimos metricas de edad media descargandonos un csv desde la pagina del Banco Mundial https://databank.worldbank.org/source/health-nutrition-and-population-statistics#
### Limpiamos y selecionamos los datos relevantes
1. Rellenamos Nulos con informacion  extraida del internet, donde no sea posible borramos registros
2. Inicialmente no discriminamos con los datos proporcionados por nuestra API, una vez ha sido creada la base de datos entera vamos borrando columnas que no tengan suficientes registros representativos dado a que evitamos a toda costa quitar filas.
3. Al unir datos de nuestra API existen muchos indicadores con mediciones cada 5 o 3 años. Para evitar borrar columnas que puedan resultar interesantes para nuestros modelos creamos medias de los años con puntos de datos existentes y rellenamos con esas medias los datos que se encuentren entre esos años.
4. Igualmente con las edades medias, con la ayuda de un poco de investigacion rellenamos los puntos que faltan
5. Con la ayuda de el factor de inflacion de la varianza analizamos nuestra base de datos conjunta y nos quedamos con aquellas columnas que no tengan multicollinearidad con 5 umbrales distintos de certeza
6. Guardamos nuestra base de datos

## 3 - FEATURE IMPORTANCES🔝 <a name="CH"/>
1. Elegimos 5 Variables a predecir distintas y para cada una de ellas elegimos los 5 factores con mas peso en esa variables. Partimos de el analisis VIF(factor de inflacion de la varianza) con un umbral de 5. Eso nos da 38 columnas con factores no multicollineares. Para cada predicion descartamos 32 columnas.
2. Ya que decidimos en un numero fijo de 5 factores no tenemos un umbral fijo del peso relativo con el que descartar


## 4 - MACHINE LEARNING 🤖 <a name="ML"/>
1. Para Cada unas de nuestras variables a predecir creamos un dataframe con las columnas predictivas y el valor a predecir.
2. Buscamos de una forma automatizada los mejores modelos para cada una de nuestros dataframes y guardamos el mejor modelo para cada factor en un archivo pickle, con eso podemos hacer prediciones en vivo con el input del usuario de la pagina streamlit.

## 5 - STREAMLIT 📡 <a name="SL"/>
#### Contruimos la estructura de la pagina en la que incluimos: La base de datos entera construida, Una pagina para cada factor a predecir , con un selector para cada variable que consideramos en nuestra feature selection como relevante. Por ultimo presentamos una conclusion

## CONTENT 📑
[1 - Objective 🎯](#O)<br />
[2 - Extraction, Transformation and Loading ⚙](#ETL) <br />
[3 - Feature Importances🔝](#FI)<br />
[4 - Machine Learning 🤖 ](#ML)<br />
[5 - Streamlit📡 ](#SL)<br />
 
## 1 - OBJECTIVE 🎯<a name="O"/>   
#### -Use all the necessary data extraction and cleaning tools plus attempt to automate the supervised learning process of the models.:<br />
#### -Build a machine learning model capable of predicting a medical variable with the help of a database of medical information by year and country..<br />
#### -Build a streamlit page containing all the information necessary to illustrate the relationships between variables..<br />





## 2 - EXTRACTION, TRANSFORMATION AND LOADING ⚙️ <a name="ETL"/>
### We obtain our Data from 5 different sources using 4 different extraction methods.
1. Downloading a CSV from Kaggle https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who this contains the framework of our Database
2. We use Beautiful Soup for scraping http://www.geoba.se/population.php to get population data and create per capita metrics from that data for our original data.
3. From Wikipedia we extract with the Instant Data Scrapper the Gross Domestic Product of each country per year and add it to our database.
4. We make an API from the WHO https://www.who.int/data/gho/info/gho-odata-api , it contains more than 2000 columns, later we will have to separate the viable columns to get something that resembles a usable database.
5. Lastly, we add average age metrics by downloading a csv from the World Bank website https://databank.worldbank.org/source/health-nutrition-and-population-statistics#.
### Cleaning and selecting relevant data
1. We fill in Nulls with information extracted from the internet, where not possible we delete records
2. Initially we do not discriminate with the data provided by our API, once the entire database has been created we delete columns that do not have enough representative records since we avoid removing rows at all costs.
3. When merging data from our API there are many indicators with measurements every 5 or 3 years. To avoid deleting columns that may be interesting for our models we create averages of the years with existing data points and fill in with those averages the data between those years.
4. Likewise with the average ages, with the help of a little research we fill in the missing items
5. With the help of the variance inflation factor we analyze our joint database and keep those columns that do not have multicollinearity with 5 different thresholds of certainty.
6. We save our database

## 3 - FEATURE IMPORTANCES🔝 <a name="CH"/>
1. We choose 5 different variables to predict and for each of them we choose the 5 factors with the most weight in that variable. We start from the VIF (variance inflation factor) analysis with a threshold of 5. This gives us 38 columns with non-multicollinear factors. For each prediction we discard 32 columns.
2. Since we decide on a fixed number of 5 factors we do not have a fixed threshold of relative weight with which to rule out


## 4 - MACHINE LEARNING 🤖 <a name="ML"/>
1. For each of our variables to be predicted we create a dataframe with the predicted columns and the value to be predicted.
2. We search in an automated way for the best models for each of our dataframes and save the best model for each factor in a pickle file, with that we can do live preditions with the user input from the streamlit page.

## 5 - STREAMLIT 📡 <a name="SL"/>
#### We build the structure of the page in which we include: The entire database built, a page for each factor to predict, with a selector for each variable that we consider in our feature selection as relevant. Finally we present a conclusion
