import cv2
import numpy as np

image = cv2.imread("joel1.jpg")
img_gray2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh2 = cv2.threshold(img_gray2, 150, 255, cv2.THRESH_BINARY)

contours4, hierarchy4 = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Find the index of the largest contour based on the contour area
largest_contour_index = max(range(len(contours4)), key=lambda i: cv2.contourArea(contours4[i]))

# Get the bounding rectangle of the largest contour
x, y, w, h = cv2.boundingRect(contours4[largest_contour_index])

# Crop the region from the original image using the bounding rectangle coordinates
cropped_image = image[y:y+h, x:x+w]

# Display the cropped image
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
