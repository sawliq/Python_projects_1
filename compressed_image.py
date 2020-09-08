from PIL import Image,ImageFilter
img=Image.open(r"C:\\Users\\syeds\\Downloads\\astro.jpg")
img.thumbnail((400,400))
img.save("Compressed_astro.png",'png')
print(img.size )   #returns the suitable value for compression

 