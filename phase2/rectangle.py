import cv2
image=cv2.imread("virat.jpg")

color=(0,0,256)
pt1=(100,100)
pt2=(200,300)
thickness=3
rectangle=cv2.rectangle(image,pt1,pt2,color,thickness)
cv2.imshow("rectangle",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("rectangle.png",rectangle)
