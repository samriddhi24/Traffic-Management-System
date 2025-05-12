# config.py
import os

# YOLO Config
YOLO_CFG_PATH = "yolov4.cfg"
YOLO_WEIGHTS_PATH = "yolov4.weights"
YOLO_CONFIDENCE_THRESHOLD = 0.5

# Tesseract OCR Path
TESSERACT_CMD = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Violation Parameters
SPEED_LIMIT = 80

# Snapshot Directory
SNAPSHOT_DIR = "snapshots/"
os.makedirs(SNAPSHOT_DIR, exist_ok=True)

# Logging
LOG_FILE = "system.log"

# Camera ID
CAMERA_ID = 0
