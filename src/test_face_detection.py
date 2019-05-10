from kappa.face_detection.inference_image_face import *
import os
if __name__ == "__main__":
    tDetector = TensorflowFaceDetector()
    boxes = tDetector.getBoxes("res/images/face_detection/onestpastoutseul.jpg")
