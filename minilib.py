import cv2
import pytesseract
from pdf2image import convert_from_path
import PyPDF2 as pdf
import re
import csv
import os


def draw_box_on_chars(img):
    """ 
    This function draws boxes around the characters of the read and puts the character by the box 
    """
    boxes = pytesseract.image_to_boxes(img)
    imgH, imgW, imgC = img.shape
    for b in boxes.splitlines():
        b = b.split(" ")
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x, imgH - y), (w, imgH - h), (0, 0, 255), 1)
    cv2.imshow("Result", img)
    cv2.waitKey(0)


def write_string_to_file(string, file_name):
    """
    Writes string to file
    """
    with open(file_name, "w") as f:
        f.write(string)


def draw_boxes_on_data(img, config=r''):
    """
    Drawing boxes based on data extracted from the image parsing as data
    Config is used to set the tesseract engine or the type of characters to look for
    """
    data = pytesseract.image_to_data(img, config=config)
    for x, b in enumerate(data.splitlines()):
        if x != 0:
            b = b.split()
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 1)
                cv2.putText(img, b[11], (x, y),
                            cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))
    cv2.imshow("Result", img)
    cv2.waitKey(0)


def convert_pdf_to_image(pdf_path, output_folder, file_name):
    """
    Converting a pdf file to jpeg image
    and saving the file to root path or specified path
    """
    image = convert_from_path(
        pdf_path, output_folder=output_folder, fmt="jpeg", output_file=f"{file_name}.jpg")


def extract_invoice_data(invoice_image_path, csv_file):
    """
    Extract inv number, date and total from invoice as image
    Writes data to csv file provided in format Number, Date, Total
    """
    # Extract image data to string
    image_data = pytesseract.image_to_string(invoice_image_path)

    # - Extract invoice number
    invoice_number = re.search("Invoice # [\d].*", image_data)
    number = invoice_number.group(0).split()[2]

    # - Extract invoice date
    invoice_date = re.search("Invoice Date [\d].*", image_data)
    date = invoice_date.group(0).split()[2]

    # - Extract invoice total
    invoice_total = re.search("TOTAL [a-z]* [\d].*", image_data)
    total = invoice_total.group(0).split()[2]

    # Write image data to csv
    with open(csv_file, "a", newline='') as file:
        writer = csv.writer(file)

        if os.path.getsize(csv_file) == 0:
            writer.writerow(["Number", "Date", "Total"])

        writer.writerow([number, date, total])
