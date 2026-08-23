import cv2
image = cv2.imread("image.png") #  colorful image loaded 

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imwrite("Gray_image.png",image) # saving the image

# to display 
cv2.imshow("window Title",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()




