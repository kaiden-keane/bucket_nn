from ultralytics import YOLO

model = YOLO('yolov8n.pt') # get pre-trained weights

if __name__ == '__main__':
    model.train(
        data='buckets.yaml',
        epochs=50,
        imgsz=640,
        batch=8,
        device='cuda'
    )