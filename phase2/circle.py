import cv2
image=cv2.imread("virat.jpg")

color=(0,0,255)
centre=(100,100)
radius=50
thickness=3
circle=cv2.circle(image,centre,radius,color,thickness)
cv2.imshow("rectangle",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("centre.png",circle)