# Image_Fixer_GoogleIT
This is my code to manipulate images in a folder.

I had to add some parameters because of an error that it was being raised.

Before the for loop, make sure you add an if statement:

if image_file != ".DS_Store":

I also had to change the last line:

new_image.convert("RGB")
new_image.save(os.path.join(output_dir,image_file+".jpeg")
