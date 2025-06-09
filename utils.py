import cv2
import numpy as np

def region_of_interest(img):
    height, width = img.shape
    mask = np.zeros_like(img)
    polygon = np.array([[(
        int(0.3 * width), int(0.69 * height)),
        (int(0.54 * width), int(0.435 * height)),
        (int(0.59 * width), int(0.435 * height)),
        (int(1.37 * width), int(0.68 * height))
    ]], np.int32)
    cv2.fillPoly(mask, [polygon], 255)
    return cv2.bitwise_and(img, mask)
