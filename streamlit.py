import streamlit as st
import pandas as pd
import numpy as np
import pickle  #to load a saved model
import base64

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64



@st.cache(suppress_st_warning=True)
def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value
app_mode = st.sidebar.selectbox('Select Disease',['Adolescent birth rate (per1000)','Total NCD Deaths (in thousands)','Homicide rates (per 100 000)','Suicide rates (per 100 000)','Prevalence Hypertension among adults'])
 
   
   
if app_mode =='Adolescent birth rate (per1000)':
    
    csv=pd.read_csv("informations.csv")
    st.write(csv)

    st.image('slider-short-3.jpg')

    st.subheader('Sir/Mme , YOU need to fill all neccesary informations in order to get a reply to your prediction !')
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

 
   
   
    data1={
    'ApplicantIncome':ApplicantIncome,
    'CoapplicantIncome':CoapplicantIncome,
    'Self Employed':Self_Employed,
    'LoanAmount':LoanAmount,
    'Loan_Amount_Term':Loan_Amount_Term,
    'Credit_History':Credit_History,
    'Property_Area':[Rural,Urban,Semiurban],
    }

    feature_list=[ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,get_value(Gender,gender_dict),get_fvalue(Married),data1['Dependents'][0],data1['Dependents'][1],data1['Dependents'][2],data1['Dependents'][3],get_value(Education,edu),get_fvalue(Self_Employed),data1['Property_Area'][0],data1['Property_Area'][1],data1['Property_Area'][2]]

    single_sample = np.array(feature_list).reshape(1,-1)

    if st.button("Predict"):
        file_ = open("6m-rain.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
   
   
        loaded_model = pickle.load(open('Random_Forest.sav', 'rb'))
        prediction = loaded_model.predict(single_sample)
        if prediction[0] == 0 :
            st.error(
    'According to our Calculations, you will not get the loan from Bank'
    )
            st.markdown(
    f'<img src="data:image/gif;base64,{data_url_no}" alt="cat gif">',
    unsafe_allow_html=True,)
        elif prediction[0] == 1 :
            st.success(
    'Congratulations!! you will get the loan from Bank'
    )
            st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
    )

            


elif app_mode =='Total NCD Deaths (in thousands)':
    
    csv=pd.read_csv("informations.csv")
    st.write(csv)

    st.image('slider-short-3.jpg')
    st.subheader('Sir/Mme , YOU need to fill all neccesary informations in order to get a reply to your prediction !')
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

    
   
   
    data1={
    'ApplicantIncome':ApplicantIncome,
    'CoapplicantIncome':CoapplicantIncome,
    'Self Employed':Self_Employed,
    'LoanAmount':LoanAmount,
    'Loan_Amount_Term':Loan_Amount_Term,
    'Credit_History':Credit_History
    }

    feature_list=[ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,get_value(Gender,gender_dict),get_fvalue(Married),data1['Dependents'][0],data1['Dependents'][1],data1['Dependents'][2],data1['Dependents'][3],get_value(Education,edu),get_fvalue(Self_Employed),data1['Property_Area'][0],data1['Property_Area'][1],data1['Property_Area'][2]]

    single_sample = np.array(feature_list).reshape(1,-1)

    if st.button("Predict"):
        file_ = open("6m-rain.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
   
        file = open("green-cola-no.gif", "rb")
        contents = file.read()
        data_url_no = base64.b64encode(contents).decode("utf-8")
        file.close()
   
   
        loaded_model = pickle.load(open('Random_Forest.sav', 'rb'))
        prediction = loaded_model.predict(single_sample)
        if prediction[0] == 0 :
            st.error(
    'According to our Calculations, you will not get the loan from Bank'
    )
            st.markdown(
    f'<img src="data:image/gif;base64,{data_url_no}" alt="cat gif">',
    unsafe_allow_html=True,)
        elif prediction[0] == 1 :
            st.success(
    'Congratulations!! you will get the loan from Bank'
    )
            st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
    )

elif app_mode =='Homicide rates (per 100 000)':
    
    csv=pd.read_csv("informations.csv")
    st.write(csv)

    st.image('slider-short-3.jpg')
    st.subheader('Sir/Mme , YOU need to fill all neccesary informations in order to get a reply to your prediction !')
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

    
   
   
    data1={
    'ApplicantIncome':ApplicantIncome,
    'CoapplicantIncome':CoapplicantIncome,
    'Self Employed':Self_Employed,
    'LoanAmount':LoanAmount,
    'Loan_Amount_Term':Loan_Amount_Term,
    'Credit_History':Credit_History
    }

    feature_list=[ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,get_value(Gender,gender_dict),get_fvalue(Married),data1['Dependents'][0],data1['Dependents'][1],data1['Dependents'][2],data1['Dependents'][3],get_value(Education,edu),get_fvalue(Self_Employed),data1['Property_Area'][0],data1['Property_Area'][1],data1['Property_Area'][2]]

    single_sample = np.array(feature_list).reshape(1,-1)

    if st.button("Predict"):
        file_ = open("6m-rain.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
   
        file = open("green-cola-no.gif", "rb")
        contents = file.read()
        data_url_no = base64.b64encode(contents).decode("utf-8")
        file.close()
   
   
        loaded_model = pickle.load(open('Random_Forest.sav', 'rb'))
        prediction = loaded_model.predict(single_sample)
        if prediction[0] == 0 :
            st.error(
    'According to our Calculations, you will not get the loan from Bank'
    )
            st.markdown(
    f'<img src="data:image/gif;base64,{data_url_no}" alt="cat gif">',
    unsafe_allow_html=True,)
        elif prediction[0] == 1 :
            st.success(
    'Congratulations!! you will get the loan from Bank'
    )
            st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
    )            
            
            
elif app_mode =='Suicide rates (per 100 000)':
    
    csv=pd.read_csv("informations.csv")
    st.write(csv)

    st.image('slider-short-3.jpg')
    st.subheader('Sir/Mme , YOU need to fill all neccesary informations in order to get a reply to your prediction !')
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

    
   
   
    data1={
    'ApplicantIncome':ApplicantIncome,
    'CoapplicantIncome':CoapplicantIncome,
    'Self Employed':Self_Employed,
    'LoanAmount':LoanAmount,
    'Loan_Amount_Term':Loan_Amount_Term,
    'Credit_History':Credit_History
    }

    feature_list=[ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,get_value(Gender,gender_dict),get_fvalue(Married),data1['Dependents'][0],data1['Dependents'][1],data1['Dependents'][2],data1['Dependents'][3],get_value(Education,edu),get_fvalue(Self_Employed),data1['Property_Area'][0],data1['Property_Area'][1],data1['Property_Area'][2]]

    single_sample = np.array(feature_list).reshape(1,-1)

    if st.button("Predict"):
        file_ = open("6m-rain.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
   
        file = open("green-cola-no.gif", "rb")
        contents = file.read()
        data_url_no = base64.b64encode(contents).decode("utf-8")
        file.close()
   
   
        loaded_model = pickle.load(open('Random_Forest.sav', 'rb'))
        prediction = loaded_model.predict(single_sample)
        if prediction[0] == 0 :
            st.error(
    'According to our Calculations, you will not get the loan from Bank'
    )
            st.markdown(
    f'<img src="data:image/gif;base64,{data_url_no}" alt="cat gif">',
    unsafe_allow_html=True,)
        elif prediction[0] == 1 :
            st.success(
    'Congratulations!! you will get the loan from Bank'
    )
            st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
    )      
            
            
elif app_mode =='Prevalence Hypertension among adults'
    
    csv=pd.read_csv("informations.csv")
    st.write(csv)

    st.image('slider-short-3.jpg')
    st.subheader('Sir/Mme , YOU need to fill all neccesary informations in order to get a reply to your prediction !')
    st.sidebar.header("Predictive Factors :")
    vio_dict = {1:-0.337,2:-0.329,3:-0.32,4:-0.3,5:-0.28:0.2,7:0.4,8:1.4,9:2.82,10:8.5}
    drug_dict = {1:-0.1742,2:-0.173,3:-0.17,4:-0.166,5:-0.1616,6:-0.145,7:-0.13,8:-0.11,9:0.5,10:1.87}
    gdp_dict = {1:-0.661,2:-0.63,3:-0.56,4:-0.5,5:-0.437,6:-0.28,7:-0.2,8:1.55,9:3.75,10:6.2497}
    health_dict = {1:-0.48,2:-0.462,3:-0.42,4:-0.38,5:-0.335,6:-0.26,7:-0.05,8:0.065,9:0.5,10:1.07}
    tuber_dict = {1:-0.67,2:-0.64,3:-0.592,4:-0.53,5:-0.47,6:-0.23,7:0.1,8:0.54,9:3.6,10:7.7}
    Violence=st.sidebar.slider('Violence',1,10,1)
    Drugs=st.sidebar.slider('Drugs',1,10,1)
    gdp=st.sidebar.slider('gdp',1,10,1)
    Health_ex=st.sidebar.slider('Health_ex',1,10,1)
    Tuberculosis=st.sidebar.slider('Tuberculosis',1,10,1)

    
   
   
    data1={
    'ApplicantIncome':ApplicantIncome,
    'CoapplicantIncome':CoapplicantIncome,
    'Self Employed':Self_Employed,
    'LoanAmount':LoanAmount,
    'Loan_Amount_Term':Loan_Amount_Term,
    'Credit_History':Credit_History
    }

    feature_list=[ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,get_value(Gender,gender_dict),get_fvalue(Married),data1['Dependents'][0],data1['Dependents'][1],data1['Dependents'][2],data1['Dependents'][3],get_value(Education,edu),get_fvalue(Self_Employed),data1['Property_Area'][0],data1['Property_Area'][1],data1['Property_Area'][2]]

    single_sample = np.array(feature_list).reshape(1,-1)

    if st.button("Predict"):
        file_ = open("6m-rain.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
   
        file = open("green-cola-no.gif", "rb")
        contents = file.read()
        data_url_no = base64.b64encode(contents).decode("utf-8")
        file.close()
   
   
        loaded_model = pickle.load(open('Random_Forest.sav', 'rb'))
        prediction = loaded_model.predict(single_sample)
        if prediction[0] == 0 :
            st.error(
    'According to our Calculations, you will not get the loan from Bank'
    )
            st.markdown(
    f'<img src="data:image/gif;base64,{data_url_no}" alt="cat gif">',
    unsafe_allow_html=True,)
        elif prediction[0] == 1 :
            st.success(
    'Congratulations!! you will get the loan from Bank'
    )
            st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
    )                        
            
            
            
            
            
            
            
            




