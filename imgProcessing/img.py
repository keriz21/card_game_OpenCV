import cv2
import numpy as np

def crop_center(frame, percent=75):
    height, width, _ = frame.shape
    crop_percent = percent / 100.0

    new_width = int(width * crop_percent)
    new_height = int(height * crop_percent)

    start_x = (width - new_width) // 2
    start_y = (height - new_height) // 2

    cropped_frame = frame[start_y:start_y + new_height, start_x:start_x + new_width]

    return cropped_frame

def enhance_color_strength(image, saturation_factor=2.0, white_boost_factor=1.5):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] * saturation_factor, 0, 255).astype(np.uint8)

    hsv_image[:, :, 2] = np.clip(hsv_image[:, :, 2] * white_boost_factor, 0, 255).astype(np.uint8)

    enhanced_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    return enhanced_image

def thresh_binary(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)
    
    kernel = np.ones((5, 5), np.uint8)

    thresholded = cv2.morphologyEx(thresholded,cv2.MORPH_OPEN, kernel)
    return thresholded

def smooth_edges(image):
    # Erosion untuk mengurangi ketebalan garis
    kernel = np.ones((5, 5), np.uint8)
    eroded = cv2.erode(image, kernel, iterations=1)

    # Dilasi untuk memperhalus garis
    dilated = cv2.dilate(eroded, kernel, iterations=1)

    return dilated

def filter(frame):
    crop = crop_center(frame)
    enhance = enhance_color_strength(crop)
    thresh = thresh_binary(enhance)
    smooth = smooth_edges(thresh)

    return smooth