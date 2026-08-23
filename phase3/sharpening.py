import cv2
import numpy as np
from pathlib import Path


# This looks for blurreed_image.jpg in the same folder as this script.
image_path = Path(__file__).with_name("blurreed_image.jpg")
image = cv2.imread(str(image_path))

if image is None:
    print(f"Could not load image: {image_path}")
else:
    # The center value emphasizes the current pixel; negative neighbours
    # emphasize edges, making the image look sharper.
    sharpening_kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0],
    ])

    sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)

    cv2.imshow("Blurred image", image)
    cv2.imshow("Sharpened image", sharpened_image)
    cv2.imwrite(str(image_path.with_name("sharpened_image.jpg")), sharpened_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
