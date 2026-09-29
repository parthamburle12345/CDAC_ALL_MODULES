from PIL import Image
import numpy as np

# 1. Load an image file into a NumPy array
# (You can use any JPG or PNG image on your computer)
img = np.array(Image.open("tiger.jpg"))

# 2. Inspect core array attributes
print("Data Type :", img.dtype)  # uint8 (values from 0 to 255)
print("Dimensions:", img.ndim)   # 3 (Height, Width, Color Channels)
print("Shape     :", img.shape)  # e.g., (300, 400, 3) -> 300 rows, 400 cols, 3 channels
print("Pixel(0,0):", img[0, 0])  # [R, G, B] values of the top-left pixel

# cropped = img[img.shape[0]//2:, img.shape[1]//2:].copy()
cropped = img[img.shape[0]//4:(img.shape[0]//4+img.shape[0]//2), img.shape[1]//4:(img.shape[1]//4+img.shape[1]//2)].copy()
Image.fromarray(cropped).save("cropped.jpg")

thumbnail = img[::3, ::3].copy()
Image.fromarray(thumbnail).save("thumbnail.jpg")

# Horizontal Flip (Mirror: reverse columns along Axis 1)
horizontal_flip = img[:, ::-1]
Image.fromarray(horizontal_flip).save("flipped_horizontal.jpg")

# Vertical Flip (Upside-down: reverse rows along Axis 0)
vertical_flip = img[::-1, :]
Image.fromarray(vertical_flip).save("flipped_vertical.jpg")

# Vertical Flip (Upside-down: reverse rows along Axis 0)
vertical_flip = img[::-1, ::-1]
Image.fromarray(vertical_flip).save("flipped.jpg")

# Convert 3D RGB array to 2D Grayscale matrix
gray = (
    img[:, :, 0] * 0.299 +
    img[:, :, 1] * 0.587 +
    img[:, :, 2] * 0.114
).astype(np.uint8)

Image.fromarray(gray).save("grayscale.jpg")
print("Grayscale Shape:", gray.shape)  # 2D array: (Height, Width)

# 1. Increase Brightness (+40):
brightened = np.clip(img.astype(np.int16) + 40, 0, 255).astype(np.uint8)
Image.fromarray(brightened).save("brightened.jpg")

# 2. Warm Sunset Tint (Boost Red, soften Blue via broadcasting):
warm_filter = np.array([1.25, 1.05, 0.75])
warm_img = np.clip(img * warm_filter, 0, 255).astype(np.uint8)
Image.fromarray(warm_img).save("warm_tint.jpg")

