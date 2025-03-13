import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load the uploaded image
image_path = "/mnt/data/0196Mike F. B_W WEB.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply Gaussian Blur to reduce noise
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Use Canny edge detection to generate a sketch effect
edges = cv2.Canny(blurred, threshold1=50, threshold2=150)

# Invert the colors for a pencil sketch effect
sketch = cv2.bitwise_not(edges)

# Save and display the sketch image
sketch_path = "/mnt/data/sketch_image.jpg"
cv2.imwrite(sketch_path, sketch)

# Display the sketch
plt.figure(figsize=(8,6))
plt.imshow(sketch, cmap='gray')
plt.axis("off")
plt.title("Generated Sketch")
plt.show()

# Provide the processed file
sketch_path
