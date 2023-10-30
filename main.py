import threading
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2

def CV(cam):
    model = YOLO(r"...\PlantVision YOLOV8\runs\detect\train\weights\best.pt")
    model.predict(source=f"{cam}", show=True, imgsz=512, conf=0.2, max_det=5, verbose=False)


def main():
    thread1 = threading.Thread(target=CV, args=(1,))
    thread2 = threading.Thread(target=CV, args=(2,))
    
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()
