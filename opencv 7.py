import cv2
cap = cv2.VideoCapture("C:/Users/bsree/AppData/Local/Packages/5319275A.WhatsAppDesktop_cv1g1gvanyjgm/TempState/7AB4BABDD6B87640E9CCCCF7055324CB/WhatsApp Video 2023-10-16 at 10.23.06_ba374286.mp4")


height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = cap.get(cv2.CAP_PROP_FPS)
path = "C:/Users/bsree/AppData/Local/Packages/5319275A.WhatsAppDesktop_cv1g1gvanyjgm/TempState/7AB4BABDD6B87640E9CCCCF7055324CB/output.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter(path, fourcc, 2,(width, height))
while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("frame", frame)
    output.write(frame)

    if cv2.waitKey(24) & 0xFF==("q"):
        break
cap.release()
output.release()
cv2.destroyAllWindows()

