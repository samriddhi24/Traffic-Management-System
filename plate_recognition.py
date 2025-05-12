# plate_recognition.py
import cv2
import pytesseract
import re
import logging
import os
from config import TESSERACT_CMD, SNAPSHOT_DIR

pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

def extract_number_plate(frame, vehicle_bbox):
    x, y, w, h = vehicle_bbox
    vehicle_img = frame[y:y + h, x:x + w]

    try:
        gray = cv2.cvtColor(vehicle_img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

        plate_text = pytesseract.image_to_string(thresh, config="--psm 8")
        cleaned = re.findall(r'[A-Z0-9]{5,10}', plate_text.upper())

        if cleaned:
            # Optional: Save plate crop for reference
            plate_img_path = os.path.join(SNAPSHOT_DIR, f"plate_{cleaned[0]}.jpg")
            cv2.imwrite(plate_img_path, thresh)

        return cleaned[0] if cleaned else None

    except Exception as e:
        logging.error(f"OCR failed: {e}")
        return None
