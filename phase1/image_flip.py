import cv2 
image=cv2.imread("virat.jpg")
flipped_vertical=cv2.flip(image,0)
flipped_horizontal=cv2.flip(image,1)
flipped_both=cv2.flip(image,-1)

cv2.imshow("flipped_vertical",flipped_vertical)
cv2.imwrite("flipped_vertical.jpg",flipped_vertical)


cv2.imshow("flipped_horizontal",flipped_horizontal)
cv2.imwrite("flipped_horizontal.jpg",flipped_horizontal)

cv2.imshow("flipped_both",flipped_both)
cv2.imwrite("flipped_both.jpg",flipped_both)

cv2.imshow("original",image)

cv2.waitKey(0)
cv2.destroyAllWindows()
