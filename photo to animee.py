
#import the packages
import cv2
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# Function to load image using OpenCV
def load_image():
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename()
    # If a file is selected
    if file_path:
        # Load the image using cv2
        img = cv2.imread(file_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Process the image
        process_image(img)

# Function to process and display the image
def process_image(img):
    #Convert to grayscale and apply median blur to reduce image noise
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayimg = cv2.medianBlur(grayimg, 5)

    #Get the edges 
    edges = cv2.adaptiveThreshold(grayimg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 5)

    #Convert to a cartoon version
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    #Display original image
    plt.figure(figsize=(6, 6))
    plt.imshow(img)
    plt.axis("off")
    plt.title("Original Image")
    plt.show()

    #Display cartoon image
    plt.figure(figsize=(6, 6))
    plt.imshow(cartoon)
    plt.axis("off")
    plt.title("Cartoon Image")
    plt.show()

# Create tkinter root window
root = tk.Tk()
root.title("Image Cartoonizer")

# Button to load image
load_button = tk.Button(root, text="Load Image", command=load_image)
load_button.pack(pady=10)

# Run the tkinter event loop
root.mainloop()

    # Get the edges 
    edges = cv2.adaptiveThreshold(grayimg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 5)

    # Convert to a cartoon version
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Display original image
    plt.figure(figsize=(6, 6))
    plt.imshow(img)
    plt.axis("off")
    plt.title("Original Image")
    plt.show()

    # Display cartoon image
    plt.figure(figsize=(6, 6))
    plt.imshow(cartoon)
    plt.axis("off")
    plt.title("Cartoon Image")
    plt.show()

    # Convert image to anime-style using CycleGAN (for illustration purposes only)
    anime_style = convert_to_anime(img)

    # Display anime-style image
    plt.figure(figsize=(6, 6))
    plt.imshow(anime_style)
    plt.axis("off")
    plt.title("Anime-Style Image")
    plt.show()

# Function to convert image to anime style (using a placeholder function)
def convert_to_anime(img):
    # Placeholder function for illustration
    # In practice, you would use a pre-trained model like CycleGAN
    # This function simply returns a random noise image as an example
    return np.random.randint(0, 256, img.shape, dtype=np.uint8)

# Create tkinter root window
root = tk.Tk()
root.title("Image Cartoonizer")

# Button to load image
load_button = tk.Button(root, text="Load Image", command=load_image)
load_button.pack(pady=10)

# Run the tkinter event loop
root.mainloop()
