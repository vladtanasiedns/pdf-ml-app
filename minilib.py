import cv2
import pytesseract


def draw_box_on_chars(img, config=r''):
    """ 
    This function draws boxes around the characters of the read and puts the character by the box 
    """
    boxes = pytesseract.image_to_boxes(img, config)
    imgH, imgW, imgX = img.shape
    for b in boxes.splitlines():
        b = b.split(" ")
        print(b)
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x, imgH - y), (w, imgH - h), (0, 0, 255), 1)
        cv2.putText(img, b[0], (x, imgH-y+25),
                    cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))
    cv2.imshow("Result", img)
    cv2.waitKey(0)


def write_to_file(string):
    """
    Reads writes string to file
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
