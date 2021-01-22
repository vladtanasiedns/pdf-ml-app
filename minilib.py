import cv2
import pytesseract
from pdf2image import convert_from_path
import PyPDF2 as pdf


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


def write_string_to_file(string):
    """
    Writes string to file
    """
    with open("output.txt", "w") as f:
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


def convert_pdf_to_image(pdf_path, output_folder):
    """
    Converting a pdf file to jpeg image
    and saving the file to root path or specified path
    """
    doc = pdf.PdfFileReader(pdf_path)
    title = doc.getDocumentInfo()['/Title']
    image = convert_from_path(
        pdf_path, output_folder=output_folder, fmt="jpeg", output_file=f"{title}.jpg")
