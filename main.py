#!/usr/bin python3
import cv2
import minilib as mi
import sys
import os

cwd = os.getcwd()+"/input/"
output = os.getcwd()+"/output/"

for file in os.listdir(cwd):
    file_path = cwd + file
    mi.convert_pdf_to_image(file_path, output, file)
