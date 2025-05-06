from ultralytics import YOLO


if __name__ == '__main__':
    for i in (640, 512, 416):
        model = YOLO('yolov8n.pt') # get pre-trained weights
        model.train(
            data='data.yaml',
            epochs=50,
            imgsz=i,
            batch=8,
            device='cuda',
            name=f'yolov8n_sz_{i}',
            save_dir=f'runs/detect/yolov8n_{i}'
        )

    for i in (640, 512, 416):
        model = YOLO('yolov8s.pt') # get pre-trained weights
        model.train(
            data='data.yaml',
            epochs=50,
            imgsz=i,
            batch=8,
            device='cuda',
            name=f'yolov8s_sz_{i}',
            save_dir=f'runs/detect/yolov8s_{i}'
        )