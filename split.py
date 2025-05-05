import os
import random
import shutil

imgs_dir = 'images'
label_dir = 'labels2'


image_files = [ f for f in os.listdir(imgs_dir) if f.endswith(".jpg") ]

random.shuffle(image_files)
print(image_files)
split_ratio = 0.8

split_idx = int(len(image_files) * split_ratio)
train_files = image_files[:split_idx]
val_files = image_files[split_idx:]

os.makedirs("dataset", exist_ok=True)
os.makedirs(os.path.join("dataset", "train"), exist_ok=True)
os.makedirs(os.path.join("dataset", "val"), exist_ok=True)

train_img_dir = os.path.join('dataset', 'train', 'images')
train_label_dir = os.path.join('dataset', 'train', 'labels')
os.mkdir(train_img_dir)
os.mkdir(train_label_dir)

val_img_dir = os.path.join('dataset', 'val', 'images')
val_label_dir = os.path.join('dataset', 'val', 'labels')
os.mkdir(val_img_dir)
os.mkdir(val_label_dir)

def move_files(files_list, img_dst, label_dst):
    for file in files_list:
        name = file.split(".")[0]
        
        img = os.path.join(imgs_dir, name + ".jpg")
        label = os.path.join(label_dir, name + ".txt")
        
        shutil.copy(img, os.path.join(img_dst, name + ".jpg"))
        shutil.copy(label, os.path.join(label_dst, name + ".txt"))

        

move_files(train_files, train_img_dir, train_label_dir)
move_files(val_files, val_img_dir, val_label_dir)