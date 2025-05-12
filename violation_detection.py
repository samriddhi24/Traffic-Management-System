# violation_detection.py
from config import SPEED_LIMIT

def detect_violation(vehicle_id, speed, red_light_status):
    violations = []

    if speed > SPEED_LIMIT:
        violations.append("Overspeeding")

    if red_light_status:
        violations.append("Red Light Jumping")

    return violations if violations else None
