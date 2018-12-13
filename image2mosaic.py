import cv2
from pathlib import Path
import time

IMAGE_PATH = "./image"

def mosaic(src, ratio=0.1):
    small = cv2.recize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

def mosaic_area(src, x, y, width, height, ratio=0.1):
    dst = src.copy()
    dst[y:y + height, x:x+width] = mosaic(dst[y:y + height, x:x + width], ratio)
    return dst

    

