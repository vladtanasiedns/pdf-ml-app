#!/usr/bin python3
import cv2
import pytesseract
import minilib as mi

img = cv2.imread('page-Sales invoice (Green design).jpg', cv2.IMREAD_GRAYSCALE)

gray_eqlzd = cv2.equalizeHist(img)

cv2.imshow("Result", img)
cv2.waitKey(0)
