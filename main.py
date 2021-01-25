#!/usr/bin python3
import cv2
import minilib as mi
import pytesseract
import re
import os

cwd = os.getcwd()+"/input/"
output = os.getcwd()+"/output/"

# for file in os.listdir(cwd):
#     file_path = cwd + file
#     mi.convert_pdf_to_image(file_path, output, file)


image_data = pytesseract.image_to_string(
    "./output/101-YYY-LLC.pdf.jpg0001-1.jpg")

print(image_data)

# Extract invoice data from the invoice_data variable using regex
# - Extract invoice number
invoice_number = re.search("Invoice # [\d]*", image_data)
print(invoice_number.group(0))


# - Extract invoice date
# - Extract invoice total
