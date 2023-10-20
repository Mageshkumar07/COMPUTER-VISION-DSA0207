import cv2


image = cv2.imread("C:/Users/bsree/OneDrive/Pictures/krishna/mickey.png", cv2.IMREAD_GRAYSCALE)


sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  


sobel_x = cv2.convertScaleAbs(sobel_x)


cv2.imshow("Original Image", image)
cv2.imshow("Sobel X-axis Edge Detection", sobel_x)
cv2.waitKey(0)
cv2.destroyAllWindows()
