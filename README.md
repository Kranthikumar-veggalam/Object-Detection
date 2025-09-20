# 📹 Live Object Detection Web App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://YOUR_APP_LINK_HERE)

A real-time object detection application built with Python, OpenCV, and Streamlit. This app uses your webcam to identify objects in the video stream and draws bounding boxes around them with confidence scores.



---

## 🚀 Features

* **Real-Time Detection:** Identifies objects directly from your webcam feed.
* **Pre-Trained Model:** Powered by the fast and efficient **SSD MobileNet V2** model, pre-trained on the COCO dataset.
* **80 Classes:** Capable of detecting 80 different common objects (people, cars, bicycles, etc.).
* **Interactive Web UI:** Built with Streamlit for a clean and easy-to-use interface.

---

## 🛠️ Tech Stack

* **Python:** The core programming language.
* **Streamlit:** For building the interactive web application.
* **OpenCV:** For handling computer vision tasks and image processing.
* **NumPy:** For numerical operations on image data.

---

## ⚙️ How to Run Locally

To run this project on your own machine, follow these steps.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Kranthikumar-veggalam/Object-Detection.git](https://github.com/Kranthikumar-veggalam/Object-Detection.git)
    cd Object-Detection
    ```

2.  **Install the dependencies:**
    Make sure you have Python 3.8+ installed.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
    Your browser will open a new tab with the application running!

---

## ☁️ Deployment

This application is deployed on **Streamlit Community Cloud**. The deployment is configured to run directly from the `main` branch of this GitHub repository.

---

## ✨ How It Works

The application uses OpenCV's DNN (Deep Neural Network) module to load a pre-trained SSD MobileNet V2 model. The model processes each frame from the webcam, predicts the location and class of objects, and draws bounding boxes on the frame before displaying it back to the user. The `streamlit-webrtc` component is used to handle the real-time video stream from the browser to the Python backend.

---

## 🙏 Acknowledgements

* This project uses a model from the [TensorFlow Object Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md).
* Thanks to the developers of [Streamlit](https://streamlit.io/) and [OpenCV](https://opencv.org/).