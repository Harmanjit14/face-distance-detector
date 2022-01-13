import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector()

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]

        left_pupil = face[145]
        right_pupil = face[374]

        cv2.circle(img, left_pupil, 5,  (255, 0, 255), cv2.FILLED)
        cv2.circle(img, right_pupil, 5,  (255, 0, 255), cv2.FILLED)
        cv2.line(img, left_pupil, right_pupil, (255, 0, 255), 1)

        w, _info, _image = detector.findDistance(
            left_pupil, right_pupil, img)

        W = 6.3

        f = 600
        D = W*f/w

        cvzone.putTextRect(
            img, f'Distance from PC {D} cm', (face[10][0], face[10][1]), 1, 1)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
