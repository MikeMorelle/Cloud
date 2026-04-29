import cv2
import numpy as np
import requests
import time
from ultralytics import YOLO
from skimage.metrics import structural_similarity as ssim

#YOLO Modell laden 
model = YOLO("best(1).pt")
cap = cv2.VideoCapture(0)

def is_occluded(frame):
    if frame is None:
        return False
    
    #Bild in Graustufen umwandeln
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    #Helligkeit/Varianz berechnen 
    brightness = np.mean(gray)
    variance = np.var(gray)
    #Schwellenwerte
    return brightness < 50 or variance < 500

def is_camera_moved(frame1, prev_frame):
    if frame1 is None or prev_frame is None:
        return False
    
    #Bilder in Graustufen umwandeln
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    #Strucural Similarity Index (0-1) berechnen
    score, _ = ssim(gray1, gray2, full=True)
    #Schwellenwert
    return score < 0.7

#Cooldown gegen Spam-Alerts
last_sent = 0
COOLDOWN = 5  

def send_alert(message):
    #aktuelle und letzte Sendezeit vergleichen
    global last_sent
    now = time.time()
    #Prüfen, ob Cooldown aktiv ist
    if now - last_sent < COOLDOWN:
        print("ALARM SPAM VERHINDERT")
        return
    #Telegram Bot API aufrufen
    url = "https://api.telegram.org/bot8358523968:AAH43qZhtvkxW8FVYAaf-NKjxaoG2kQl9c4/sendMessage"
    data = {
        "chat_id": "8765793935",
        "text": message
    }
    requests.post(url, data=data)
    print(f"ALARM!!! {message}")
    last_sent = now

#Vorheriges Frame für Bewegungserkennung
prev_frame = None

while True:
    #Frame von Kamera lesen
    ret, frame = cap.read()
    #Redo wenn kein Frame gelesen werden konnte
    if not ret:
        break
    #YOLO model auf Frame anwenden
    results = model(frame)
   
    #Verdeckenserkennung
    occluded = is_occluded(frame)
    #Bewegungserkennung
    moved = is_camera_moved(frame, prev_frame)
    prev_frame = frame.copy()

    #Status ggf. Alarm setzen
    status = "OK"
    if occluded:
        status = "Verdeckt"
        send_alert("Die Kamera ist verdeckt!")
    elif moved:
        status = "Bewegt"
        send_alert("ES IST BÖSES IM BUSCH!")
    if len(results[0].boxes) > 0:
        if results[0].boxes.cls[0] == 0:  # Klasse 0 = Feuer
            status = "Feuer"
        elif results[0].boxes.cls[0] == 1:  # Klasse 1 = Rauch
            status = "Rauch"
        send_alert("ES BRENNT!")
    
    #Status auf Frame anzeigen
    cv2.putText(frame, status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("System", frame)
    #ESC key to exit
    if cv2.waitKey(1) == 27: 
        break

#Ressourcen freigeben
cap.release()
cv2.destroyAllWindows()
