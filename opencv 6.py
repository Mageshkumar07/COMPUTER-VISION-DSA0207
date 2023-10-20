import cv2

cap = cv2.VideoCapture("C:/Users/bsree/AppData/Local/Packages/5319275A.WhatsAppDesktop_cv1g1gvanyjgm/TempState/7AB4BABDD6B87640E9CCCCF7055324CB/WhatsApp Video 2023-10-16 at 10.23.06_a7c922a0.mp4")

if not cap.isOpened():
    print("Error opening video file")

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        cv2.imshow('Frame', frame)

        if cv2.waitKey(250) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
