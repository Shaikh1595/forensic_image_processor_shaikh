import numpy as np
from skimage import io, color, morphology, filters, exposure
import matplotlib.pyplot as plt
import cv2

# Load the 'before' image to be processed.
before_image_path = ('D:/Users/sahil/Documents/PROJECTS/forensic_image_processor/cartridge_case_images_original/case_image_1.jpg')
before_image = io.imread(before_image_path)

# Define the size of the border to be ignored
border_size = 50

# Create a mask for the entire image
roi_mask = np.ones_like(before_image, dtype=bool)

# Define the region of interest (ROI) coordinates within the mask.
# These values define the area to be excluded (the 50-pixel border).
roi_mask[border_size:-border_size, border_size:-border_size] = False

# Convert the image to grayscale for analysis.
gray_image = color.rgb2gray(before_image)

# Define the approximate range of intensities for the breech-face impression in the grayscale image.
# These values should be adjusted based on the specific image characteristics.
lower_threshold = 0.7  # Lower threshold for the breech-face impression
upper_threshold = 1.0  # Upper threshold for the breech-face impression

# Create a mask for the breech-face impression based on the intensity range.
breech_face_mask = ((gray_image > lower_threshold) & (gray_image <= upper_threshold))

# Clean up the mask by removing small objects (noise) and filling holes.
breech_face_mask_cleaned = morphology.remove_small_objects(breech_face_mask, min_size=50)
breech_face_mask_cleaned = morphology.remove_small_holes(breech_face_mask_cleaned, area_threshold=50)

# Apply the breech-face mask to the image, marking it in red.
processed_image = before_image.copy()
for c in range(3):  # Apply color to all three channels
    processed_image[:, :, c] = np.where(breech_face_mask_cleaned, [255, 0, 0][c], processed_image[:, :, c])

# Define the approximate position and size of the aperture shear.
# These values should be adjusted based on the specific image characteristics.
shear_center_x = 300  # X-coordinate of the shear's center
shear_center_y = 100  # Y-coordinate of the shear's center
shear_width = 20      # Width of the shear area
shear_height = 20     # Height of the shear area

# Create a mask for the aperture shear based on the defined coordinates.
aperture_shear_mask = np.zeros_like(gray_image, dtype=bool)
aperture_shear_mask[shear_center_y-shear_height//2:shear_center_y+shear_height//2,
                    shear_center_x-shear_width//2:shear_center_x+shear_width//2] = True

# Define the approximate range of intensities for the breech-face impression in the grayscale image.
# These values should be adjusted based on the specific image characteristics.
lower_threshold_breech_face = 0.7  # Lower threshold for the breech-face impression
upper_threshold_breech_face = 1.0  # Upper threshold for the breech-face impression

# Create a mask for the breech-face impression based on the intensity range.
breech_face_mask = ((gray_image > lower_threshold_breech_face) & (gray_image <= upper_threshold_breech_face))

# Clean up the breech-face mask by removing small objects (noise) and filling holes.
breech_face_mask_cleaned = morphology.remove_small_objects(breech_face_mask, min_size=50)
breech_face_mask_cleaned = morphology.remove_small_holes(breech_face_mask_cleaned, area_threshold=50)

# Apply the breech-face mask to the image, marking it in red.
processed_image = before_image.copy()
for c in range(3):  # Apply color to all three channels
    processed_image[:, :, c] = np.where(breech_face_mask_cleaned, [255, 0, 0][c], processed_image[:, :, c])

# Define the approximate position and size of the aperture shear.
# These values should be adjusted based on the specific image characteristics.
shear_center_x = 300  # X-coordinate of the shear's center
shear_center_y = 100  # Y-coordinate of the shear's center
shear_width = 20      # Width of the shear area
shear_height = 20     # Height of the shear area

# Create a mask for the aperture shear based on the defined coordinates.
aperture_shear_mask = np.zeros_like(gray_image, dtype=bool)
aperture_shear_mask[shear_center_y-shear_height//2:shear_center_y+shear_height//2,
                    shear_center_x-shear_width//2:shear_center_x+shear_width//2] = True

# Apply the aperture shear mask to the image, marking it in green.
for c in range(3):  # Apply color to all three channels
    processed_image[:, :, c] = np.where(aperture_shear_mask, [0, 255, 0][c], processed_image[:, :, c])

# Define the approximate range of intensities for the firing pin impression in the grayscale image.
# These values should be adjusted based on the specific image characteristics.
lower_threshold_firing_pin_impression = 0.3  # Lower threshold for the firing pin impression
upper_threshold_firing_pin_impression = 0.6  # Upper threshold for the firing pin impression

# Create a mask for the firing pin impression based on the intensity range.
firing_pin_impression_mask = ((gray_image > lower_threshold_firing_pin_impression) &
                              (gray_image <= upper_threshold_firing_pin_impression))

# Clean up the firing pin impression mask by removing small objects (noise) and filling holes.
firing_pin_impression_mask_cleaned = morphology.remove_small_objects(firing_pin_impression_mask, min_size=50)
firing_pin_impression_mask_cleaned = morphology.remove_small_holes(firing_pin_impression_mask_cleaned, area_threshold=50)

# Apply the firing pin impression mask to the image, marking it in purple.
for c in range(3):  # Apply color to all three channels
    processed_image[:, :, c] = np.where(firing_pin_impression_mask_cleaned, [128, 0, 128][c], processed_image[:, :, c])

# Define the approximate range of intensities for the firing pin drag in the grayscale image.
# These values should be adjusted based on the specific image characteristics.
lower_threshold_firing_pin_drag = 0.6  # Lower threshold for the firing pin drag
upper_threshold_firing_pin_drag = 0.8  # Upper threshold for the firing pin drag

# Create a mask for the firing pin drag based on the intensity range.
firing_pin_drag_mask = ((gray_image > lower_threshold_firing_pin_drag) &
                        (gray_image <= upper_threshold_firing_pin_drag))

# Clean up the firing pin drag mask by removing small objects (noise) and filling holes.
firing_pin_drag_mask_cleaned = morphology.remove_small_objects(firing_pin_drag_mask, min_size=50)
firing_pin_drag_mask_cleaned = morphology.remove_small_holes(firing_pin_drag_mask_cleaned, area_threshold=50)

# Define the approximate range of intensities for the breech-face impression in the grayscale image.
# These values should be adjusted based on the specific image characteristics.
lower_threshold_breech = 0.7  # Lower threshold for the breech-face impression
upper_threshold_breech = 1.0  # Upper threshold for the breech-face impression

# Create a mask for the breech-face impression based on the intensity range.
breech_face_mask = ((gray_image > lower_threshold_breech) & (gray_image <= upper_threshold_breech))

# Clean up the mask by removing small objects (noise) and filling holes.
breech_face_mask_cleaned = morphology.remove_small_objects(breech_face_mask, min_size=50)
breech_face_mask_cleaned = morphology.remove_small_holes(breech_face_mask_cleaned, area_threshold=50)

# Define the approximate position and size of the aperture shear.
# These values should be adjusted based on the specific image characteristics.
shear_center_x = 330  # X-coordinate of the shear's center
shear_center_y = 140  # Y-coordinate of the shear's center
shear_width = 50      # Width of the shear area
shear_height = 20     # Height of the shear area

# Create a mask for the aperture shear based on the defined coordinates.
aperture_shear_mask = np.zeros_like(gray_image, dtype=bool)
aperture_shear_mask[shear_center_y-shear_height//2:shear_center_y+shear_height//2,
                    shear_center_x-shear_width//1:shear_center_x+shear_width//2] = True

# Define the approximate range of intensities for the firing pin impression in the grayscale image.
# These values should be adjusted based on the specific image characteristics.
lower_threshold_firing_pin = 0.2  # Lower threshold for the firing pin impression
upper_threshold_firing_pin = 0.4  # Upper threshold for the firing pin impression

# Create a mask for the firing pin impression based on the intensity range.
firing_pin_impression_mask = ((gray_image > lower_threshold_firing_pin) & (gray_image <= upper_threshold_firing_pin))

# Clean up the mask by removing small objects (noise) and filling holes.
firing_pin_impression_mask_cleaned = morphology.remove_small_objects(firing_pin_impression_mask, min_size=50)
firing_pin_impression_mask_cleaned = morphology.remove_small_holes(firing_pin_impression_mask_cleaned, area_threshold=50)

# Define the approximate range of intensities for the firing pin drag in the grayscale image.
# These values should be adjusted based on the specific image characteristics.
lower_threshold_firing_pin_drag = 0.35  # Lower threshold for the firing pin drag
upper_threshold_firing_pin_drag = 0.5  # Upper threshold for the firing pin drag

# Create a mask for the firing pin drag based on the intensity range.
firing_pin_drag_mask = ((gray_image > lower_threshold_firing_pin_drag) & (gray_image <= upper_threshold_firing_pin_drag))

# Clean up the mask by removing small objects (noise) and filling holes.
firing_pin_drag_mask_cleaned = morphology.remove_small_objects(firing_pin_drag_mask, min_size=50)
firing_pin_drag_mask_cleaned = morphology.remove_small_holes(firing_pin_drag_mask_cleaned, area_threshold=50)

# Apply the masks for breech-face, aperture shear, firing pin impression, and firing pin drag to the image.
processed_image = before_image.copy()

# Apply the breech-face mask in red
for c in range(3):
    processed_image[:, :, c] = np.where(breech_face_mask_cleaned, [255, 0, 0][c], processed_image[:, :, c])

# Apply the aperture shear mask in green
for c in range(3):
    processed_image[:, :, c] = np.where(aperture_shear_mask, [0, 255, 0][c], processed_image[:, :, c])

# Apply the firing pin impression mask in purple
for c in range(3):
    processed_image[:, :, c] = np.where(firing_pin_impression_mask_cleaned, [171, 0, 128][c], processed_image[:, :, c])

# Apply the firing pin drag mask in light blue
for c in range(3):
    processed_image[:, :, c] = np.where(firing_pin_drag_mask_cleaned, [0, 191, 255][c], processed_image[:, :, c])

# Calculate the center of the image (where the red dot from Step 1 is)
center_x = before_image.shape[1] // 2
center_y = before_image.shape[0] // 2

# Define the direction of the firing pin drag arrow.
# This example points straight up. You can adjust the angle as needed.
arrow_length = 70  # Length of the arrow
arrow_angle = 290  # Angle in degrees (0 degrees is up)

# Calculate the endpoint of the arrow.
end_x = int(center_x + arrow_length * np.cos(np.radians(arrow_angle)))
end_y = int(center_y - arrow_length * np.sin(np.radians(arrow_angle)))

# Draw the arrow on the processed image in blue.
cv2.arrowedLine(processed_image, (center_x, center_y), (end_x, end_y), [0, 0, 255], thickness=5, tipLength=0.3)

# Save the final processed image.
output_image_path = ('D:/Users/sahil/Documents/PROJECTS/forensic_image_processor/cartridge_case_images_processed/case_image_processed.jpg')
io.imsave(output_image_path, processed_image)

# Display the processed image.
plt.imshow(processed_image)
plt.axis('on')
plt.show()
