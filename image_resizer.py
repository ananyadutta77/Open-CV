import cv2
def main():
    image=cv2.imread("shinchan.jpg")
    if image is None:
        print(f"error: unable to load image at {image}")
        return
    print(" original image loaded successfully!!")
    sizes={'small':(200,200),'medium':(400,400),'large':(600,600)}
    for size_name,dimensions in sizes.items():
        resized=cv2.resize(image,dimensions)
        cv2.imshow(f"{size_name.capitalize()}IMage",resized)
        cv2.imwrite(f"input_image_{size_name}.jpg",resized)
        print(f"image resized to {dimensions[0]}X{dimensions[1]} pixels ({size_name})and saved.")

        print("displaying all resized images. press 0 to exit")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("destroyed all windows. Project completed successfully...!")
if __name__=="__main__":
    main()        