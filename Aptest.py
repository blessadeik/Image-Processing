import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("Image", image)
cv2.waitKey(0)