import cv2
import matplotlib.pyplot as plt
image=cv2.imread("shinchan.jpg")

image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("image RGB")
plt.show()

gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image,cmap='gray')
plt.title("Grayscale Image")
plt.show()

cropped_img=image[100:300,200:400]
cropped_rgb=cv2.cvtColor(cropped_img,cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("cropped region")
plt.show()