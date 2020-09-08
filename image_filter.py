from PIL import Image,ImageFilter
img=Image.open(r"C:\\Users\\syeds\\Downloads\\charmander.jpg")
filtered_image=img.filter(ImageFilter.SMOOTH)     #you can SHARPEN , BLUR and more
filtered_image.save("BLUR.png",'png')
