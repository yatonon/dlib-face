#!/usr/bin/python
import os
import sys
import glob
import re
import shutil
import dlib
from skimage import io

if len(sys.argv) != 2:
    exit()
faces_folder = sys.argv[1]

detector = dlib.simple_object_detector("detector.svm")

win_det = dlib.image_window()
win_det.set_image(detector)

print("Showing detections on the images in the faces folder...")
win = dlib.image_window()
for f in glob.glob(os.path.join(faces_folder, "*.jpg")):
    print("Processing file: {}".format(f))
    img = io.imread(f)
    dets = detector(img)
    print("Number of faces detected: {}".format(len(dets)))
    for k, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            k, d.left(), d.top(), d.right(), d.bottom()))

    win.clear_overlay()
    win.set_image(img)
    win.add_overlay(dets)

    filename = re.search('([^/]+?)?$' , f)
    num = 0
    while num < 1:
        print("it's correct? y/n if y, I will learn this image.")
        answer = input('>> ')

        if answer == 'y':
            datasets = []
            for k, d in enumerate(dets):
                datasets.append("<box top=\'{}\' left=\'{}\' width=\'{}\' height=\'{}\'/>".format(
                d.top(), d.left(), d.right()-d.left(), d.bottom()-d.top()))

            with open('./learning/mydataset.xml') as f:
                l = f.readlines()
                l.insert(6,'<image file=\''+filename.group()+'\'>\n')
                l.insert(7,'</image>\n')
                for index, item in enumerate(datasets):
                    print("インデックス：" + str(index) + ", 値：" + item)
                    l.insert(index+7, item+'\n')

            with open('./learning/mydataset.xml', mode='w') as f:
                f.writelines(l)

            shutil.copyfile("./test/"+filename.group(), "./learning/"+filename.group())
            num = 1

        elif answer == 'n':
            print('ok,this image isn\'t learning.')
            num = 1
        else:
            print('you should tap y or n.')

        dlib.hit_enter_to_continue()
