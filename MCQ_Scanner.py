import cv2
import xlsxwriter
import pytesseract
import re
import os
import fnmatch
import sys

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
outWorkbook = xlsxwriter.Workbook("OUTPUT EXCEL FILE PATH")
outSheet = outWorkbook.add_worksheet()


def image_processing(file_path):
    # Remove old png
    for filename in os.listdir():
        if filename.endswith(".png"):
            os.remove(filename)

    # Load image, grayscale, Gaussian blur, adaptive threshold
    image = cv2.imread(file_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 30)
    # Dilate to combine adjacent text contours
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
    dilate = cv2.dilate(thresh, kernel, iterations=2)
    # Find contours, highlight text areas, and extract ROIs
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    ROI_number = 0
    for c in cnts:
        area = cv2.contourArea(c)
        if area > 1000:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 2)
            ROI = image[y:y + h, x:x + w]
            cv2.imwrite('ROI_{}.png'.format(ROI_number), ROI)
            ROI_number += 1

    #cv2.imshow('image', image)
    #cv2.imshow('dilate', dilate)
    #cv2.imshow('thresh', thresh)
    #cv2.waitKey()

    # This part if for 10 questions in one image

    #number_of_png = len(fnmatch.filter(os.listdir(), '*.png'))
    #print("Number of Images :", number_of_png)

    #if number_of_png != 20:
       # sys.exit('Error handling: Expected 20 processed images')  # An error in the image processing must output
        # ROI_0 to ROI_19 images if not check the processed images in your directory


def extract_q(filename_q):  # Extracts the Questions
    global q
    quest = cv2.imread(filename_q, 0)
    custom_config = r'--oem 3 --psm 6'
    q = pytesseract.image_to_string(quest, config=custom_config, lang='eng')
    print(q)
    return q


def extract_c(filename_c):  # Extracts the Choices
    global new_text
    choices = cv2.imread(filename_c, 0)
    custom_config = r'--oem 3 --psm 6'
    c = pytesseract.image_to_string(choices, config=custom_config, lang='eng')

    x = re.sub(r'\n{2}', '\n', c)
    text = repr(x)
    new_text = text.split("\\n")
    print(text)
    return new_text


def encode_qc(position_excel):  # Encodes in Excel

    for QuItems1 in range(len(q)):
        outSheet.write(position_excel, 0, q)

    for QuItems2 in range(len(new_text)):
        outSheet.write(position_excel, QuItems2 + 1, new_text[QuItems2])


# Processing Everything - See the original template for the images
# C:\Users\Intel\Documents\MCQ_Scanner\Sample Images SAMPLE FILE PATH
image_processing("IMAGE FILE PATH")
excelQ = ( "ROI_1.png" , "ROI_3.png" ,"ROI_5.png" , "ROI_7.png", "ROI_9.png")
excelC = ("ROI_0.png" ,  "ROI_2.png", "ROI_4.png", "ROI_6.png", "ROI_8.png")
position = (5, 4, 3, 2, 1)
for Quest, Choi, Pos in zip(excelQ, excelC, position):
    extract_q(Quest)
    extract_c(Choi)
    encode_qc(Pos)

outWorkbook.close()
