import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread("shinchan.jpg")

#rotate 45 degrees around center
(h,w)=image.shape[:2]
center=(w//2,h//2)
M=cv2.getRotationMatrix2D(center,45,1.0)
rotated=cv2.warpAffine(image,M,(w,h))
rotated_rgb=cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("rotated image")
plt.show()
