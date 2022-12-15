  



import streamlit as st
import pandas as pd
import numpy as np
import pickle  #to load a saved model
import base64

import seaborn as sns
import matplotlib.pyplot as plt
import base64
import plotly.express as px
import webbrowser


@st.cache(suppress_st_warning=True)
def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://github.com/Barge7/PROYECTO-FINAL/blob/main/imagenes/fondosivia70.png?raw=true");
            background-attachment: fixed;
            background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
            )
add_bg_from_url()



def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value
app_mode = st.sidebar.selectbox('Select Disease',['Home','Data','Adolescent birth rate (per1000)','Total NCD Deaths (in thousands)','Homicide rates (per 100 000)','Suicide rates (per 100 000)','Prevalence Hypertension among adults'])
 
   
   

if app_mode == 'Home':
    def add_bg_from_url():
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://github.com/Barge7/PROYECTO-FINAL/blob/main/imagenes/fondosivia70.png?raw=true");
            background-attachment: fixed;
            background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
            )
    add_bg_from_url()
    
    
    
    st.header('Home')
    url = "https://app.powerbi.com/view?r=eyJrIjoiZGQ0YjliNDItNmRkOC00ZTdiLThlYzgtZjFjNDJjMWM1ZWM5IiwidCI6IjdmM2ZjMzNmLTk5OTAtNGQ4MC05ZGNmLTZhNzE2Yzk2ZTQxNiIsImMiOjl9"
    st.sidebar.header("Select Disease or view Data")
    file_ = open("impatiently-waiting-gif-4.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.sidebar.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True)
    st.markdown("#### Project Goal:")
    
    st.markdown("##### This Project attempts to build a database with factors that influence disease outcomes, and the frequency of the diseases. With the help of a machine learning algorithms the factors are ranked and the user can modify each input and get a predictive value for the chosen disease")
    

    if st.button('PowerBi'):
        webbrowser.open_new_tab(url)
    st.markdown("#### Sources: ")
    st.markdown("##### https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who")
    st.markdown("##### https://databank.worldbank.org/source/health-nutrition-and-population-statistics#")
    st.markdown("##### https://ghoapi.azureedge.net/api/Indicator")
    st.markdown("##### http://www.geoba.se/population.php")
    
    
    







elif app_mode == 'Data' :
    df = pd.read_csv('clean_full_data.csv')
    def add_bg_from_url():
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://github.com/Barge7/PROYECTO-FINAL/blob/main/imagenes/fondosivia70.png?raw=true");
            background-attachment: fixed;
            background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
            )
    add_bg_from_url()
    st.caption('# Full Data:')


    filtros, countries= st.columns(2)

    with filtros:
        columnas = df.columns
        selection = st.multiselect('Filtrar Columnas', columnas, default=[ 'country','year','Malaria', 'average_age'])

    with countries:
        pais = st.selectbox('Filtrar Paises', df.country.unique())
    

    

    df1 = df[selection]

    var = df1[df1.country== pais]

    st.dataframe(var)

   





elif app_mode =='Adolescent birth rate (per1000)':
    def add_bg_from_url():
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://github.com/Barge7/PROYECTO-FINAL/blob/main/imagenes/fondosivia70.png?raw=true");
            background-attachment: fixed;
            background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
            )
    add_bg_from_url()
    

    st.header("This app will predict a desired Medical value with its corresponding variables")
    st.image('Adolescent_Pregnant.jpg')
    st.sidebar.header("Predictive Factors :")
    vio_dict = {1:-0.337,2:-0.329,3:-0.32,4:-0.20,5:-0.12,6:0.2,7:0.4,8:1.4,9:2.82,10:4.8}
    hep_dict = {1:-0.1535,2:-0.153,3:-0.151,4:-0.149,5:-0.148,6:-0.12,7:-0.11,8:0.1,9:0.5,10:1.4}
    mala_dict = {1:-0.397089,2:-0.397,3:-0.39,4:-0.34,5:-0.3,6:-0.2,7:1.1,8:2.3,9:3.8,10:6.567}
    hiv_dict = {1:-0.37286,2:-0.37,3:-0.359,4:-0.35,5:-0.34,6:-0.25,7:-0.2,8:-0.17,9:1.5,10:8.86}
    gdp_dict = {1:-0.661,2:-0.63,3:-0.56,4:-0.5,5:-0.437,6:-0.28,7:-0.2,8:1.55,9:3.75,10:6.2497}
    Violence=st.sidebar.slider('Violence',1,10,1)
    Hepatitis=st.sidebar.slider('Hepatitis',1,10,1)
    Malaria=st.sidebar.slider('Malaria',1,10,1)
    HIV=st.sidebar.slider('HIV',1,10,1)
    gdp=st.sidebar.slider('gdp',1,10,1)

 
   
   
   
    
    

    feature_list=  [get_value(Violence,vio_dict),get_value(Hepatitis,hep_dict),get_value(Malaria,mala_dict),get_value(HIV,hiv_dict),get_value(gdp,gdp_dict)]

    single_sample = np.array(feature_list).reshape(1,-1)

    if st.button("Predict"):
   
        loaded_model = pickle.load(open('model_Adolescent birth rate (per 1000 women aged 15-19 years).pkl', 'rb'))
        prediction = loaded_model.predict(single_sample)
        formatted_string = "{:.2f}".format(prediction[0])
        float_value = float(formatted_string)
        st.metric(label="Adolescent birth rate per 1000 women", value=float_value)
        
    if st.button("Correlations"):   
        df = pd.read_csv('clean_full_data.csv')    
        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["Interpersonal Violence"], y = df["Adolescent birth rate (per 1000 women aged 15-19 years)"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('Adolescent birth rate  vs. Interpersonal Violence')
        st.pyplot(fig)
        
        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["Acute Hepatitis"], y = df["Adolescent birth rate (per 1000 women aged 15-19 years)"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('Adolescent birth rate  vs. Acute Hepatitis')
        st.pyplot(fig)

        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["per_capita-Malaria"], y = df["Adolescent birth rate (per 1000 women aged 15-19 years)"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('Adolescent birth rate  vs. Per capita Malaria rates')
        st.pyplot(fig)

        
        
        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["per_capita-HIV/AIDS"], y = df["Adolescent birth rate (per 1000 women aged 15-19 years)"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('Adolescent birth rate  vs. Per capita HIV rates')
        st.pyplot(fig)

        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["gdp/percap"], y = df["Adolescent birth rate (per 1000 women aged 15-19 years)"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('Adolescent birth rate  vs. GDP per capita')
        st.pyplot(fig)
    if st.button("World Map"):
        st.image('Adolescent.png')

            



elif app_mode =='Total NCD Deaths (in thousands)':
    def add_bg_from_url():
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://github.com/Barge7/PROYECTO-FINAL/blob/main/imagenes/fondosivia70.png?raw=true");
            background-attachment: fixed;
            background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
            )
    add_bg_from_url()
    

    
    st.header("This app will predict a desired Medical value with its corresponding variables")
    st.image('NCD_deaths.jpg')
    st.sidebar.header("Predictive Factors :")
    drug_dict = {1:-0.1742,2:-0.173,3:-0.17,4:-0.166,5:-0.1616,6:-0.145,7:-0.13,8:-0.11,9:0.5,10:1.87}
    viop_dict = {1:-0.6943,2:-0.63,3:-0.53,4:-0.44,5:-0.351,6:-0.12,7:0.05,8:0.16,9:4.1,10:8.7}
    cirr_dict = {1:-1.3939,2:-0.82,3:-0.51,4:-0.33,5:-0.127,6:0.05,7:0.15,8:0.55,9:3.8,10:6.83}
    traff_dict = {1:-1.43,2:-1.03,3:-0.66,4:-0.42,5:-0.217,6:0.05,7:0.35,8:0.82,9:1.75,10:4.06}
    Drugs=st.sidebar.slider('Drugs',1,10,1)
    Violence=st.sidebar.slider('Violence',1,10,1)
    Cirrhosis=st.sidebar.slider('Cirrhosis',1,10,1)
    NCD=st.sidebar.slider('NCD',8000,80000,100)
    Traffic=st.sidebar.slider('Traffic',1,10,1)

    
   
   

    feature_list=[get_value(Drugs,drug_dict),get_value(Violence,viop_dict),get_value(Cirrhosis,cirr_dict),NCD,get_value(Traffic,traff_dict)]

    single_sample = np.array(feature_list).reshape(1,-1)

    if st.button("Predict"):
        loaded_model = pickle.load(open('model_Total NCD Deaths (in thousands).pkl', 'rb'))
        prediction = loaded_model.predict(single_sample)
        formatted_string = "{:.2f}".format(prediction[0])
        float_value = float(formatted_string)
        st.metric(label="Total NCD Deaths in thousands", value=float_value)

        
    if st.button("Correlations"):   
        df = pd.read_csv('clean_full_data.csv')     
        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["Drug Use Disorders"], y = df["Total NCD Deaths (in thousands)"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('NCD Deaths  vs. Drug Use Disorders')
        st.pyplot(fig)
        
        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["per_capita-Interpersonal Violence"], y = df["Total NCD Deaths (in thousands)"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('NCD Deaths  vs. per capita Interpersonal Violence')
        st.pyplot(fig)

        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["per_capita-Cirrhosis and Other Chronic Liver Diseases"], y = df["Total NCD Deaths (in thousands)"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('NCD Deaths  vs. Per capita Cirrhosis and Other Chronic Liver Diseases')
        st.pyplot(fig)
        
        
        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["Crude suicide rates (per 100 000 population)"], y = df["Total NCD Deaths (in thousands)"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('NCD Deaths  vs. Suicide rates (per 100 000)')
        st.pyplot(fig)

    if st.button("World Map"):
        st.image('NCD.png')    
        
        
elif app_mode =='Homicide rates (per 100 000)':
    def add_bg_from_url():
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://github.com/Barge7/PROYECTO-FINAL/blob/main/imagenes/fondosivia70.png?raw=true");
            background-attachment: fixed;
            background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
            )
    add_bg_from_url()
    

    
    st.header("This app will predict a desired Medical value with its corresponding variables")
    st.image('homicide.jpg')
    st.sidebar.header("Predictive Factors :")
    viop_dict = {1:-0.6943,2:-0.63,3:-0.53,4:-0.44,5:-0.351,6:-0.12,7:0.05,8:0.16,9:4.1,10:8.7}
    alco_dict = {1:-0.5994,2:-0.53,3:-0.47,4:-0.44,5:-0.413,6:-0.21,7:0.01,8:0.1,9:3.5,10:7.1}
    prot_dict = {1:-0.545,2:-0.535,3:-0.51,4:-0.45,5:-0.3980,6:-0.21,7:-0.06,8:0.69,9:4.1,10:8.1}
    cirr_dict = {1:-1.3939,2:-0.82,3:-0.51,4:-0.33,5:-0.127,6:0.05,7:0.15,8:0.55,9:3.8,10:6.83}
    traff_dict = {1:-1.43,2:-1.03,3:-0.66,4:-0.42,5:-0.217,6:0.05,7:0.35,8:0.82,9:1.75,10:4.06}
    Violence=st.sidebar.slider('Violence',1,10,1)
    Alcohol=st.sidebar.slider('Alcohol',1,10,1)
    Protein=st.sidebar.slider('Protein',1,10,1)
    Cirrhosis=st.sidebar.slider('Cirrhosis',1,10,1)
    Traffic=st.sidebar.slider('Traffic',1,10,1)

    
   
   
    

    feature_list=[get_value(Violence,viop_dict),get_value(Alcohol,alco_dict),get_value(Protein,prot_dict),get_value(Cirrhosis,cirr_dict),get_value(Traffic,traff_dict)]

    single_sample = np.array(feature_list).reshape(1,-1)

    if st.button("Predict"):
        
        
   
        loaded_model = pickle.load(open('model_Estimates of rates of homicides per 100 000 population.pkl', 'rb'))
        prediction = loaded_model.predict(single_sample)
        formatted_string = "{:.2f}".format(prediction[0])
        float_value = float(formatted_string)
        st.metric(label="Homicide rates per 100 000", value=float_value)
        
    if st.button("Correlations"):   
        df = pd.read_csv('clean_full_data.csv')
        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["per_capita-Interpersonal Violence"], y = df["Estimates of rates of homicides per 100 000 population"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('Homicides rates (per 100 000)  vs. Interpersonal Violence')
        st.pyplot(fig)
        
        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["per_capita-Alcohol Use Disorders"], y = df["Estimates of rates of homicides per 100 000 population"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('Homicides rates (per 100 000)  vs. per capita Alcohol Use Disorders')
        st.pyplot(fig)

        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["per_capita-Protein-Energy Malnutrition"], y = df["Estimates of rates of homicides per 100 000 population"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('Homicides rates (per 100 000)  vs. Per capita Protein Malnutrition')
        st.pyplot(fig)
        
        
        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["per_capita-Cirrhosis and Other Chronic Liver Diseases"], y = df["Estimates of rates of homicides per 100 000 population"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('Homicides rates (per 100 000)  vs. Per capita Cirrhosis and other Liver Diseases')
        st.pyplot(fig)

        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["Estimated road traffic death rate (per 100 000 population)"], y = df["Estimates of rates of homicides per 100 000 population"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('Homicides rates (per 100 000)  vs. Road Traffic death rate (per 100 000)')
        st.pyplot(fig)
        
    if st.button("World Map"):
        st.image('Homicides.png')        
            
elif app_mode =='Suicide rates (per 100 000)':
    def add_bg_from_url():
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://github.com/Barge7/PROYECTO-FINAL/blob/main/imagenes/fondosivia70.png?raw=true");
            background-attachment: fixed;
            background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
            )
    add_bg_from_url()
    

    
    st.header("This app will predict a desired Medical value with its corresponding variables")
    st.image('suicide.jpg')
    st.sidebar.header("Predictive Factors :")
    viop_dict = {1:-0.6943,2:-0.63,3:-0.53,4:-0.44,5:-0.351,6:-0.12,7:0.05,8:0.16,9:4.1,10:8.7}
    hiv_dict = {1:-0.37286,2:-0.37,3:-0.359,4:-0.35,5:-0.34,6:-0.25,7:-0.2,8:-0.17,9:1.5,10:8.86}
    cold_dict = {1:-0.454,2:-0.415,3:-0.395,4:-0.34,5:-0.29,6:-0.23,7:-0.18,8:-0.02,9:4.4,10:8.47}
    road_dict = {1:-1.31,2:-0.92,3:-0.41,4:-0.28,5:-0.16,6:0.01,7:0.15,8:0.52,9:2.8,10:5.28}
    pois_dict = {1:-0.82,2:-0.69,3:-0.601,4:-0.52,5:-0.432,6:-0.21,7:0.1,8:0.84,9:4.2,10:8.5}
    Violence=st.sidebar.slider('Violence',1,10,1)
    HIV=st.sidebar.slider('HIV',1,10,1)
    Environmental=st.sidebar.slider('Environmental',1,10,1)
    Road=st.sidebar.slider('Road',1,10,1)
    Poisoning=st.sidebar.slider('Poisoning',1,10,1)

    
   
   
    

    feature_list=[get_value(Violence,viop_dict),get_value(HIV,hiv_dict),get_value(Environmental,cold_dict),get_value(Road,road_dict),get_value(Poisoning,pois_dict)]

    single_sample = np.array(feature_list).reshape(1,-1)

    if st.button("Predict"):
        
        loaded_model = pickle.load(open('model_Age-standardized suicide rates (per 100 000 population).pkl', 'rb'))
        prediction = loaded_model.predict(single_sample)
        formatted_string = "{:.2f}".format(prediction[0])
        float_value = float(formatted_string)
        
        st.metric(label="Suicide rates per 100 000", value=float_value)
        
    if st.button("Correlations"):
        df = pd.read_csv('clean_full_data.csv')
        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["per_capita-Interpersonal Violence"], y = df["Age-standardized suicide rates (per 100 000 population)"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('Suicide rates (per 100 000)  vs. per capita Interpersonal Violence')
        st.pyplot(fig)
        
        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["per_capita-HIV/AIDS"], y = df["Age-standardized suicide rates (per 100 000 population)"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('Suicide rates (per 100 000)  vs. per capita HIV/AIDS')
        st.pyplot(fig)

        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["per_capita-Environmental Heat and Cold Exposure"], y = df["Age-standardized suicide rates (per 100 000 population)"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('Suicide rates (per 100 000)  vs. Per capita Environmental Heat and Cold Exposure')
        st.pyplot(fig)
        
        
        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["per_capita-Road Injuries"], y = df["Age-standardized suicide rates (per 100 000 population)"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('Suicide rates (per 100 000)  vs. Per capita Road Injuries')
        st.pyplot(fig)

        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["Mortality rate attributed to unintentional poisoning (per 100 000 population)"], y = df["Age-standardized suicide rates (per 100 000 population)"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('Suicide rates (per 100 000)  vs. Poisoning death rate (per 100 000)')
        st.pyplot(fig)
    if st.button("World Map"):
        st.image('Suicide1.png')





elif app_mode =='Prevalence Hypertension among adults':
    def add_bg_from_url():
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://github.com/Barge7/PROYECTO-FINAL/blob/main/imagenes/fondosivia70.png?raw=true");
            background-attachment: fixed;
            background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
            )
    add_bg_from_url()

    
    st.header("This app will predict a desired Medical value with its corresponding variables")
    st.image('hypertension.png')
    st.sidebar.header("Predictive Factors :")
    vio_dict = {1:-0.337,2:-0.329,3:-0.32,4:-0.3,5:-0.28,6:0.2,7:0.4,8:1.4,9:2.82,10:8.5}
    drug_dict = {1:-0.1742,2:-0.173,3:-0.17,4:-0.166,5:-0.1616,6:-0.145,7:-0.13,8:-0.11,9:0.5,10:1.87}
    gdp_dict = {1:-0.661,2:-0.63,3:-0.56,4:-0.5,5:-0.437,6:-0.28,7:-0.2,8:1.55,9:3.75,10:6.2497}
    health_dict = {1:-0.48,2:-0.462,3:-0.42,4:-0.38,5:-0.335,6:-0.26,7:-0.05,8:0.065,9:0.5,10:1.07}
    tuber_dict = {1:-0.67,2:-0.64,3:-0.592,4:-0.53,5:-0.47,6:-0.23,7:0.1,8:0.54,9:3.6,10:7.7}
    Violence=st.sidebar.slider('Violence',1,10,1)
    Drugs=st.sidebar.slider('Drugs',1,10,1)
    gdp=st.sidebar.slider('gdp',1,10,1)
    Health_ex=st.sidebar.slider('Health_ex',1,10,1)
    Tuberculosis=st.sidebar.slider('Tuberculosis',1,10,1)

    
   
   
    

    feature_list=[get_value(Violence,vio_dict),get_value(Drugs,drug_dict),get_value(gdp,gdp_dict),get_value(Health_ex,health_dict),get_value(Tuberculosis,tuber_dict)]

    single_sample = np.array(feature_list).reshape(1,-1)

    if st.button("Predict"):
        
   
   
        loaded_model = pickle.load(open('model_Prevalence of controlled hypertension among adults aged 30-79 years with hypertension, age-standardized.pkl', 'rb'))
        prediction = loaded_model.predict(single_sample)
        formatted_string = "{:.2f}".format(prediction[0])
        float_value = float(formatted_string)
        st.metric(label="Prevalence of hypertension among adults per 100", value=float_value)
        
    if st.button("Correlations"):    
        
        df = pd.read_csv('clean_full_data.csv')
        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["Interpersonal Violence"], y = df["Prevalence of controlled hypertension among adults aged 30-79 years with hypertension, age-standardized"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('Prevalence of hypertension among adults  vs. per capita Interpersonal Violence')
        st.pyplot(fig)
        
        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["Drug Use Disorders"], y = df["Prevalence of controlled hypertension among adults aged 30-79 years with hypertension, age-standardized"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('Prevalence of hypertension among adults  vs. Drug Use Disorders')
        st.pyplot(fig)

        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["gdp/percap"], y = df["Prevalence of controlled hypertension among adults aged 30-79 years with hypertension, age-standardized"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('Prevalence of hypertension among adults  vs. Per capita GDP')
        st.pyplot(fig)
        
        
        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["Domestic private health expenditure (PVT-D) per capita in US$"], y = df["Prevalence of controlled hypertension among adults aged 30-79 years with hypertension, age-standardized"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('Prevalence of hypertension among adults  vs. Per capita private health expenditure')
        st.pyplot(fig)

        fig = plt.figure(figsize=(10, 4))
        sns.regplot(x= df["Deaths due to tuberculosis among HIV-negative people (per 100 000 population)"], y = df["Prevalence of controlled hypertension among adults aged 30-79 years with hypertension, age-standardized"],scatter_kws={"color": "black"}, line_kws={"color": "red"})
        plt.title('Prevalence of hypertension among adults  vs. Tuberculosis (non-HIV) death rate (per 100 000)')
        st.pyplot(fig)      
    if st.button("World Map"):
        st.image('Hypertension1.png')        
            
            
            
            
            
            
            




