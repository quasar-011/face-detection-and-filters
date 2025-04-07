import cv2

def filter(frame, mode):
    if mode == "gray":
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif mode == "blur":
        return cv2.GaussianBlur(frame, (15,15), 0)
    elif mode == "edges":
        return cv2.Canny(frame, 100, 200)
    elif mode == "cartoon":
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(blur,  255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(frame, 9, 300, 300)
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        return cartoon
    return frame

modelFile = "res10_300x300_ssd_iter_140000.caffemodel"
configFile = "deploy.prototxt"
net = cv2.dnn.readNetFromCaffe(configFile, modelFile)

cap = cv2.VideoCapture(0)
mode = None

print("Press: g=Gray | b=Blur | e=edges | c=cartoon | n=none | s=Save | q=Quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0), swapRB=False)
    
    net.setInput(blob)
    detections = net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0,0,i,2]
        if confidence>0.6:
            box=detections[0, 0, i, 3:7] * [w, h, w, h]
            (x1, y1, x2, y2) = box.astype("int")
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    output = filter(frame, mode)
    if mode in ["gray", "edges"]:
        output = cv2.cvtColor(output, cv2.COLOR_GRAY2BGR)

    cv2.imshow("Filtered Facecam (DNN)", output)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('g'):
        mode = "gray"
    elif key == ord('b'):
        mode = "blur"
    elif key == ord('e'):
        mode = "edges"
    elif key == ord('c'):
        mode = "cartoon"
    elif key == ord('n'):
        mode = None
    elif key == ord('s'):
        cv2.imwrite("screenshot.png", ouput)
        print("Screenshot saved!")

cap.release()
cv2.destroyAllWindows()
