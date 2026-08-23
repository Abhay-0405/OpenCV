import cv2 

image=cv2.imread("image.png")
h,w = image.shape[:2]
M=cv2.getRotationMatrix2D((h//2,w//2),90,1.0)
rotated=cv2.warpAffine(image,M,(w,h))

cv2.imshow("rotated_img",rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("rotated_img.png",rotated)










