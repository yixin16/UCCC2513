from urllib.request import urlretrieve
import cv2 as cv

def download_save_image(url, filename):
    """docstring"""
    urlretrieve(url, filename)

def display_images(images, titiles):
    for img, title in zip(images, titiles):
        cv.imshow(title, img)
    
    cv.waitKey(0)
    cv.destroyAllWindows()