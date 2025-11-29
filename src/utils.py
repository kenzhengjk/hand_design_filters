import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO
from typing import List, Optional, Tuple

def set_seed(seed: int = 7) -> None:
    """Sets the random seed for reproducibility."""
    import random
    import torch
    
    torch.manual_seed(seed)
    random.seed(seed)
    np.random.seed(seed)

def load_image_from_url(url: str) -> np.ndarray:
    """Loads an image from a URL and returns it as a numpy array."""
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return np.array(img)

def rgb2gray(rgb: np.ndarray) -> np.ndarray:
    """Converts an RGB image to grayscale."""
    if len(rgb.shape) == 3 and rgb.shape[2] == 3:
        return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
    return rgb

def show_multiple_images(images: List[np.ndarray], titles: List[str], figsize: Tuple[int, int] = (15, 5)) -> None:
    """Displays multiple images side-by-side using matplotlib."""
    if len(images) != len(titles):
        raise ValueError("Number of images must match number of titles.")
    
    plt.figure(figsize=figsize)
    for i, (img, title) in enumerate(zip(images, titles)):
        plt.subplot(1, len(images), i + 1)
        plt.imshow(img, cmap='gray')
        plt.title(title)
        plt.axis('off')
    plt.show()