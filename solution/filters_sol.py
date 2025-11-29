import numpy as np
from scipy import ndimage
from typing import Optional

def apply_convolution(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """
    Applies a convolution kernel to an image.
    
    Args:
        image: 2D numpy array representing the grayscale image.
        kernel: 2D numpy array representing the filter kernel.
        
    Returns:
        The convolved image.
    """
    # Using scipy.ndimage for efficiency and correctness
    return ndimage.convolve(image, kernel)

def get_blur_kernel(filter_size: int=3) -> np.ndarray:
    """
    Constructs a 3x3 averaging (blur) kernel.
    
    Returns:
        A 3x3 numpy array normalized so that it sums to 1.
    """
    # ================================================================ #
    # TODO: Implement a 3x3 averaging kernel.                          #
    # Hint: The kernel should have shape (3, 3) and sum to 1.          #
    # ================================================================ #
    
    kernel = None
    
    # --- SOLUTION START ---
    kernel = np.ones((filter_size, filter_size)) / (filter_size * filter_size) 
    # --- SOLUTION END ---
    
    if kernel is None:
        raise NotImplementedError("Blur kernel not implemented.")

    return kernel

def get_edge_detection_kernel() -> np.ndarray:
    """
    Constructs a 3x3 edge detection kernel (Laplacian).
    
    Returns:
        A 3x3 numpy array.
    """
    # ================================================================ #
    # TODO: Implement a 3x3 edge detection kernel.                     #
    # Hint: A common kernel is [[0, 1, 0], [1, -4, 1], [0, 1, 0]]      #
    # ================================================================ #
    
    kernel = None
    
    # --- SOLUTION START ---
    kernel = np.array([
        [0, 1, 0], 
        [1, -4, 1], 
        [0, 1, 0]
    ])
    # --- SOLUTION END ---
    
    if kernel is None:
        raise NotImplementedError("Edge detection kernel not implemented.")

    return kernel

def get_sharpen_kernel(blur_kernel: np.ndarray, sharpness_factor: float=1.5) -> np.ndarray:
    """
    Constructs a 3x3 sharpen kernel.
    
    Returns:
        A 3x3 numpy array.
    """
    identity_kernel = np.zeros_like(blur_kernel)
    identity_kernel[1, 1] = 1  # Identity kernel for 3x3 (center pixel is 1, others are 0)

    # --- SOLUTION START ---
    # Calculate the unsharp mask kernel
    unsharp_kernel = identity_kernel - blur_kernel

    # Apply the sharpness factor
    sharpen_kernel = identity_kernel + sharpness_factor * unsharp_kernel
    # --- SOLUTION END ---
    
    return sharpen_kernel

def edge_detecting_pipeline(image: np.ndarray) -> np.ndarray:
    """
    Full pipeline to detect edges in an image.
    """
    kernel = get_edge_detection_kernel()
    return apply_convolution(image, kernel)