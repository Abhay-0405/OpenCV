import cv2
image=cv2.imread("image.png",cv2.IMREAD_COLOR)

# to display 
cv2.imshow("window Title",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# To save 
cv2.imwrite("output_python.png",image)

# Image dimensions 
h,w,c=image.shape
# h-> height 
# w-> width 
# c-> channels (3 for colored images , B G R)

print(f"image height : {h}\nimage width : {w}\nimage channels: {c}")
# image height : 394
# image width : 700
# image channels: 3