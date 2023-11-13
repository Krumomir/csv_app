import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


# Function for histogram equalization
def histogram_equalization(image, method=1):
    # Check if the input image is in color and convert to grayscale if necessary
    if image.ndim == 3:
        image = np.mean(image, axis=2)

    # Define the number of bins for the histogram
    num_bins = 256

    # Compute the histogram and bins
    histogram, bins = np.histogram(image.flatten(), num_bins, density=True)

    # Define the range for pixel and cumulative histograms
    P_min, P_max = 0, num_bins - 1
    C_min, C_max, C_new = 0, num_bins - 1, np.zeros(num_bins)

    # Initialize histograms and variables
    H = np.zeros(num_bins)
    R_current = 0
    H_sum = 0
    H_mid = (P_max - P_min) / (C_max - C_min)

    # Compute the histogram of the input image
    for pixel_value in range(P_min, P_max + 1):
        H[pixel_value] = np.sum(image == pixel_value)

    # Histogram equalization process
    for C_current in range(C_min, C_max + 1):
        L = R_current
        H_sum += H[C_current]

        # Perform the redistribution of pixel values based on the cumulative histogram
        while H_sum > H_mid:
            H_sum -= H_mid
            R_current += 1

        R = R_current

        # Apply the chosen equalization method
        if method == 1:
            C_new[C_current] = (L + R) / 2
        elif method == 2:
            C_new[C_current] = np.random.randint(L, R + 1)

    # Update the pixel values in the input image
    for pixel_value in range(P_min, P_max + 1):
        if method in [1, 2]:
            image[np.where(image == pixel_value)] = C_new[pixel_value]

    return image


def main():
    # Load the input image
    input_image = Image.open('flowers.webp')
    input_image = np.array(input_image)

    # Apply histogram equalization with different methods
    output_image_method1 = histogram_equalization(input_image, method=1)
    output_image_method2 = histogram_equalization(input_image, method=2)

    # Display the input and output images
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 2, 1)
    plt.imshow(input_image, cmap='gray')
    plt.title('Input Image')

    plt.subplot(2, 2, 2)
    plt.imshow(output_image_method1, cmap='gray')
    plt.title('Method 1')

    plt.subplot(2, 2, 3)
    plt.imshow(output_image_method2, cmap='gray')
    plt.title('Method 2')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
