import cv2 

image=cv2.imread("image.png")

cropped_img=image[100:200,50:150]

cv2.imshow("title",cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite("cropped_img.png",cropped_img)

