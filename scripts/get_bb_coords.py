import json
import cv2
from pprint import pprint
import numpy as np
# images =[]
with open("../bbs/bbs.json",'r') as fl:
	data = json.load(fl)
	for img_no,image in enumerate(data):
		img = cv2.imread('../images/'+str(img_no)+'.jpg',1)
		s = '1'
		for box_no,box in enumerate(image):
			try:
				x,y = box[0]
				h = box[-1][1] - y
				w = box[1][0] - x
				x,y,h,w = int(x),int(y),int(h),int(w)
				s = s + '\n' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h)
			except:
				print("Exception encountered ! -*-")
				pass
		print(img_no)
		f = open('../annotations/'+str(img_no)+'.txt','w+')
		f.write(s)
		f.close()


'''
images = np.array(images)
images = np.reshape(images,(951,128,128,1))
pprint (images.shape)
'''
