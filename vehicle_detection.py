# vehicle_detection.py
import cv2
import numpy as np
import logging
from config import YOLO_CFG_PATH, YOLO_WEIGHTS_PATH, YOLO_CONFIDENCE_THRESHOLD

# Load YOLO model once
net = cv2.dnn.readNet(YOLO_WEIGHTS_PATH, YOLO_CFG_PATH)
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

def detect_vehicles(frame):
    try:
        height, width, _ = frame.shape
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)
        detections = net.forward(output_layers)

        vehicles = []
        for detection in detections:
            for obj in detection:
                scores = obj[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > YOLO_CONFIDENCE_THRESHOLD and class_id in [2, 3, 5, 7]:  # Car, Motorcycle, Bus, Truck
                    center_x, center_y, w, h = (obj[:4] * np.array([width, height, width, height])).astype(int)
                    x, y = center_x - w // 2, center_y - h // 2
                    vehicles.append((x, y, w, h))

        return vehicles

    except Exception as e:
        logging.error(f"Vehicle detection failed: {e}")
        return []
