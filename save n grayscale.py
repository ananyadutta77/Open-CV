import cv2
image=cv2.imread("shinchan.jpg")
gray_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
resized_img=cv2.resize(gray_img,(240,240))
cv2.imshow("Processed Image",resized_img)
key=cv2.waitKey(0)
#ASCII check
if key==ord('s'):
    cv2.imwrite("grayscale_resizedimg.jpg",resized_img)
    print("image saved as 'grayscale_resizedimg.jpg'")
else:
    print("image is not saved")   
cv2.destroyAllWindows()
print(f"image dimensions: {image.shape}")     
