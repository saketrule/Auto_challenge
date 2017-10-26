import json
import cv2
from pprint import pprint
import numpy as np
from random import randint

def intersect(p1,p2):
    if p1[1]<p2[0] or p1[0]>p2[1]:
        print("got false")
        return False
    else:
        return True
with open("../bbs/bbs.json",'r') as fl:
    data = json.load(fl)
    for img_no,image in enumerate(data):
        img = cv2.imread('../images/'+str(img_no)+'.jpg',1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        height,width = img.shape
        cnt = 0
        trial = 0
        while cnt<3 and trial<20:
            trial += 1
            y1,x1 = randint(0,height),randint(0,width)
            y2,x2 = (50+y1+randint(0,height-y1)),(50+x1+randint(0,width-x1))
            works = True
            for box_no,box in enumerate(image):
                bx1,by1 = box[0]
                bx2,by2 = box[2]
                if intersect((bx1,bx2),(x1,x2)) and intersect((by1,by2),(y1,y2)):
                    works = False
                    break
            if works:
                try:
                    crop = img[y1:y2,x1:x2]
                    rsz = cv2.resize(crop,(128,128),interpolation = cv2.INTER_AREA)
                    cv2.imwrite('../processed_false/'+str(img_no)+'_'+str(cnt)+'.jpg',rsz)
                    cnt += 1
                    print(img_no,"---",x1,y1,x2,y2)
                except:
                    pass
