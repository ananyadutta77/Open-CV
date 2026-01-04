import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
import os

def apply_filter(image, filter_type):
    filtered_image = image.copy()
    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0
    elif filter_type == "green_tint":
        filtered_image[:, :, 2] = 0
        filtered_image[:, :, 0] = 0
    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == "sobel":
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
        combined_sobel = cv2.bitwise_or(
            sobelx.astype(np.uint8),
            sobely.astype(np.uint8)
        )
        filtered_image = cv2.cvtColor(combined_sobel, cv2.COLOR_GRAY2BGR)
    elif filter_type == "canny":
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_image, 100, 200)
        filtered_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    return filtered_image

def process_image(image):
    filter_type = "original"
    print("Press these keys to apply filters: \n"
          "r - red tint\n"
          "b - blue tint \n"
          "g - green tint \n"
          "s - sobel edge detection \n"
          "c - canny edge detection\n"
          "q - quit")
    cv2.namedWindow("filtered image", cv2.WINDOW_NORMAL)
    height, width = image.shape[:2]
    while True:
        filtered_image = apply_filter(image, filter_type)
        cv2.imshow("filtered image", filtered_image)
        cv2.resizeWindow("filtered image", width, height)
        key = cv2.waitKey(0) & 0xFF
        if key == ord("r"):
            filter_type = "red_tint"
        elif key == ord("g"):
            filter_type = "green_tint"
        elif key == ord("b"):
            filter_type = "blue_tint"
        elif key == ord("s"):
            filter_type = "sobel"
        elif key == ord("c"):
            filter_type = "canny"
        elif key == ord("q"):
            print("exiting...")
            break
        else:
            print("invalid key pressed! press r,g,b,s,c,or q!!!!")
    cv2.destroyAllWindows()

def upload_and_process_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
    )
    if not file_path:
        print("No file selected.")
        return
    image = cv2.imread(file_path)
    if image is None:
        print(f"Error: Could not read image from {file_path}")
        return
    print(f"Image loaded successfully from: {os.path.basename(file_path)}")
    print(f"Image shape: {image.shape}")
    process_image(image)

if __name__ == "__main__":
    upload_and_process_image()
