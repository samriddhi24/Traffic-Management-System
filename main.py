import cv2
from vehicle_detection import detect_vehicles
from plate_recognition import extract_number_plate
from violation_detection import detect_violation
from database import store_violation

# Initialize camera
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        print("Failed to capture image")
        break

    vehicles = detect_vehicles(frame)

    for vehicle_bbox in vehicles:
        number_plate = extract_number_plate(frame, vehicle_bbox)

        if number_plate:
            violations = detect_violation(number_plate, speed=90, red_light_status=True)  # Sample data
            if violations:
                for v in violations:
                    store_violation(number_plate, v)
                    print(f"Violation: {v}, Plate: {number_plate}")

    cv2.imshow("Traffic Monitoring", frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

