#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=C0103
# pylint: disable=E1101

import sys
import time
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import cv2

import kappa.face_detection.utils.label_map_util as label_map_util
import kappa.face_detection.utils.visualization_utils_color as vis_util

# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_CKPT = 'res/face_detection/model/frozen_inference_graph_face.pb'

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = 'src/kappa/face_detection/protos/face_label_map.pbtxt'

NUM_CLASSES = 2

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

class TensoflowFaceDector(object):
    def __init__(self):
        """Tensorflow detector
        """

        self.detection_graph = tf.Graph()
        with self.detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')


        with self.detection_graph.as_default():
            config = tf.ConfigProto()
            config.gpu_options.allow_growth = True
            self.sess = tf.Session(graph=self.detection_graph, config=config)
            self.windowNotSet = True


    def run(self, image):
        """image: bgr image
        return (boxes, scores, classes, num_detections)
        """

        image_np = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # the array based representation of the image will be used later in order to prepare the
        # result image with boxes and labels on it.
        # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
        image_np_expanded = np.expand_dims(image_np, axis=0)
        image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
        # Each box represents a part of the image where a particular object was detected.
        boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')
        # Each score represent how level of confidence for each of the objects.
        # Score is shown on the result image, together with the class label.
        scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
        classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
        num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')
        # Current detection.
        start_time = time.time()
        (boxes, scores, classes, num_detections) = self.sess.run(
            [boxes, scores, classes, num_detections],
            feed_dict={image_tensor: image_np_expanded})
        elapsed_time = time.time() - start_time
        print('inference time cost: {}'.format(elapsed_time))

        return (boxes, scores, classes, num_detections)



    def getBoxes(self,imagePath):

        #coordinates of a box are ymin,xmin,ymax,xmax
        #in order to have normalized coordinates, you have to do
        # left : xmin * image_width
        # right : xmax * image_width
        # top : ymin * image_height
        # bottom : ymax * image_height

        boxesToPrint=[]
        image = cv2.imread(imagePath)
        [h, w] = image.shape[:2]
        (boxes, scores, classes, num_detections) = self.run(image)
        i = 0

        while scores[0][i] > 0.45:
            boxesToPrint.append(boxes[0][i])
            i += 1

        return boxesToPrint






if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print ("usage:%s (input filename)[output filename] Detect faces\
 in the image"%(sys.argv[0]))
        exit(1)

    tDetector = TensoflowFaceDector()
    image = cv2.imread(sys.argv[1])

    [h, w] = image.shape[:2]
    print (h, w)
    #image = cv2.resize(image, (0,0), fx=2, fy=2)
    #image = cv2.flip(image, 1)

    (boxes, scores, classes, num_detections) = tDetector.run(image)
    i = 0
    #coordinates of a box are ymin,xmin,ymax,xmax
    #in order to have normalized coordinates, you have to do
    # left : xmin * image_width
    # right : xmax * image_width
    # top : ymin * image_height
    # bottom : ymax * image_height
    boxesToPrint = []
    while scores[0][i] > 0.45:
        print(scores[0][i])
        boxesToPrint.append(boxes[0][i])
        i += 1

    print(boxesToPrint)
    vis_util.visualize_boxes_and_labels_on_image_array(
        image,
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        category_index,
        use_normalized_coordinates=True,
        line_thickness=4)
    cv2.namedWindow("tensorflow based (%d, %d)" % (w, h), cv2.WINDOW_NORMAL)
    cv2.imshow("tensorflow based (%d, %d)" % (w, h), image)
    if len(sys.argv) == 3:
        cv2.imwrite(sys.argv[2],image)
    cv2.waitKey(0)
