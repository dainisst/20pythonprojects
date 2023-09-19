# install pillow if you havent
# import pillow
# open up the image we want to resize using python
# pring the current size of that image
# specify the size we wanna change it to
# save the new resized image

from PIL import Image

def resize_image(size1, size2):

  image = Image.open('test.jpg')

  print(f"current size: {image.size}")

  resized_image = image.resize((size1, size2))

  resized_image.save('test_resized.jpeg')

size1 = int(input("enter width: "))
size2 = int(input("enter height: "))

resize_image(size1, size2)