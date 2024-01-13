import cv2
import numpy as np

# Load the image
img = cv2.imread('image.jpg')

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply filters to enhance edges
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 100, 200)

# Find contours of objects in the image
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through contours and filter for possible number plates
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 1000:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# # Display the image with detected number plate
# cv2.imshow('Number plate detection', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.namedWindow('Number plate detection', cv2.WINDOW_NORMAL)
cv2.imshow('Number plate detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
