import cv2
image=cv2.imread("virat.jpg")
if image is not None:
    blurred_image=cv2.GaussianBlur(image,(21,21),-10)
    cv2.imshow("blurred_image",blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("blurreed_image.jpg",blurred_image)
else:
    print("image not valid ...")