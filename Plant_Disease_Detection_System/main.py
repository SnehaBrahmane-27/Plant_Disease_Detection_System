import streamlit as st
import tensorflow as tf
import numpy as np
from treatment_data import get_treatment
from db import create_tables, register_user, validate_login, save_prediction, get_user_history,delete_prediction
import uuid
import os


create_tables()


st.markdown("""
    <style>

    /* Blue 'See Image' Button with hover effect */
    .stButton > button[data-testid="stSidebarNav"] {
        background-color: #3498db;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1.5em;
        font-weight: bold;
        border: none;
    }
    .stButton > button[data-testid="stSidebarNav"]:hover {
        background-color: #2980b9;
        transform: scale(1.1);
        transition: 0.3s;
    }

    /* Blue 'Predict' Button with hover effect */
    .stButton > button:first-child {
        background-color: #3498db;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1.5em;
        font-weight: bold;
        border: none;
    }
    .stButton > button:first-child:hover {
        background-color: #2980b9;
        transform: scale(1.1);
        transition: 0.3s;
    }

    </style>
""", unsafe_allow_html=True)




if "user" not in st.session_state:
    st.session_state.user = None

if st.session_state.user is None:
    st.sidebar.subheader("Login/Register")
    choice = st.sidebar.radio("Action", ["Login", "Register"])
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if choice == "Register":
        if st.sidebar.button("Register"):
            if register_user(username, password):
                st.sidebar.success("Registered! Please login.")
            else:
                st.sidebar.error("Username exists.")

    if choice == "Login":
        if st.sidebar.button("Login"):
            if validate_login(username, password):
                st.session_state.user = username
                st.rerun()
            else:
                st.sidebar.error("Invalid credentials")
else:
    st.sidebar.success(f"Logged in as {st.session_state.user}")
    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.rerun()

    st.sidebar.title("Dashboard")
    lan = st.sidebar.radio("Choose Language / भाषा निवडा ",["English","Marathi","Hindi"])
    tabs = st.tabs(["🏠 Home", "🌿 Recognize", "💊 Treatments", "📜 History"])



    def model_prediction(test_img):
        model=tf.keras.models.load_model('trained_model.keras')
        img = tf.keras.preprocessing.image.load_img(test_img,target_size=(128,128))
        img_arr= tf.keras.preprocessing.image.img_to_array(img)
        img_arr=np.array([img_arr])
        prediction= model.predict(img_arr)
        result_index=np.argmax(prediction)
        return result_index 


    with tabs[0]:
        st.header("PLANT DISEASE RECOGNITION SYSTEM")
        img_path = ('home_page.jpg')
        st.image(img_path,use_container_width=True)
        st.markdown("""
        ## Welcome to the Plant Disease Recognition System! 🌿🔍
        
        Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

        ### How It Works
        1. **Upload Image:** Go to the **Disease Recognition** page and upload an image of a plant with suspected diseases.
        2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
        3. **Results:** View the results and recommendations for further action.

        ### Why Choose Us?
        - **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
        - **User-Friendly:** Simple and intuitive interface for seamless user experience.
        - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.

        ### Get Started
        Click on the **Disease Recognition** page in the sidebar to upload an image and experience the power of our Plant Disease Recognition System!

        """)


    with tabs[1]:
        st.header("Upload your plant leaf here  !!")
        test_img = st.file_uploader("")
        if(st.button("see image")):
            try:
                st.image(test_img,use_container_width=True)
            except:
                st.error("upload image first")
        if(st.button("Recognize",icon="🌿")):
            try:
                class_name=['Apple -Apple scab',
                'Apple -Black rot',
                'Apple -Cedar apple rust',
                'Apple is healthy',
                'Blueberry is healthy',
                'Cherry -Powdery mildew',
                'Cherry is healthy',
                'Corn(maize) -Cercospora leaf spot , Gray leaf spot',
                'Corn(maize) -Common rust',
                'Corn(maize) -Northern leaf blight',
                'Corn(maize) is healthy',
                'Grape -Black rot',
                'Grape -Esca(Black measles)',
                'Grape -Leaf blight (Isariopsis leaf spot)',
                'Grape is healthy',
                'Orange -Haunglongbing(Citrus greening)',
                'Peach -Bacterial spot',
                'Peach is healthy',
                'Pepper,bell -Bacterial spot',
                'Pepper,bell is healthy',
                'Potato -Early blight',
                'Potato -Late blight',
                'Potato is healthy',
                'Raspberry is healthy',
                'Soybean is healthy',
                'Squash -Powdery mildew',
                'Strawberry -Leaf scorch',
                'Strawberry is healthy',
                'Tomato -Bacterial spot',
                'Tomato -Early blight',
                'Tomato -Late blight',
                'Tomato -Leaf mold',
                'Tomato -Septoria leaf spot',
                'Tomato -Spider mites , Two spotted spider mite',
                'Tomato -Target spot',
                'Tomato -Yellow leaf curl virus',
                'Tomato -Mosaic virus',
                'Tomato is healthy']

                result_index= model_prediction(test_img)
                st.success("Model is predicting it's a {}".format(class_name[result_index]))
                st.info(get_treatment(class_name[result_index],lan))

                os.makedirs("saved_images", exist_ok=True)
                unique_name = f"saved_images/{uuid.uuid4().hex}.jpg"
                with open(unique_name, "wb") as f:
                    f.write(test_img.getbuffer())
                save_prediction(st.session_state.user, unique_name, class_name[result_index])
            except:
                st.error("upload image first")
    

    with tabs[2]:
        st.subheader("Treatment Section")
        st.markdown("Search and select a disease below to view its treatment:")

        diseases = [
            'Apple -Apple scab', 'Apple -Black rot', 'Apple -Cedar apple rust', 'Apple is healthy',
            'Blueberry is healthy', 'Cherry -Powdery mildew', 'Cherry is healthy',
            'Corn(maize) -Cercospora leaf spot , Gray leaf spot', 'Corn(maize) -Common rust',
            'Corn(maize) -Northern leaf blight', 'Corn(maize) is healthy', 'Grape -Black rot',
            'Grape -Esca(Black measles)', 'Grape -Leaf blight (Isariopsis Leaf Spot)', 'Grape is healthy',
            'Orange -Haunglongbing(Citrus greening)', 'Peach -Bacterial spot', 'Peach is healthy',
            'Pepper,bell -Bacterial spot', 'Pepper,bell is healthy', 'Potato -Early blight',
            'Potato -Late blight', 'Potato is healthy', 'Raspberry is healthy', 'Soybean is healthy',
            'Squash -Powdery mildew', 'Strawberry -Leaf scorch', 'Strawberry is healthy',
            'Tomato -Bacterial spot', 'Tomato -Early blight', 'Tomato -Late blight', 'Tomato -Leaf mold',
            'Tomato -Septoria leaf spot', 'Tomato -Spider mites , Two spotted spider mite',
            'Tomato -Target spot', 'Tomato -Yellow leaf curl virus', 'Tomato -Mosaic virus', 'Tomato is healthy'
        ]

        search_query = st.text_input("Search disease")
        filtered_diseases = [d for d in diseases if search_query.lower() in d.lower()]


        for disease in filtered_diseases:
                with st.expander(disease):
                    st.write(get_treatment(disease, lan))

    
    
    with tabs[3]:
        st.subheader("🗞 Your Prediction History")
        history = get_user_history(st.session_state.user)
        
        if not history:
            st.info("No prediction history yet.")
        else:
            for h in history:
                with st.container():
                    st.image(h[2], width=250)
                    st.write(f"**Disease**: {h[3]}")
                    st.caption(f"🕓 {h[4]}")
                    if st.button(f"🗑 Delete", key=f"del_{h[0]}"):
                        delete_prediction(h[0])
                        st.success("Prediction deleted successfully!")
                        st.rerun()
                    st.markdown("---")


