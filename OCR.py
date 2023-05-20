import cv2
import pytesseract
import numpy as np
import matplotlib.pyplot as plt



pytesseract.pytesseract.tesseract_cmd = "C:/Users/Joel/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"

# Path to the debit card image
image_path = "atm.jpg"  # Replace with the actual image path

# Load the image
image = cv2.imread(image_path)


# Function to preprocess the image before OCR
def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return thresholded

# Function to extract numbers from an image region
def extract_numbers(image):
    extracted_numbers = pytesseract.image_to_string(image, config='--psm 6 digits')
    return extracted_numbers

# Function to extract text (name) from an image region
def extract_text(image):
    extracted_text = pytesseract.image_to_string(image, config='--psm 7')
    return extracted_text


# Preprocess the image
preprocessed_image = preprocess_image(image)


# Specify the regions of interest coordinates
numbers_roi = preprocessed_image[285:330, 88:712]
text_roi = preprocessed_image[412:440, 77:397]
# Extract the numbers from numbers_roi
numbers = extract_numbers(numbers_roi)

# Extract the text from text_roi
text = extract_text(text_roi)

# Print the extracted numbers and text
print("Extracted Numbers:")
print(numbers)

print("Extracted Text:")
print(text)
