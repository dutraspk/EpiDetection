import cv2
from ultralytics import YOLO

model = YOLO("yolo.pt")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    result = model(frame, save=True)
    annoted_frame = result[0].plot()
    
    cv2.imshow("CDRX - WEBcam", annoted_frame)


    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
