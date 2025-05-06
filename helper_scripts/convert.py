import os
import json

image_width = 1920
image_height = 1080
input_dir = "imagesmay_3_buckets_labelled_updated"
output_dir = "training"
os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(input_dir):
    if not file.endswith(".label"):
        continue
    
    with open(os.path.join(input_dir, file), 'r') as f:
        boxes = json.load(f)
    
    yolo_lines = []
    for box in boxes:
        class_id = 0  # "orange" only
        x_center = (box['x'] + box['x'] / 2) / image_width
        y_center = (box['y'] + box['y'] / 2) / image_height
        w = box['width'] / image_width
        h = box['height'] / image_height

        if x_center > 1: x_center=1
        elif x_center < 0: x_center=0

        if y_center > 1: y_center=1
        elif y_center < 0: y_center=0

        if w > 1: w=1
        elif w < 0: w=0

        if h > 1: h=1
        elif h < 0: h=0

        yolo_lines.append(f"{class_id} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}")
    
    output_filename = os.path.splitext(file)[0] + ".txt"
    with open(os.path.join(output_dir, output_filename), 'w') as f:
        f.write("\n".join(yolo_lines))