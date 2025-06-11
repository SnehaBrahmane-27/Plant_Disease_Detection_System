
# 🌿 PLANT DISEASE DETECTION SYSTEM

A multilingual, deep learning-powered web application that identifies plant diseases from leaf images and recommends appropriate treatments. Designed for accessibility and scalability, it features a user login system, treatment recommendations in multiple Indian languages, and a history tracking system — all within an intuitive tabbed interface using Streamlit.

---

## 🚀 FEATURES

* 🔍 **Accurate Disease Prediction** using a trained CNN model
* 🌐 **Multilingual Treatment Recommendations** (English, Hindi, Marathi, etc.)
* 🔒 **User Login & Registration** with session tracking
* 📁 **Prediction History** stored securely with SQLite
* 🧭 **Tabbed Interface**: Home | Predict | Treatments | History
* 📷 Upload an image of the affected plant leaf and get instant results

---

## 🧠 MACHINE LEARNING OVERVIEW

* **Model**: Convolutional Neural Network (CNN)
* **Framework**: TensorFlow / Keras
* **Training Dataset**: Public plant disease datasets
* **Metrics**:

  * Accuracy: \~97%
  * Precision, Recall, F1-Score
* **Output Labels**: 30+ plant diseases across 10+ crops

---

## 📥 MODEL INPUT

The prediction module uses a trained image classification model. The user uploads a **leaf image**, and the system returns the detected disease.

---

## 🌾 SUPPORTED CROPS & DISEASES

* **Tomato**: Early Blight, Late Blight, Mosaic Virus
* **Potato**: Early Blight, Late Blight
* **Apple**: Apple Scab, Black Rot
* **Corn**, **Grapes**, **Orange**, and more
* 30+ diseases supported

---

## 🌐 MULTILINGUAL TREATMENT SUPPORT

* Languages: English 🇬🇧, Hindi 🇮🇳, Marathi 🇮🇳
* Expandable for additional regional languages
* Treatment data is shown via collapsible tabs for better UX

---

## 🛠️ TECHNOLOGIES USED

* **Python**
* **Streamlit**
* **TensorFlow / Keras**
* **SQLite**
* **Pandas, NumPy**
* **HTML / CSS**

---

## 📊 DATA & DATABASE

* **Input**: Leaf images uploaded by users
* **Output**: Predicted disease and recommended treatment in the selected language
* **Database**: Stores user info, prediction timestamp, image path, and result


---

## 📂 PROJECT STRUCTURE

```plaintext
Plant_Disease_Detection_System/
├── Dataset/
│   ├── train/               # Training images
│   └── valid/               # Validation images
├── saved_images/           # User-uploaded images
├── test/                   # Testing images
├── data.py                 # Helper for image loading
├── db.py                   # SQLite database functions
├── home_page.jpg           # Homepage background image
├── main.py                 # Streamlit app entry point
├── predictions.db          # Stores prediction history
├── README.md               # Project description
├── requirement.txt         # Python dependencies
├── Test_model.ipynb        # Model testing notebook
├── Train_model.ipynb       # Model training notebook
├── trained_model.keras     # Trained CNN model
├── training_hist.json      # Model training history
├── treatment_data.py       # Treatment text per disease
└── users.db                # User credentials and logins

```


---

## 📊 DATASET

The **Plant Disease Detection System** uses the **New Plant Diseases Dataset** from Kaggle, which consists of two main sets of plant images:

* **Training Set**: 70,295 images of plant leaves from various crops, used to train the deep learning model.
* **Testing Set**: 17,572 images, used to evaluate the model's performance.

### Dataset Source:

* **Source**: [New Plant Diseases Dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)

---


## 💻 HOW TO RUN LOCALLY

1. Clone the repository:

   ```bash
   git clone https://github.com/SnehaBrahmane-27/Plant_Disease_Detection_System.git
   cd plant-disease-detection
   ```

2. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run main.py
   ```

4. Open the app in your browser:
   [http://localhost:8501](http://localhost:8501)


---

## 📸 DEMO

![App Screenshot](path/to/screenshot.png)


---

## 📌 FUTURE ENHANCEMENTS

* Admin dashboard for managing treatments and diseases
* OCR for scanning prescription images
* Voice assistance & accessibility features
* Deployment to Render / AWS / Azure
* REST API for third-party integration

---

## 👤 AUTHOR

**Sneha Brahmane**
B.Tech in IT
📧 Email: [snehabrahmane281@gmail.com](mailto:snehabrahmane281@gmail.com)
🌐 GitHub: [github.com/SnehaBrahmane-27](https://github.com/SnehaBrahmane-27)

---

## 📝 LICENSE

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🔧 BADGES

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

