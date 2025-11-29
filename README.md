# Hand-Designed Image Filters Assignment

A hands-on programming assignment where you'll implement fundamental image processing filters using convolution operations. Learn how classic computer vision techniques work by building blur, edge detection, and sharpening filters from scratch!

## 📚 Learning Objectives

By completing this assignment, you will:
- Understand how convolution operations work in image processing
- Implement averaging/blur filters with different kernel sizes
- Build an edge detection filter using the Laplacian operator
- Create a sharpening filter using unsharp masking techniques
- Visualize the effects of different filters on real images

## 🗂️ Repository Structure

```
hand_design_filters/
├── src/
│   ├── __init__.py
│   ├── filters.py        # ⭐ YOUR CODE GOES HERE
│   └── utils.py          # Helper functions (pre-implemented)
├── tests/
│   ├── __init__.py
│   └── test_filters.py   # Unit tests to verify your implementation
├── run.py                # Main script to test filters on images
├── requirements.txt 
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd hand_design_filters
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📝 Assignment Tasks

You will implement **three filter functions** in `src/filters.py`. Each function is marked with TODO comments.

### Task 1: Blur Filter (Averaging Kernel)

**Function:** `get_blur_kernel(filter_size: int = 3)`

Implement an averaging kernel that blurs the image by replacing each pixel with the average of its neighbors.

**Requirements:**
- Create a `filter_size × filter_size` kernel filled with equal values
- Normalize the kernel so it sums to 1.0 (preserves brightness)
- **Hint:** Use `np.ones()` to create the kernel


### Task 2: Edge Detection Filter (Laplacian)

**Function:** `get_edge_detection_kernel()`

Implement a 3×3 Laplacian kernel that detects edges by finding areas of rapid intensity change.

**Requirements:**
- Create a 3×3 kernel that highlights edges
- The kernel should sum to 0 (responds to changes, not constant values)

### Task 3: Sharpening Filter (Unsharp Masking)

**Function:** `get_sharpen_kernel(blur_kernel: np.ndarray, sharpness_factor: float = 1.5)`

Implement a sharpening kernel using the unsharp masking technique.

**Requirements:**
- Use the provided identity kernel and blur kernel
- **Hint:** Think about combining the identity kernel and blur kernel mathematically


## 🏃 Running Your Code

### Test on Real Images

Run the main script to see your filters in action:

```bash
python run.py
```

This will:
1. Load a sample image from the internet
2. Apply your blur filters with different kernel sizes (3×3, 6×6, 9×9)
3. Apply your edge detection filter
4. Apply your sharpening filter with different strength factors (2, 5, 8)
5. Display the results side-by-side

**Note:** The script will skip tasks that haven't been implemented yet.

### Run Unit Tests

Verify your implementation with automated tests (and add your own too!):

```bash
# Run all tests
python -m unittest tests/test_filters.py

# Run tests with verbose output
python -m unittest tests/test_filters.py -v

# Run a specific test
python -m unittest tests.test_filters.TestFilters.test_blur_kernel_defaults
```

**What the tests check:**
- ✅ Blur kernel has correct dimensions
- ✅ Blur kernel sums to 1.0 (brightness preservation)
- ✅ Blur kernel has equal values (true averaging)
- ✅ Edge kernel is 3×3
- ✅ Edge kernel sums to 0 (derivative filter property)
- ✅ Sharpen kernel preserves brightness

## 🔍 Understanding the Code

### File Descriptions

**`src/filters.py`** (YOUR WORK)
- Contains three functions you need to implement
- Each function has clear TODO markers
- The `apply_convolution()` function is already implemented

**`src/utils.py`** (Pre-implemented)
- Helper functions for loading images, converting to grayscale, and visualization
- You don't need to modify this file

**`run.py`** (Ready to use)
- Demonstrates your filters on a real image
- Shows progressive effects with different parameters
- Great for visual debugging

**`tests/test_filters.py`** (Automated testing)
- Unit tests to verify correctness
- Tests mathematical properties of your kernels
- Run these to check your implementation

## 💡 Tips and Hints

1. **Start with Task 1 (Blur)**
   - It's the simplest and builds intuition
   - Remember to normalize (divide by the sum)

2. **For Edge Detection**
   - Look up the Laplacian operator if stuck
   - The center value should be positive, neighbors negative
   - Sum should equal zero

3. **For Sharpening**
   - You're adding high-frequency details back to the image
   - The identity kernel is already created for you
   - Think algebraically: what combination of identity and blur gives you sharpening?

4. **Debugging**
   - Print your kernels! Uncomment the print statements in `run.py`
   - Check that blur kernel sums to 1.0
   - Check that edge kernel sums to 0.0
   - Visualize results with `run.py` before running tests

5. **Experiment!**
   - Try different blur kernel sizes in the sharpening task
   - Notice how larger blur kernels affect sharpening results
   - This is a great way to build intuition

## 📊 Expected Output

When you run `python run.py`, you should see:

1. **Blur Results:** Images progressively more blurred with larger kernels
2. **Edge Detection:** Edges highlighted in white against a dark background
3. **Sharpening:** Images with enhanced details and sharper edges

## ❓ Troubleshooting

**Import errors?**
- Make sure you're in the `hand_design_filters` directory
- Check that your virtual environment is activated
- Verify all dependencies are installed

**Tests failing?**
- Print your kernel values to debug
- Check kernel dimensions with `.shape`
- Verify sums with `np.sum(kernel)`

**No images showing?**
- Make sure matplotlib is installed
- If using SSH/remote, you may need to save images instead of displaying
- Check your internet connection (the script downloads a sample image)

## 📚 Additional Resources

- [NumPy Documentation](https://numpy.org/doc/)
- [Image Processing Kernels](https://en.wikipedia.org/wiki/Kernel_(image_processing)#Details)
- [Unsharp Masking](https://en.wikipedia.org/wiki/Unsharp_masking)

## ✅ Submission Checklist

Before submitting, make sure:
- [ ] All three functions in `src/filters.py` are implemented
- [ ] `python run.py` executes without errors
- [ ] All unit tests pass
- [ ] You've experimented with different parameters

## 📧 Getting Help

If you're stuck:
1. Review the hints in the code comments
2. Print intermediate values to debug
3. Check the unit test error messages
4. Review the mathematical formulas above
5. And of course, ask for help on Ed!

---

Good luck, and have fun exploring some fundamental image processing techniques! 🎨🔬
