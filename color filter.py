#bgr has three index [B,G,R]=[0,1,2] so if any channel (out of bgr) image[:,:,1]=0, here green=0
import cv2
import numpy as np
def apply_color_filter(image, filter_type):
    filtered_image=image.copy()
    if filter_type=="red_tint":
        filtered_image[:,:,0]=0
        filtered_image[:,:,1]=0
    elif filter_type=="blue_tint":
        filtered_image[:,:,1]=0
        filtered_image[:,:,2]=0  
    elif filter_type=="green_tint":
        filtered_image[:,:,0]=0
        filtered_image[:,:,2]=0   
    elif filter_type=="increase_red":
        filtered_image[:,:,2]=cv2.add(filtered_image[:,:,2],50)
    elif filter_type=="decrease_blue":
        filtered_image[:,:,2]=cv2.subtract(filtered_image[:,:,0],50)    
    return filtered_image
image=cv2.imread("brooklynb.jpg")   
if image is None:
    print("error: img not found")
else:
    filter_type="original"    
    print("press these keys to see the filters: ")
    print("r-red tint")
    print("b-blue tint")
    print("g-green tint")
    print("i-increase red intensity")
    print("d-decrease blue intensity")
    print("q-quit")

    while True:
        filtered_image=apply_color_filter(image,filter_type)
        cv2.imshow("filtered image", filtered_image)
        key=cv2.waitKey(0)&0xFF #waits for key press indefinitely

        if key==ord('r'): #map key press
            filter_type="red_tint"
        elif key==ord('b'): 
            filter_type="blue_tint"   
        elif key==ord('g'):
            filter_type="green_tint"  
        elif key==ord('i'):
            filter_type="increase_red"
        elif key==ord('d'):
            filter_type="decrease_blue"   
        elif key==ord('q'):
            print("Quiting...")      
            break
        else:
            print("invalid key!! use 'r','b','g','d','i','d'")   
cv2.destroyAllWindows()            



