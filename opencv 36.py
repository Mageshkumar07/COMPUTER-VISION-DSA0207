import cv2
mickey_cascade = cv2.CascadeClassifier("C:/Users/bsree/OneDrive/Pictures/krishna/mickey.png")
img = cv2.imread("C:/Users/bsree/OneDrive/Pictures/krishna/home1.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mickeys = mickey_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
for (x, y, w, h) in mickeys:
 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('mickeys Detected', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
