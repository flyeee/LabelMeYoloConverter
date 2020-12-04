import os
import cv2
import numpy as np



lable_path = "./result/"
img_path = "./input/"


for file in os.listdir(lable_path):
    if file.endswith(".txt"):
        file_pre_fix = file.split(".")[0]
        img_name = ""
        for img in os.listdir(img_path):
            if img.split(".")[0] == file_pre_fix:
                img_name = img
        img_file = cv2.imread(img_path + img_name)
        img_height, img_width, channels = img_file.shape
        with open(lable_path + file, "r") as f:
            for line in f:
                x = float(line.split(" ")[1]) * img_width
                y = float(line.split(" ")[2]) * img_height
                w = float(line.split(" ")[3]) * img_width
                h = float(line.split(" ")[4]) * img_height
                x1 = int(x - w/2.0)
                x2 = int(x + w/2.0)
                y1 = int(y - h/2.0)
                y2 = int(y + h/2.0)
                color = (255, 0, 0)
                print((x1, y1))
                image = cv2.rectangle(img_file, (x1, y1), (x2, y2), color, 2)
        cv2.imwrite("./verify/"+img_name,image)