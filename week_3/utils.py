from urllib.request import urlretrieve
import cv2 as cv
import time

def download_save_image(url, filename):
    """docstring"""
    urlretrieve(url, filename)

def display_images(images, titiles):
    for img, title in zip(images, titiles):
        cv.imshow(title, img)
    
    cv.waitKey(0)
    cv.destroyAllWindows()
    
def image_resize(img, fx, fy, interpolation):
    startTime = time.time()
    resized_image = cv.resize(img, None, fx=fx, fy=fy, interpolation=interpolation)
    endTime = time.time()
    return resized_image, endTime - startTime