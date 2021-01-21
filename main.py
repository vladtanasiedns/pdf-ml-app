#!/usr/bin python3
import cv2
import pytesseract
import minilib as mi

img = cv2.imread("factura.jpg")
string = pytesseract.image_to_string(img)
mi.write_to_file(string)
