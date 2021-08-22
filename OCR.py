import numpy as np
import cv2
import pytesseract
import os
import matplotlib.pyplot as plt
import math
import time



def getTextfromImage(img_rgb):
    data = pytesseract.image_to_string(img_rgb, lang="ind")
    return data

def clearUnusedChar(string):
    res = ""
    for i in string:
        if i == "\n":
            res += "<br><br>"
        else:
            res += i
    return res

def doOCR(ImagePath):
    pathIm = os.path.join(os.getcwd(), ImagePath)
    start = time.time()
    im_rgb = cv2.imread(pathIm)
    im_rgb = cv2.cvtColor(im_rgb, cv2.COLOR_BGR2RGB)
    ## (2) Threshold
    th, im_gray = cv2.threshold(im_rgb, 127, 255, cv2.THRESH_TRUNC)
    try:
        res = clearUnusedChar(getTextfromImage(im_gray));
        print(res);
        end = time.time()
        return {
            "text" : res,
            "status" : 200,
            "msg" : "success do ocr",
            'operation_time' : end - start
        }
    except Exception as e:
        end = time.time()
        return {
            "text" : "",
            "status" : 500,
            "msg" : e,
            'operation_time' : end - start
        }

