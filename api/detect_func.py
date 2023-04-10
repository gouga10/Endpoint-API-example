'''This script detects if a person is drowsy or not,using dlib and eye aspect ratio
calculations. Uses an image file as input.'''

#Import necessary libraries
from scipy.spatial import distance
from imutils import face_utils
import numpy as np

import dlib
import cv2
def model(image_path):

    image=cv2.imread(image_path)
    detector = dlib.get_frontal_face_detector()

    faces = detector(image, 0)
    if faces:
        print(str(len(faces)))
        return str(len(faces))
    else:
        print('noooooooo')
        return '0'


