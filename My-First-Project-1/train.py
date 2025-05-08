from ultralytics import YOLO


if __name__ == '__main__':
    for t in ('n', 's', 'm'):
        for i in (640, 512, 416):
            model = YOLO(f'yolo11{t}.pt') # get pre-trained weights
            model.train(
                data='data.yaml',
                epochs=100,
                patience=15,
                imgsz=i,
                batch=-1,
                device='cuda',
                name=f'yolo11{t}_sz_{i}',
                save_dir=f'runs/detect/yolo11{t}_{i}'
            )