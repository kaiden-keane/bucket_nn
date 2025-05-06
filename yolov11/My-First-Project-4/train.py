from ultralytics import YOLO


if __name__ == '__main__':
    for i in (640, 512, 416):
        model = YOLO('yolo11n.pt') # get pre-trained weights
        model.train(
            data='data.yaml',
            epochs=50,
            imgsz=i,
            batch=8,
            device='cuda',
            name=f'yolo11n_sz_{i}',
            save_dir=f'runs/detect/yolo11n_{i}'
        )

    for i in (640, 512, 416):
        model = YOLO('yolo11s.pt') # get pre-trained weights
        model.train(
            data='data.yaml',
            epochs=50,
            imgsz=i,
            batch=8,
            device='cuda',
            name=f'yolo11s_sz_{i}',
            save_dir=f'runs/detect/yolo11s_{i}'
        )