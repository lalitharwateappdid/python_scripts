from wand.image import Image as WandImage
import os
from PIL import Image

def convert_heic_with_wand(heic_path, output_path):
    with WandImage(filename=heic_path) as img:
        img.save(filename=output_path)

def convert_and_resize_images(input_folder, output_folder, size):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        img_path = os.path.join(input_folder, filename)

        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            with Image.open(img_path) as img:
                img = img.resize(size, Image.LANCZOS)
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                new_filename = os.path.splitext(filename)[0] + '.jpg'
                new_img_path = os.path.join(output_folder, new_filename)
                img.save(new_img_path, 'WEBP')
                print(f'Converted and resized: {img_path} -> {new_img_path}')

        elif filename.lower().endswith('.heic'):
            temp_jpg_path = os.path.splitext(img_path)[0] + '.jpg'
            convert_heic_with_wand(img_path, temp_jpg_path)
            with Image.open(temp_jpg_path) as img:
                img = img.resize(size, Image.LANCZOS)
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                new_filename = os.path.splitext(filename)[0] + '.jpg'
                new_img_path = os.path.join(output_folder, new_filename)
                img.save(new_img_path, 'WEBP')
                print(f'Converted HEIC and resized: {img_path} -> {new_img_path}')
            os.remove(temp_jpg_path)  # Clean up temporary file

if __name__ == "__main__":
    input_folder = r'D:\projects\komal_packaging_assets\Pharmaceuitical\Scoops'
    output_folder = r'D:\projects\komal_packaging_assets\Pharmaceuitical\Scoops_resized'
    size = (237, 257)

    convert_and_resize_images(input_folder, output_folder, size)
