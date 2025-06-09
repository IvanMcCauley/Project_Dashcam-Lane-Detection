import cv2
import numpy as np

def region_of_interest(img):
    # Get image dimensions
    height, width = img.shape
    # Create a blank mask the same size as the image
    mask = np.zeros_like(img)

    # Define the polygon that covers the lane area
    polygon = np.array([[
        (int(0.3 * width), int(0.69 * height)),     # Bottom-left
        (int(0.54 * width), int(0.435 * height)),   # Top-left
        (int(0.59 * width), int(0.435 * height)),   # Top-right
        (int(1.37 * width), int(0.68 * height))     # Bottom-right (extends beyond width for full coverage)
    ]], np.int32)

    # Fill the polygon with white (255) on the mask
    cv2.fillPoly(mask, [polygon], 255)
    # Apply the mask to the input image using bitwise AND
    return cv2.bitwise_and(img, mask)