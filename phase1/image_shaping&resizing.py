import cv2
from pathlib import Path

image=cv2.imread("image.png")

if image is not None:
    resized=cv2.resize(image,(300,300))
    cv2.imwrite("resized_python_image.png",resized)
    cv2.imshow("something",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("enter a valid file name ")