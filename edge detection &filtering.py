import cv2
import numpy as np
import matplotlib.pyplot as plt
def display_image(title,image):
    """utility function to display an img"""
    plt.figure(figsize=(8,8))
    if len(image.shape)==2:
        plt.imshow(image,cmap="gray")
    else:
        plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))    
    plt.title(title)
    plt.axis('off')
    plt.show()
def interactive_img_detection(image_path):
    image=cv2.imread(image_path)    
    if image is None:
        print("error: image not found!!!")
        return
    gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    display_image("original grayscale image",gray_image)

    print("select an option from 1-6")
    print("1:sobel edge detection")
    print("2: canny edge detection")
    print("3: laplacian edge detection")
    print("4: Gaussian smoothing")
    print("5: Median filtering")
    print("6: exit")
    while True:
        choice=input("enter you choice 1-6: ")

        if choice=="1":
            sobelx=cv2.Sobel(gray_image,cv2.CV_64F,1,0,ksize=3)
            sobely=cv2.Sobel(gray_image,cv2.CV_64F,0,1,ksize=3)
            combined_sobel=cv2.bitwise_or(sobelx.astype(np.uint8),sobely.astype(np.uint8))
            display_image("sobel edge detection",combined_sobel)
        elif choice=="2":
            print("provide threshold for canny (default: 100,200)")    
            lower_thresh=int(input("enter lower threshhold: "))
            upper_thresh=int(input("enter higher threshhold: "))
            edges=cv2.Canny(gray_image,lower_thresh,upper_thresh)
            display_image("canny edge detection",edges)
        elif choice =="3":
            laplacian=cv2.Laplacian(gray_image,cv2.CV_64F)    
            display_image("laplacian edge detection",np.abs(laplacian).astype(np.uint8))
            #filtering techniques
        elif choice=="4":
            print("adjust kernelsize for Gaussian blur (must be odd, default=5)")
            kernel_size=int(input("enter kernel size: ")) 
            blurred=cv2.GaussianBlur(image,(kernel_size,kernel_size),0)
            display_image("Gaussian Smoothed img",blurred)  
        elif choice=="5":
            print("adjust kernel size for median filtering (must be odd, default=5)")    
            kernel_size=int(input("enter kernel size: ")) 
            median_filtered=cv2.medianBlur(image,kernel_size)
            display_image("Median Filtered img",median_filtered) 
        elif choice=="6" :
            print("exiting...")
            break
        else: 
            print("invalid choice. please select a no. b/w 1-6")
interactive_img_detection("pisa.jpg")            

