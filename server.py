import cv2
import threading
import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO

app = FastAPI()

# Permite que o Lovable acesse a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = YOLO("yolo.pt")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Não foi possível abrir a câmera.")

latest_detections = []
latest_frame_info = {
    "camera": True,
    "detections": [],
    "timestamp": 0
}

lock = threading.Lock()


def detection_loop():
    global latest_detections, latest_frame_info

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Não foi possível capturar um frame.")
            time.sleep(0.1)
            continue

        results = model(frame, verbose=False)

        detections = []

        for result in results:
            boxes = result.boxes

            for box in boxes:
                class_id = int(box.cls[0])
                confidence = float(box.conf[0])

                class_name = model.names[class_id]

                x1, y1, x2, y2 = box.xyxy[0].tolist()

                detections.append({
                    "class": class_name,
                    "confidence": round(confidence, 3),
                    "box": {
                        "x1": round(x1),
                        "y1": round(y1),
                        "x2": round(x2),
                        "y2": round(y2)
                    }
                })

        with lock:
            latest_detections = detections

            latest_frame_info = {
                "camera": True,
                "detections": detections,
                "timestamp": time.time()
            }


@app.get("/")
def root():
    return {
        "status": "online",
        "service": "EpiDetection YOLO"
    }


@app.get("/detections")
def get_detections():
    with lock:
        return latest_frame_info


@app.get("/health")
def health():
    return {
        "status": "ok",
        "camera": cap.isOpened()
    }

@app.get("/getEpi")
def getEpi():
    


thread = threading.Thread(
    target=detection_loop,
    daemon=True
)

thread.start()
