import cv2
import PIL
from PIL import Image
from collections import Counter
import operator

def capture_image():
    cam = cv2.VideoCapture(0)
    frame = cam.read()[1]
    cam.release()
    return frame


def img_display_processing(image):
    cv2image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(cv2image)
    return img

def required_image(num):
    data = []
    for i in range(num):
        image = capture_image()
        data.append(image)

    return data

def get_emotion_details(arr):
    freq = Counter(arr)
    freq = dict(sorted(freq.items(), key=operator.itemgetter(1),reverse=True))
    num = 0
    for k in freq:
        if(num>=2):
            break
        if(k==2):
            return 'sad'
        if(k==3):
            return 'happy'
        num = num+1;

    return 'neutral'
        

