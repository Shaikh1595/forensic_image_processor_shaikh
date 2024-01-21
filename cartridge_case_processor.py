import numpy as np
from skimage import io, color, morphology, filters, exposure
import matplotlib.pyplot as plt
import cv2

# Load the 'before' image to be processed
before_image_path = ('D:/Users/sahil/Documents/PROJECTS/forensic_image_processor/cartridge_case_images_original/case_image_1.jpg')
before_image = io.imread(before_image_path)

# Convert the image to grayscale for analysis
gray_image = color.rgb2gray(before_image)

# Define the approximate range for the breech-face impression
lower_threshold = 0.7  # Lower threshold
upper_threshold = 1.0  # Upper threshold

# Create a mask for breech-face based on the intensity range
breech_face_mask = ((gray_image > lower_threshold) & (gray_image <= upper_threshold))

# Clean up the mask
breech_face_mask_cleaned = morphology.remove_small_objects(breech_face_mask, min_size=50)
breech_face_mask_cleaned = morphology.remove_small_holes(breech_face_mask_cleaned, area_threshold=50)

# Apply the breech-face mask to the image
processed_image = before_image.copy()
for c in range(3):
    processed_image[:, :, c] = np.where(breech_face_mask_cleaned, [255, 0, 0][c], processed_image[:, :, c])

# Define the approximate position and size of the aperture shear *To be made dynamic at a later time
shear_center_x = 300  
shear_center_y = 100  
shear_width = 20      
shear_height = 20     

# Create a mask for the aperture shear
aperture_shear_mask = np.zeros_like(gray_image, dtype=bool)
aperture_shear_mask[shear_center_y-shear_height//2:shear_center_y+shear_height//2,
                    shear_center_x-shear_width//2:shear_center_x+shear_width//2] = True

# Define the approximate range of intensities for the breech-face impression in the grayscale image
lower_threshold_breech_face = 0.7 
upper_threshold_breech_face = 1.0  

# Create a mask for the breech-face impression
breech_face_mask = ((gray_image > lower_threshold_breech_face) & (gray_image <= upper_threshold_breech_face))

# Clean up the breech-face mask
breech_face_mask_cleaned = morphology.remove_small_objects(breech_face_mask, min_size=50)
breech_face_mask_cleaned = morphology.remove_small_holes(breech_face_mask_cleaned, area_threshold=50)

# Apply the breech-face mask to the image
processed_image = before_image.copy()
for c in range(3): 
    processed_image[:, :, c] = np.where(breech_face_mask_cleaned, [255, 0, 0][c], processed_image[:, :, c])

# Define the position and size of the aperture shear
shear_center_x = 300
shear_center_y = 100  
shear_width = 20     
shear_height = 20     

# Create a mask for the aperture shear
aperture_shear_mask = np.zeros_like(gray_image, dtype=bool)
aperture_shear_mask[shear_center_y-shear_height//2:shear_center_y+shear_height//2,
                    shear_center_x-shear_width//2:shear_center_x+shear_width//2] = True

# Apply the aperture shear mask to the image
for c in range(3): 
    processed_image[:, :, c] = np.where(aperture_shear_mask, [0, 255, 0][c], processed_image[:, :, c])

# Define the approximate range of intensities for the firing pin impression
lower_threshold_firing_pin_impression = 0.3 
upper_threshold_firing_pin_impression = 0.6  

# Create a mask for the firing pin impression
firing_pin_impression_mask = ((gray_image > lower_threshold_firing_pin_impression) &
                              (gray_image <= upper_threshold_firing_pin_impression))

# Clean up the firing pin impression mask
firing_pin_impression_mask_cleaned = morphology.remove_small_objects(firing_pin_impression_mask, min_size=50)
firing_pin_impression_mask_cleaned = morphology.remove_small_holes(firing_pin_impression_mask_cleaned, area_threshold=50)

# Apply the firing pin impression mask
for c in range(3):  # Apply color to all three channels
    processed_image[:, :, c] = np.where(firing_pin_impression_mask_cleaned, [128, 0, 128][c], processed_image[:, :, c])

# Define the approximate range of intensities for the firing pin drag
lower_threshold_firing_pin_drag = 0.6
upper_threshold_firing_pin_drag = 0.8 

# Create a mask for the firing pin drag
firing_pin_drag_mask = ((gray_image > lower_threshold_firing_pin_drag) &
                        (gray_image <= upper_threshold_firing_pin_drag))

# Clean up the firing pin drag
firing_pin_drag_mask_cleaned = morphology.remove_small_objects(firing_pin_drag_mask, min_size=50)
firing_pin_drag_mask_cleaned = morphology.remove_small_holes(firing_pin_drag_mask_cleaned, area_threshold=50)

# Define the approximate range of intensities for the breech-face impression
lower_threshold_breech = 0.7 
upper_threshold_breech = 1.0  

# Create a mask for the breech-face impression
breech_face_mask = ((gray_image > lower_threshold_breech) & (gray_image <= upper_threshold_breech))

# Clean up the mask
breech_face_mask_cleaned = morphology.remove_small_objects(breech_face_mask, min_size=50)
breech_face_mask_cleaned = morphology.remove_small_holes(breech_face_mask_cleaned, area_threshold=50)

# Define the approximate position and size of the aperture shear
shear_center_x = 330 
shear_center_y = 140  
shear_width = 50     
shear_height = 20    

# Create a mask for the aperture shear
aperture_shear_mask = np.zeros_like(gray_image, dtype=bool)
aperture_shear_mask[shear_center_y-shear_height//2:shear_center_y+shear_height//2,
                    shear_center_x-shear_width//1:shear_center_x+shear_width//2] = True

# Define the approximate range of intensities for the firing pin impression
lower_threshold_firing_pin = 0.2  
upper_threshold_firing_pin = 0.4  

# Create a mask for the firing pin impression
firing_pin_impression_mask = ((gray_image > lower_threshold_firing_pin) & (gray_image <= upper_threshold_firing_pin))

# Clean up the mask
firing_pin_impression_mask_cleaned = morphology.remove_small_objects(firing_pin_impression_mask, min_size=50)
firing_pin_impression_mask_cleaned = morphology.remove_small_holes(firing_pin_impression_mask_cleaned, area_threshold=50)

# Define the approximate range of intensities for the firing pin drag
lower_threshold_firing_pin_drag = 0.35
upper_threshold_firing_pin_drag = 0.5  

# Create a mask for the firing pin drag based
firing_pin_drag_mask = ((gray_image > lower_threshold_firing_pin_drag) & (gray_image <= upper_threshold_firing_pin_drag))

# Clean up the mask
firing_pin_drag_mask_cleaned = morphology.remove_small_objects(firing_pin_drag_mask, min_size=50)
firing_pin_drag_mask_cleaned = morphology.remove_small_holes(firing_pin_drag_mask_cleaned, area_threshold=50)

# Apply the masks for breech-face, aperture shear, firing pin impression, and firing pin drag
processed_image = before_image.copy()

for c in range(3):
    processed_image[:, :, c] = np.where(breech_face_mask_cleaned, [255, 0, 0][c], processed_image[:, :, c])

for c in range(3):
    processed_image[:, :, c] = np.where(aperture_shear_mask, [0, 255, 0][c], processed_image[:, :, c])

for c in range(3):
    processed_image[:, :, c] = np.where(firing_pin_impression_mask_cleaned, [171, 0, 128][c], processed_image[:, :, c])

for c in range(3):
    processed_image[:, :, c] = np.where(firing_pin_drag_mask_cleaned, [0, 191, 255][c], processed_image[:, :, c])

center_x = before_image.shape[1] // 2
center_y = before_image.shape[0] // 2

# Define the direction of the firing pin drag arrow
arrow_length = 70  
arrow_angle = 290  

end_x = int(center_x + arrow_length * np.cos(np.radians(arrow_angle)))
end_y = int(center_y - arrow_length * np.sin(np.radians(arrow_angle)))

# Draw the arrow on the processed image
cv2.arrowedLine(processed_image, (center_x, center_y), (end_x, end_y), [0, 0, 255], thickness=5, tipLength=0.3)

# Save the final image
output_image_path = ('D:/Users/sahil/Documents/PROJECTS/forensic_image_processor/cartridge_case_images_processed/case_image_processed.jpg')
io.imsave(output_image_path, processed_image)

# Display the processed image
plt.imshow(processed_image)
plt.axis('on')
plt.show()

# Mohmed Shaikh Jan-2024