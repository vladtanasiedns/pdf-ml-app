#!/usr/bin python3

import minilib as mi
import os

cwd = os.getcwd()+"/input/"
output = os.getcwd()+"/output/"

for file in os.listdir(cwd):
    file_path = cwd + file
    mi.convert_pdf_to_image(file_path, output, file)

for file in os.listdir(output):
    file_path = output + file
    mi.extract_invoice_data(file_path, "invoice_data.csv")
