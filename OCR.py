import cv2
import pytesseract
import numpy as np
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = "C:/Users/Joel/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"
image_type = input("Enter the file name of the card: ")
image_path = image_type + ".jpg"

print("\n")

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return thresholded

def extract_numbers(image):
    extracted_numbers = pytesseract.image_to_string(image, config='--psm 6 digits')
    return extracted_numbers

def extract_text(image):
    extracted_text = pytesseract.image_to_string(image, config='--psm 7')
    return extracted_text

image = cv2.imread(image_path)
preprocessed_image = preprocess_image(image)

def process_aadhar_card(image_path):
    
    numbers_roi = preprocessed_image[370:410, 260:560]
    text_roi = preprocessed_image[160:195, 270:427]
    
    numbers = extract_numbers(numbers_roi)
    text = extract_text(text_roi)
    
    return numbers, text

def process_atm_card(image_path):
    
    numbers_roi = preprocessed_image[285:330, 88:712]
    text_roi = preprocessed_image[412:440, 77:397]
    
    numbers = extract_numbers(numbers_roi)
    text = extract_text(text_roi)
    
    return numbers, text

def process_pan_card(image_path):
    
    numbers_roi = preprocessed_image[324:351, 38:216]
    text_roi = preprocessed_image[214:245, 272:518]
    
    numbers = extract_text(numbers_roi)
    text = extract_text(text_roi)
    
    return numbers, text

# Process Aadhar Card
aadhar_numbers, aadhar_text = process_aadhar_card(image_path)
atm_numbers, atm_text = process_atm_card(image_path)
pan_name, pan_text = process_pan_card(image_path)
if len(aadhar_numbers) == 13:
    print("AADHAR CARD\n")
    print("NAME:", aadhar_text)
    print("Aadhar Number:", aadhar_numbers)

elif len(atm_numbers) > 14:
    print("ATM CARD\n")
    print("NAME:", atm_text)
    print("CARD NUMBER:", atm_numbers)

else:
    print("PAN CARD\n")
    print("NAME:", pan_name)
    print("PAN ID:", pan_text)