# 📹 Live Webcam Object Detection

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://object-detection-kk.streamlit.app/)

This project is a real-time object detection application that uses a webcam to identify and classify objects in the video stream. It is built with Python and OpenCV, and the interactive web interface is powered by Streamlit.

![Live Object Detection GIF](https://i.imgur.com/your-gif-url.gif)


## 🚀 Features

* **Real-Time Detection:** Identifies objects directly from your webcam feed using `streamlit-webrtc`.
* **Pre-Trained Model:** Powered by the fast and efficient **SSD MobileNet V2** model, pre-trained on the COCO dataset.
* **80 Classes:** Capable of detecting 80 different common objects like people, cars, bicycles, and more.
* **Interactive Web UI:** A clean and easy-to-use interface built with Streamlit.

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** for the web interface
* **streamlit-webrtc** for real-time video streaming
* **opencv-python-headless** for computer vision
* **NumPy** for numerical operations

---

## ⚙️ How to Run Locally

To run this project on your own machine, follow these steps.

1.  **Clone the repository:**
    ```bash
    git clone git clone [https://github.com/Kranthikumar-veggalam/Object-Detection.git](https://github.com/Kranthikumar-veggalam/Object-Detection.git)
    cd Object-Detection
    ```

2.  **Install the dependencies:**
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

This application is deployed on [Streamlit Community Cloud](https://streamlit.io/cloud). It is configured to run directly from the `main` branch of this GitHub repository.
