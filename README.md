# Forensic Image Processor
For Assessment - Mohmed Shaikh

Example Output: Processed_Example.png
[https://drive.google.com/file/d/1t32csHL-YbYx-tmVqIop8bNHihLFv5PQ]

## Overview

This program is designed to process cartridge case images by masking specific features and adding visual elements. It was created to perform the following tasks:

1. Mask the breech-face impression in red.
2. Mask the aperture shear in green.
3. Mask the firing pin impression in purple.
4. Mask the firing pin drag in light blue.
5. Add a blue arrow indicating the direction of the firing pin drag.

## The program will be updated to specify a region of interest (ROI) within the image, excluding a specified border. The masks and visual elements will then be applied only within the ROI.

## Usage

1. **Input Image**: Place your cartridge case image in the same directory as the program and name it `case_image_original.jpg`.

2. **Configuration**: You can configure the program by adjusting the parameters in the code to match the specific characteristics of your images. # This will be updated with dynamic code

3. **Run the Program**: Execute the program, and it will process the input image based on the defined masks and visual elements.

4. **Output**: The processed image will be saved as `case_image_processed.jpg` in the same directory as the program.

## Dependencies

This program uses the following libraries:

- NumPy
- scikit-image (skimage)
- Matplotlib
- OpenCV (cv2)

You can install these libraries using pip if needed:

```bash
pip install numpy scikit-image matplotlib opencv-python
