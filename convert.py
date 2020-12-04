# -*- coding: utf-8 -*-

import os
from os import walk, getcwd
from PIL import Image
import json


def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
    
    
"""-------------------------------------------------------------------""" 

""" Configure Paths"""   
mypath = "./dataset/"
outpath = "./result/"
json_backup ="./json_backup/"

wd = getcwd()
#list_file = open('%s_list.txt'%(wd), 'w')

""" Get input json file list """
json_name_list = []
for file in os.listdir(mypath):
    if file.endswith(".json"):
        json_name_list.append(file)
    

""" Process """
for json_name in json_name_list:
    txt_name = json_name.rstrip(".json") + ".txt"
    """ Open input text files """
    txt_path = mypath + json_name
    print("Input:" + txt_path)
    txt_file = open(txt_path, "r")
    
    """ Open output text files """
    txt_outpath = outpath + txt_name
    print("Output:" + txt_outpath)
    txt_outfile = open(txt_outpath, "a")
    print(mypath+json_name)
    """ Convert the data to YOLO format """
    with open(mypath+json_name) as f:
        img_data = json.load(f)
        pt = img_data['shapes'][0]['points']
        print(pt)
        xmin = min(pt[0][0], pt[1][0])
        xmax = max(pt[0][0],pt[1][0])
        ymin = min(pt[0][1],pt[1][1])
        ymax = max(pt[0][1],pt[1][1])

        w = img_data['imageWidth']
        h = img_data['imageHeight']

        print(w, h)
        print(xmin, xmax, ymin, ymax)
        b = (xmin, xmax, ymin, ymax)
        bb = convert((w,h), b)
        print(bb)
        txt_outfile.write("0" + " " + " ".join([str(a) for a in bb]) + '\n')

    # os.rename(txt_path,json_backup+json_name)

