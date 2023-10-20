import cv2


image = cv2.imread("C:/Users/bsree/OneDrive/Pictures/krishna/home1.png", cv2.IMREAD_GRAYSCALE)

sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  


sobel_y = cv2.convertScaleAbs(sobel_y)

cv2.imshow("Original Image", image)
cv2.imshow("Sobel Y-axis Edge Detection", sobel_y)
cv2.waitKey(0)
cv2.destroyAllWindows()
