import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = "C:/Users/Joel/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"
config='--psm 7'

image = cv2.imread("aadhar.jpg")
img_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

ocr_text = pytesseract.image_to_string(img_RGB)

lines = ocr_text.split("\n")
name = ""
aadhar_id = ""

for line in lines:
    if "Name:" in line:
        name = line.split(":")[1].strip()
    elif line.replace(" ", "").isdigit():
        aadhar_id = line

print("Name:", name)
print("Aadhar ID:", aadhar_id)

cv2.imshow("Input", image)
cv2.waitKey(0)
