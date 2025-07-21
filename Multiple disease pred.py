#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 15:35:39 2025

@author: tgm
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load saved models
diabetes_model = pickle.load(open('/Users/tgm/Desktop/Multiple Disease Prediction/saved modals/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('/Users/tgm/Desktop/Multiple Disease Prediction/saved modals/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('/Users/tgm/Desktop/Multiple Disease Prediction/saved modals/parkinsons_model.sav', 'rb'))

# Sidebar navigation
with st.sidebar:
    selected = option_menu('Disease Prediction System Using ML',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinson’s Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction ')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Level')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input("Insulin Level")
    with col3:
        BMI = st.text_input("BMI Value")
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input("Age of the Person")

    diabetes_diagnosis = ''

    if st.button("Diabetes Test Result"):
        try:
            input_data = [float(Pregnancies), float(Glucose), float(BloodPressure),
                          float(SkinThickness), float(Insulin), float(BMI),
                          float(DiabetesPedigreeFunction), float(Age)]

            prediction = diabetes_model.predict([input_data])

            if prediction[0] == 1:
                diabetes_diagnosis = 'The person has Diabetes.'
            else:
                diabetes_diagnosis = 'The person does not have Diabetes.'

            st.success(diabetes_diagnosis)

        except:
            st.error("Please enter valid numeric values.")

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain Type')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholesterol (mg/dl)')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar (> 120 mg/dl, 1 = True; 0 = False)')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang = st.text_input('Exercise-Induced Angina (1 = Yes; 0 = No)')
    with col1:
        oldpeak = st.text_input('ST Depression Induced by Exercise')
    with col2:
        slope = st.text_input('Slope of the Peak Exercise ST Segment')
    with col3:
        ca = st.text_input('Number of Major Vessels Colored by Fluoroscopy')
    with col1:
        thal = st.text_input('Thalassemia (0 = Normal; 1 = Fixed Defect; 2 = Reversible Defect)')
  
    heart_diagnosis = ''

    if st.button("Heart Disease Test Result"):
        try:
            input_data = [float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs),
                          float(restecg), float(thalach), float(exang), float(oldpeak),
                          float(slope), float(ca), float(thal)]

            prediction = heart_disease_model.predict([input_data])

            if prediction[0] == 1:
                heart_diagnosis = 'The person has Heart Disease.'
            else:
                heart_diagnosis = 'The person does not have Heart Disease.'

            st.success(heart_diagnosis)

        except:
            st.error("Please enter valid numeric values.")

# Parkinson’s Disease Prediction Page
if selected == 'Parkinson’s Prediction':
    st.title('Parkinson’s Disease Prediction')

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('Jitter:DDP')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        APQ = st.text_input('MDVP:APQ')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('Spread1')
    with col5:
        spread2 = st.text_input('Spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''

    if st.button("Parkinson’s Test Result"):
        try:
            input_data = [str(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_abs),
                          float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB),
                          float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR), float(HNR),
                          float(RPDE), float(DFA), float(spread1), float(spread2), float(D2), float(PPE)]

            prediction = parkinsons_model.predict([input_data])

            if prediction[0] == 1:
                parkinsons_diagnosis = 'The person has Parkinson’s Disease.'
            else:
                parkinsons_diagnosis = 'The person does not have Parkinson’s Disease.'

            st.success(parkinsons_diagnosis)

        except:
            st.error("Please enter valid numeric values.")
