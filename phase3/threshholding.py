import cv2
from pathlib import Path


image_path = Path(__file__).with_name("virat.jpg")
image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)

if image is None:
    print(f"Could not load image: {image_path}")
else:
    # Pixels brighter than 127 become white (255); the rest become black (0).
    _, threshold_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow("Original image", image)
    cv2.imshow("Threshold image", threshold_image)
    cv2.imwrite("thresh_virat.jpg",threshold_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
