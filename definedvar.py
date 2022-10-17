import numpy as np
import cv2


## Defining the translate function to enable easier calls

def translate(catImage, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    moved = cv2.warpAffine(catImage, M, (catImage.shape[1], catImage.shape[0]))
    return moved

# Defining the rotate function
def rotate(catImage, angle, center = None, scale = 1.0): (h, w) = catImage.shape[:2]

    if center is None:
        center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(catImage, M, (w, h))
    return rotated