import cv2
import numpy as np
import os

def remove_background_and_add_white_background(input_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        # Check for image file extensions
        if filename.lower().endswith(('.png', '.jpg', '.jpeg','.webp')):
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)

            # Read the image
            image = cv2.imread(input_image_path)
            if image is None:
                print(f"Could not read image: {input_image_path}")
                continue
            
            # Convert to RGB (OpenCV uses BGR by default)
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Create a mask using a color threshold (adjust the values as needed)
            lower_threshold = np.array([0, 0, 0])  # Lower threshold for black
            upper_threshold = np.array([180, 180, 180])  # Upper threshold for white

            # Create a mask
            mask = cv2.inRange(image_rgb, lower_threshold, upper_threshold)

            # Invert the mask to get the foreground
            mask_inv = cv2.bitwise_not(mask)

            # Create a white background
            white_background = np.ones(image.shape, dtype=np.uint8) * 255

            # Isolate the foreground
            foreground = cv2.bitwise_and(image, image, mask=mask_inv)

            # Combine the foreground with the white background
            result = cv2.add(foreground, cv2.bitwise_and(white_background, white_background, mask=mask))

            # Save the output image
            cv2.imwrite(output_image_path, result)
            print(f"Processed and saved: {output_image_path}")

# Example usage
input_folder = r'D:\projects\drive-download-20241021T042303Z-001\Pharmaceuitical\Scoops\new_scoops'
output_folder = r'D:\projects\drive-download-20241021T042303Z-001\Pharmaceuitical\Scoops\removed'
remove_background_and_add_white_background(input_folder, output_folder)
