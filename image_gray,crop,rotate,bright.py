import cv2
import matplotlib.pyplot as plt
import numpy as np
image=cv2.imread("pisa.jpg")
#og img
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("original image")
plt.show()
#gray img
gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image,cmap='gray')
plt.title("Grayscale Image")
plt.show()
#cropped img
cropped_img=image[200:1400,300:900]
cropped_rgb=cv2.cvtColor(cropped_img,cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("cropped region")
plt.show()
#rotated img
(h,w)=image.shape[:2]
center=(w//2,h//2)
M=cv2.getRotationMatrix2D(center,6,1.0)
rotated=cv2.warpAffine(image,M,(w,h))
rotated_rgb=cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("rotated image")
plt.show()
#brightened img
matrix=np.ones(image.shape,dtype='uint8')*50
brighter=cv2.add(image,matrix)
brighter_rgb=cv2.cvtColor(brighter,cv2.COLOR_BGR2RGB) 
plt.imshow(brighter_rgb)
plt.title("brightened image")
plt.show()