import cv2
import numpy as np
image = cv2.imread('C:/Users/bsree/OneDrive/Pictures/krishna/cat.png')
canvas=np.zeros((500,500,3), dtype=np.uint8)
x_offset, y_offset = 100,100
canvas[y_offset:y_offset+ image.shape[0],x_offset:x_offset+ image.shape[1]] = image
cv2.imshow('Moved Image', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

