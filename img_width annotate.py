import cv2
import matplotlib.pyplot as plt
#step 1 : load the img
image_path="shinchan.jpg"
image=cv2.imread(image_path)
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
height,width,_=image_rgb.shape

arrow_start=(20,height-50) #near topright
arrow_end=(width-20,height-50)
cv2.arrowedLine(image_rgb,arrow_start,arrow_end,(255,255,0),3,tipLength=0.05) #downward arrow
cv2.arrowedLine(image_rgb,arrow_end,arrow_start,(255,255,0),3,tipLength=0.05) #upward arrow

plt.figure(figsize=(12,8))
plt.imshow(image_rgb)
plt.title("annotated img with bi-directional width arrow")
plt.axis("off")
plt.show()