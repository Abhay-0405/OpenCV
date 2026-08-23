import cv2
import numpy as np
from pathlib import Path


output_folder = Path(__file__).parent

# Create two black 300 x 300 grayscale images.
img1 = np.zeros((300, 300), dtype="uint8")
img2 = np.zeros((300, 300), dtype="uint8")

# Draw solid white shapes. -1 means fill the shape.
cv2.circle(img1, (150, 150), 100, 255, -1)
cv2.rectangle(img2, (100, 100), (250, 250), 255, -1)

bitwise_and = cv2.bitwise_and(img1, img2)
bitwise_or = cv2.bitwise_or(img1, img2)
bitwise_not = cv2.bitwise_not(img1)

# Save every image displayed below in this same folder.
cv2.imwrite(str(output_folder / "bitwise_circle.png"), img1)
cv2.imwrite(str(output_folder / "bitwise_rectangle.png"), img2)
cv2.imwrite(str(output_folder / "bitwise_and.png"), bitwise_and)
cv2.imwrite(str(output_folder / "bitwise_or.png"), bitwise_or)
cv2.imwrite(str(output_folder / "bitwise_not_circle.png"), bitwise_not)

cv2.imshow("Circle", img1)
cv2.imshow("Rectangle", img2)
cv2.imshow("AND", bitwise_and)
cv2.imshow("OR", bitwise_or)
cv2.imshow("NOT", bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
