import numpy as np
from scipy import ndimage

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
    Constructs a filter_size by filter_size averaging (blur) kernel.
    
    Returns:
        A numpy array normalized so that it sums to 1.
    """
    # ================================================================= #
    # START TODO: Implement an averaging kernel with given filter_size. #                    
    # Hint: You can use np.ones                                         #
    # ================================================================= #
    kernel = None

    # ================================================================= #
    # END OF YOUR CODE                                                  #
    # ================================================================= #

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
    # START TODO: Implement the Laplacian derivative filter.           #
    # ================================================================ #
    kernel = None
    
    # ================================================================ #
    # END OF YOUR CODE                                                 #
    # ================================================================ #
    
    if kernel is None:
        raise NotImplementedError("Edge detection kernel not implemented.")

    return kernel

def get_sharpen_kernel(blur_kernel: np.ndarray, sharpness_factor: float=1.5) -> np.ndarray:
    """
    Constructs a 3x3 sharpen kernel.
    
    Returns:
        A 3x3 numpy array.
    """
    # ========================================================================= #
    # START TODO: Implement a sharpening kernel.                                # 
    # Hint: Sharpening is just adding high frequency components to the image!   #
    # ========================================================================= #
    identity_kernel = np.zeros_like(blur_kernel)
    identity_kernel[1, 1] = 1  # Identity kernel for 3x3 (center pixel is 1, others are 0)
    
    # Another hint: think about what you can do with a blur filter and identity filter!
    kernel = None

    # ========================================================================= #
    # END OF YOUR CODE                                                          #
    # ========================================================================= #
    
    if kernel is None:
        raise NotImplementedError("Sharpening kernel not implemented.")
    
    return kernel
