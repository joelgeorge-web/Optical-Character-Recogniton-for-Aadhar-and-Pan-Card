import easyocr
import cv2
import os

# Initialize the webcam
webcam = cv2.VideoCapture(0)

while True:
    # Read the current frame
    success, frame = webcam.read()
    if not success:
        break

    # Display the frame
    cv2.imshow("Webcam", frame)

    # Check for the Enter key press
    key = cv2.waitKey(1) & 0xFF
    if key == 13:  # 13 is the ASCII code for the Enter key
        # Capture the current frame and save it as an image
        cv2.imwrite(filename='a5.jpg', img=frame)
        print("Photo captured.")
        break

# Release the webcam
webcam.release()
cv2.destroyAllWindows()

image_path = 'a5.jpg'  # Replace with the actual path to your image
img = cv2.imread(image_path)
# Initialize the OCR reader
reader = easyocr.Reader(['en'], gpu=False)  # This needs to run only once to load the model into memory

# Perform OCR on the image
result = reader.readtext(image_path)

# Print the detected text
for detection in result:
    text = detection[1]
    print(text)

# Delete the file
os.remove(image_path)

