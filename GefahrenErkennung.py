import cv2
import numpy as np
import requests
import time
from ultralytics import YOLO
from skimage.metrics import structural_similarity as ssim

model = YOLO("yolo11n.pt")
cap = cv2.VideoCapture(0)

def is_occluded(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    brightness = np.mean(gray)
    variance = np.var(gray)

    return brightness < 50 or variance < 500

def is_camera_moved(frame1, prev_frame):
    if frame1 is None or prev_frame is None:
        return False
    
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    score, _ = ssim(gray1, gray2, full=True)

    return score < 0.7

last_sent = 0
COOLDOWN = 5  

def send_alert(message):
    global last_sent
    now = time.time()
    if now - last_sent < COOLDOWN:
        print("Alarm Cooldwon.")
        return

    url = "***"  #erstelle selber Bot
    data = {
        "chat_id": "***",  #starte Bot und geh auf /getUpdates 
        "text": message
    }
    requests.post(url, data=data)
    print(f"Alarm gesendet: {message}")
    last_sent = now

prev_frame = None

while True:
    ret, frame = cap.read()
    if not ret:
        break
    #YOLO
    results = model(frame)
    #occlusion detection
    occluded = is_occluded(frame)
    #camera movement detection
    moved = is_camera_moved(frame, prev_frame)
    prev_frame = frame.copy()
    #Display results
    status = "OK"
    if occluded:
        status = "Occluded"
        send_alert("Kamera ist verdeckt!")
    elif moved:
        status = "Moved"
        send_alert("Da bewegt sich was!")
    
    cv2.putText(frame, status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("System", frame)
    if cv2.waitKey(1) == 27: # ESC zum Aufhören
        break

cap.release()
cv2.destroyAllWindows()
