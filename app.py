# app.py
import streamlit as st
import cv2
import numpy as np
from streamlit_webrtc import webrtc_streamer
import av

@st.cache_resource
def load_model():
    """Loads the object detection model and class names."""
    try
        pbtxt_file = 'ssd_mobilenet_v2_coco_2018_03_29.pbtxt'
        pb_file = 'frozen_inference_graph.pb'
        net = cv2.dnn.readNetFromTensorflow(pb_file, pbtxt_file)
        
        with open('coco.names', 'r') as f:
            class_names = f.read().splitlines()
        return net, class_names
    except FileNotFoundError:
        st.error("Model files not found. Please make sure frozen_inference_graph.pb, ssd_mobilenet_v2_coco_2018_03_29.pbtxt, and coco.names are in the same folder as app.py.")
        return None, None
    except cv2.error as e:
        st.error(f"Error loading model files. OpenCV Error: {e}")
        return None, None

net, class_names = load_model()

def detect_objects(image_np, network, classes):
    """Takes an image, runs detection, and returns the image with boxes drawn."""
    if network is None:
        st.warning("Model is not loaded, cannot perform detection.")
        return image_np

    h, w, _ = image_np.shape
    blob = cv2.dnn.blobFromImage(image_np, size=(300, 300), swapRB=True, crop=False)
    network.setInput(blob)
    detections = network.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.6:
            class_id = int(detections[0, 0, i, 1])
            
            # --- THE FIX ---
            # Subtract 1 from class_id for 0-based list index and check bounds
            if class_id - 1 < len(classes):
                label_text = classes[class_id - 1]
            
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                label = f"{label_text}: {confidence:.2f}"
                cv2.rectangle(image_np, (startX, startY), (endX, endY), (0, 255, 0), 2)
                cv2.putText(image_np, label, (startX, startY - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return image_np

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    processed_img = detect_objects(img, net, class_names)
    return av.VideoFrame.from_ndarray(processed_img, format="bgr24")

st.set_page_config(layout="wide", page_title="Live Object Detection")
st.title("📹 Live Object Detection App")
st.write("Click START to activate your camera. The application will identify objects in real-time.")
st.write("---")

webrtc_streamer(
    key="object-detection",
    video_frame_callback=video_frame_callback,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)