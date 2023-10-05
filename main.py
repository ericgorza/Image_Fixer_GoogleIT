from PIL import Image
import os

## Finding and Creating a List of the Images in the Directory

input_dir = "images" ## THE PATH FOR THE DIRECTORY WITH THE IMAGES - for the ex: ~/images
output_dir = "processed_images" ## THE PATH FOR THE DIRECTORY THAT IT IS GONNA BE CREATED - for the ex: /opt/icons

## Create the new dir just in case:

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

img_directory = os.listdir(input_dir)

##Creating a List of Images:

image_files_list = []

for img in img_directory:
    image_files_list.append(img)

## Creating a loop to manipulate the images:
for image_file in image_files_list:
    #Opening the image

    image_path = os.path.join(input_dir, image_file)
    image = Image.open(image_path)

    #Manipulating the image:

    new_image = image.resize((128,128)).rotate(-90)

    #Creating the output file:

    base_filename, _ = os.path.splitext(image_file)
    new_filename = str(base_filename + ".jpg")
    output_path = os.path.join(output_dir,new_filename)
    new_image.save(output_path, "JPEG")

    #Closing

    image.close()
    new_image.close()