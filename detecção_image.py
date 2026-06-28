from ultralytics import YOLO

model = YOLO("yolo.pt")
results = model("foto.jpg", save=True)

print("foi")
