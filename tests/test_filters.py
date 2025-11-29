import unittest
import numpy as np
import sys
import os

# Ensure we can import from src by adding the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.filters import get_blur_kernel, get_edge_detection_kernel, get_sharpen_kernel

class TestFilters(unittest.TestCase):
    
    def test_blur_kernel_defaults(self):
        """Test the blur kernel with default arguments."""
        try:
            # Default size is usually 3
            kernel = get_blur_kernel() 
            self.assertEqual(kernel.shape, (3, 3), "Default blur kernel should be 3x3")
            self.assertTrue(np.isclose(np.sum(kernel), 1.0), "Blur kernel must sum to 1 to preserve brightness")
        except NotImplementedError:
            self.skipTest("Blur kernel not implemented yet.")

    def test_blur_kernel_custom_size(self):
        """Test the blur kernel with a specific size."""
        try:
            size = 5
            kernel = get_blur_kernel(filter_size=size)
            self.assertEqual(kernel.shape, (size, size), f"Kernel should be {size}x{size}")
            self.assertTrue(np.isclose(np.sum(kernel), 1.0), "Blur kernel must sum to 1")
            
            # Check if it is actually an averaging filter (all values should be equal)
            expected_value = 1.0 / (size * size)
            self.assertTrue(np.allclose(kernel, expected_value), "All values in averaging kernel should be 1/(size^2)")
        except NotImplementedError:
            self.skipTest("Blur kernel not implemented yet.")

    def test_edge_kernel_structure(self):
        """Test if edge kernel sums to 0."""
        try:
            kernel = get_edge_detection_kernel()
            self.assertEqual(kernel.shape, (3, 3), "Edge kernel should be 3x3")
            # Laplacian kernels usually sum to 0 (response to constant light is 0)
            self.assertTrue(np.isclose(np.sum(kernel), 0.0), "Edge detection kernel usually sums to 0")
        except NotImplementedError:
            self.skipTest("Edge kernel not implemented yet.")

    def test_sharpen_kernel_structure(self):
        """Test sharpen kernel properties."""
        try:
            blur = np.ones((3,3)) / 9.0
            # Test with a specific sharpness factor
            factor = 2.0
            kernel = get_sharpen_kernel(blur, sharpness_factor=factor)
            
            self.assertEqual(kernel.shape, (3, 3), "Sharpen kernel should match blur kernel size")
            
            # For unsharp masking: Sharpened = Original + Factor * (Original - Blurred)
            # The sum of the kernel elements determines brightness preservation.
            # Ideally, a sharpening filter should preserve mean brightness, meaning sum should be 1.
            # We check if the student's implementation preserves brightness.
            # (Identity(1) + Factor(Identity(1) - Blur(1))) = 1 + F(0) = 1.
            self.assertTrue(np.isclose(np.sum(kernel), 1.0), "Sharpen kernel should theoretically sum to 1")
            
        except NotImplementedError:
            self.skipTest("Sharpen kernel not implemented yet.")

if __name__ == '__main__':
    unittest.main()