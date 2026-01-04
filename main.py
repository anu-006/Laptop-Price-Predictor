
import streamlit as st
import pickle
import numpy as np

data = pickle.load(open("data.pkl","rb"))
pipe = pickle.load(open("pipe.pkl","rb"))

st.title("Laptop Price Predictor")

company=st.selectbox("Select laptop brand",data["Company"].unique())

TypeName=st.selectbox("Select type",data["TypeName"].unique())

Ram=st.selectbox("Select Ram (in GB) ",data["Ram"].unique())

Weight=st.number_input("Select Weight",min_value=0.5,max_value=6.0)

touchscreen=st.selectbox("touchscreen",["Yes","No"])

IPS=st.selectbox("IPS",['Yes','No'])

Ultra_HD_4k=st.selectbox("4K Ultra HD",['Yes','No'])

Quad_HD=st.selectbox("Quad HD+",['Yes','No'])

screen_size=st.slider("Choose Screen size",10.0, 18.0, 13.0)

screen_resolution=st.selectbox("Choose Screen resolution",['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

Processor_brand=st.selectbox("Select Processor",data["Processor_brand"].unique())

clock_speed=st.number_input("Clock Speed (in GHz)",min_value=1.0,max_value=5.0,step=0.1)

HDD=st.selectbox("HDD (in GB)",[0,128,256,512,1024,2048])

SSD=st.selectbox("SSD (in GB) ",[0,8,128,256,512,1024])

Gpu_brand=st.selectbox("Select Gpu ",data["Gpu_brand"].unique())

Os_brand=st.selectbox("Select Operating System ",data["Os_brand"].unique())

if st.button("Predict Price"):
    pixel_per_inch = None

    if touchscreen=="Yes":
        touchscreen=1
    else:
        touchscreen=0

    if IPS=="Yes":
        IPS=1
    else:
        IPS=0

    if Ultra_HD_4k=="Yes":
        Ultra_HD_4k=1
    else:
        Ultra_HD_4k=0

    if Quad_HD=="Yes":
        Quad_HD=1
    else:
        Quad_HD=0

    x_resol = int(screen_resolution.split("x")[0])
    y_resol = int(screen_resolution.split("x")[1])

    pixel_per_inch = ((x_resol**2) + (y_resol**2))**0.5 / screen_size

    import pandas as pd
    input_dict = {
        'Company': [company],
        'TypeName': [TypeName],
        'Ram': [Ram],
        'Weight': [Weight],
        'touchscreen': [touchscreen],
        'IPS': [IPS],
        '4K Ultra HD': [Ultra_HD_4k],
        'Quad HD+': [Quad_HD],
        'pixel_per_inch': [pixel_per_inch],
        'Processor_brand': [Processor_brand],
        'clock_speed': [clock_speed],
        'HDD': [HDD],
        'SSD': [SSD],
        'Gpu_brand': [Gpu_brand],
        'Os_brand': [Os_brand]
    }
    query_df = pd.DataFrame(input_dict)
    prediction = pipe.predict(query_df)
    st.write("The predicted price for the laptop is: Rs." + str(int(np.exp(prediction[0]))))

