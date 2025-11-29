# Setup
import sys
import os
import numpy as np

# Add src to path so imports work
sys.path.append(os.path.abspath(os.path.join('..')))

from src.utils import set_seed, load_image_from_url, rgb2gray, show_multiple_images
from src.filters import apply_convolution, get_blur_kernel, get_edge_detection_kernel, get_sharpen_kernel

set_seed(7)
print("Environment setup complete.")

# Load Data
IMAGE_URL = 'https://user-images.githubusercontent.com/11435359/147738734-196fd92f-9260-48d5-ba7e-bf103d29364d.jpg'
image_rgb = load_image_from_url(IMAGE_URL)
image_gray = rgb2gray(image_rgb)

show_multiple_images([image_gray], ['Original Grayscale'])

#########################
### TASK 1 - Blurring ###
#########################
# Calls the student-implemented averaging_filtering function in src/filters.py
try:
    avg_images, avg_titles = [image_gray], ['original']
    for kernel_size in [3, 6, 9]:
        blur_kernel = get_blur_kernel(kernel_size)
        
        # Uncomment these two lines to print out the kernel
        # print("Blur kernel loaded.")
        # print("Kernel:\n", blur_kernel)

        blurred_image = apply_convolution(image_gray, blur_kernel)
        avg_images.append(blurred_image)
        avg_titles.append(f'{kernel_size}X{kernel_size} Kernel')

    show_multiple_images(avg_images, avg_titles)
except NotImplementedError as e:
    print(f"TODO: {e}")

###############################
### TASK 2 - Edge Detection ###
###############################
# Calls the student-implemented get_edge_detection_kernel function in src/filters.py
try:
    edge_kernel = get_edge_detection_kernel()
    
    # Uncomment these two lines to print out the kernel
    # print("Edge kernel loaded.")
    # print("Kernel:\n", edge_kernel)
    
    edge_image = apply_convolution(image_gray, edge_kernel)
    edge_images, edge_titles = [image_gray], ['original']
    edge_images.append(edge_image)
    edge_titles.append(f'Edge Detection')

    show_multiple_images(edge_images, edge_titles)
except NotImplementedError as e:
    print(f"TODO: {e}")

###########################
### TASK 3 - Sharpening ###
###########################
# Calls the student-implemented get_sharpen_kernel function in src/filters.py
try:
    sharpen_images, sharpen_titles = [image_gray], ['original']
    for sharpness_factor in [2, 5, 8]:
        # TODO: Try different blur kernel sizes and see how the sharpened result changes!
        # Why is this the case?
        blur_kernel_size = 3
        blur_kernel = get_blur_kernel(blur_kernel_size) 
        
        # Generate the unsharp mask kernel with a sharpness factor
        sharpen_kernel = get_sharpen_kernel(blur_kernel, sharpness_factor)
        
        # Uncomment these two lines to print out the kernel
        # print("Sharpen kernel loaded.")
        # print("Kernel:\n", sharpen_kernel)
        
        # Apply the sharpen kernel to the image
        sharpened_image = apply_convolution(image_gray, sharpen_kernel)
        sharpened_image = np.clip(sharpened_image, 0, 255).astype(np.uint8)
        sharpen_images.append(sharpened_image)
        sharpen_titles.append(f'Sharpened Image (Factor {sharpness_factor})')

    show_multiple_images(sharpen_images, sharpen_titles)
except NotImplementedError as e:
    print(f"TODO: {e}")
except Exception as e:
    print(f"Error during sharpening: {e}")
