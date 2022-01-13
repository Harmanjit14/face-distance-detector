import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import numpy as np

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector()

text = ['Hello there.', 'My Name is Harman', 'I am bored!']

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)
    txt = np.zeros_like(img)
    if faces:
        face = faces[0]

        left_pupil = face[145]
        right_pupil = face[374]

        # cv2.circle(img, left_pupil, 2,  (255, 0, 255), cv2.FILLED)
        # cv2.circle(img, right_pupil, 2,  (255, 0, 255), cv2.FILLED)
        # cv2.line(img, left_pupil, right_pupil, (255, 0, 255), 1)

        w, _info, _image = detector.findDistance(
            left_pupil, right_pupil, img)

        W = 6.3

        f = 600
        D = W*f/w

        for i, t in enumerate(text):
            top_padding = 20 + int(D/2)
            scale = 0.4+D/50

            cv2.putText(txt, t, (50, 50+(i*top_padding)),
                        cv2.FONT_HERSHEY_PLAIN, scale, (255, 255, 255), 2)

        cvzone.putTextRect(
            img, f'Distance {int(D)} cm', (face[10][0]-100, face[10][1]-20), 2, 3)

        stack = cvzone.stackImages([img, txt], 2, 1)
        cv2.imshow("Image", stack)
        cv2.waitKey(1)
