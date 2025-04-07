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
        edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(frame, 9, 300, 300)
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        return cartoon
    return frame

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
mode = None 
print("Press: g=Gray | b=Blur | e=Edges | c=Cartoon | n=None | s=Save | q=Quit")


while True:
    ret, frame = cap.read()
    if not ret:
        break

    faces = face_cascade.detectMultiScale(frame, 1.1, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

    output = filter(frame, mode)
    if mode == "gray" or mode == "edges":
        output = cv2.cvtColor(output, cv2.COLOR_GRAY2BGR)

    cv2.imshow("Filtered FaceCam", output)

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
        mode = "None"
    elif key == ord('s'):
        cv2.imwrite("screenshot.png", output)
        print("Screenshot saved!")

cap.release()
cv2.destroyAllWindows()
