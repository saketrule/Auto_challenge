import json
import cv2
from pprint import pprint
import numpy as np
# images =[]
with open("../bbs/bbs.json",'r') as fl:
	data = json.load(fl)
	for img_no,image in enumerate(data):
		img = cv2.imread('../images/'+str(img_no)+'.jpg',1)
		img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		for box_no,box in enumerate(image):
			try:
				x,y = box[0]
				h = box[-1][1] - y
				w = box[1][0] - x
				crop = img[int(y):int(y)+int(h),int(x):int(x)+int(w)]
				rsz = cv2.resize(crop,(128,128), interpolation = cv2.INTER_AREA)
				cv2.imwrite('../processed_auto/'+str(img_no)+'_'+str(box_no)+'.jpg',rsz)
				print("GOt: "+str(img_no))
				#rsz = np.array(rsz,dtype='float32')
				#normalizedImg = np.zeros((128, 128),dtype='float32')
				#print normalizedImg.dtype
				#normalizedImg = cv2.normalize(rsz,  normalizedImg, 0, 1, cv2.NORM_MINMAX)
				#images.append(normalizedImg)
			except:
				print("Exception encountered ! -*-")
				pass

'''
images = np.array(images)
images = np.reshape(images,(951,128,128,1))
pprint (images.shape)
'''
