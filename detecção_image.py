from ultralytics import YOLO

model = YOLO("/home/dutra/Projetos/datayolo/datatrain/yolo.pt")
results = model("/home/dutra/Downloads/tr.jpeg", save=True)

print("foi")
