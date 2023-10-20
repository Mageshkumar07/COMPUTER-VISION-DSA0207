import cv2
import numpy as np


image = cv2.imread("C:/Users/bsree/OneDrive/Pictures/krishna/mickey.png", cv2.IMREAD_GRAYSCALE)  


edges = cv2.Canny(image, 100, 200) 


cv2.imshow("Original Image", image)
cv2.imshow("Canny Edge Detection", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
