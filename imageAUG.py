from PIL import Image, ImageEnhance
import os
import random
import time

image_path = "large.jpg"
image = Image.open(image_path)

size = (32, 32)
image = image.resize(size)
# Define the augmentation parameters
rotation_angles = [-15, -10, -5, 0, 5, 10, 15]
brightness_factors = [0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3]
contrast_factors = [0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3]

# Create the output directory
output_dir = "augmented_images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# Apply the augmentations and save the resulting images
for i in range(200):
    # Randomly select the augmentation parameters
    rotation_angle = random.choice(rotation_angles)
    brightness_factor = random.choice(brightness_factors)
    contrast_factor = random.choice(contrast_factors)
    # Apply the augmentations
    augmented_image = image.rotate(rotation_angle)
    augmented_image = ImageEnhance.Brightness(augmented_image).enhance(brightness_factor)
    augmented_image = ImageEnhance.Contrast(augmented_image).enhance(contrast_factor)
    # Save the resulting image with a timestamp in the filename
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_dir, f"augmented_image_{i}_{timestamp}.jpg")
    augmented_image.save(output_path)
