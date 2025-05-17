import cv2
import numpy as np
import os

# Load Image Function
def load_image(path):
    image = cv2.imread(path)
    return image

# Analyze color and brightness
def analyze_image(image):
    # Resize for consistent analysis
    resized = cv2.resize(image, (100, 100))
    hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
    
    # Brightness check
    brightness = np.mean(hsv[:, :, 2])  # V channel

    # Dominant color
    avg_color = np.mean(resized, axis=(0, 1))  # BGR
    avg_b, avg_g, avg_r = avg_color

    # Colorfulness measure
    color_diff = np.std(resized, axis=(0, 1)).mean()

    # Decision Rules
    if brightness > 180:
        return "Transparent", "B"
    elif avg_b < 50 and avg_g < 50 and avg_r < 50:
        return "Black", "A"
    elif color_diff > 40:
        return "Colorful", "C"
    else:
        return "Unclassified", "None"

# Main Processing
def process_image(image_path):
    image = load_image(image_path)
    category, belt = analyze_image(image)
    print(f"Image '{image_path}' is classified as: {category} → Send to Conveyor Belt {belt}")

# Example: Run on a single image
if __name__ == "__main__":
    path = input("Enter image path: ")  # Example: dataset/colorful/img1.jpg
    process_image(path)
