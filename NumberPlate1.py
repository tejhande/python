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
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = float(w)/h
            if aspect_ratio > 2.0 and aspect_ratio < 4.0:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Create a named window and display the image with detected number plate
cv2.namedWindow('Number plate detection', cv2.WINDOW_NORMAL)
cv2.imshow('Number plate detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
