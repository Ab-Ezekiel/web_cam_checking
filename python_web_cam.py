import cv2

# Open the default camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot access webcam")
else:
    print("Webcam is working")

cap.release()
cv2.destroyAllWindows()
