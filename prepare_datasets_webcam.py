'''This file is used to prepare training data by taking pictures frame by frame from the webcam'''

import cv2
import os

def prepare_dataset():
    i = 0

    myname = input('enter your name: ')
    cam = cv2.VideoCapture(0)

    while True:
        ret, im = cam.read()
        i = i + 1
        classpath = os.path.join('datasets','mydata','raw',myname)
        if not os.path.exists(classpath):
            os.mkdir(classpath)
        cv2.imwrite(os.path.join(classpath, str(myname) + str(i) + ".jpg"), im)
        if i > 50:
            cam.release()
            cv2.destroyAllWindows()
            break


if __name__== "__main__":
    prepare_dataset()