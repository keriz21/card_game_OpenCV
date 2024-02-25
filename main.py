from imgProcessing import img
from imgProcessing import contour4 as ctr

from Game import gameplay as game

import cv2
import time

def main():
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("failed open the camera")
    pass

    counter = 0
    kontur = None
    kartu_text = None

    while True:
        ret, frame = cap.read()

        if not ret:
            print("failed to read frame.")
            break
        filter = img.filter(frame)
        cv2.imshow('filter', filter)

        frame2 = frame.copy()
        frame2 = img.crop_center(frame2)

        kontur,_ = ctr.find_four_sided_contours(filter,frame2,(0,480),True)
        cv2.imshow('kontur', kontur)

        game.mainkan(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()