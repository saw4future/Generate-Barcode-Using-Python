##Generate Barcode using python 
import barcode  #pip install python-barcode
from barcode.writer import ImageWriter

#define conent of the barcode as a string 
number = input("Enter the code to generate barcode: ")

#Get the required barcode format 
barcode_format = barcode.get_barcode_class('upc')

#Geenrate barcode and render as image 
my_barcode = barcode_format(number, writer=ImageWriter())

#Save barcode as PNG
my_barcode.save("Generated_barcode")


##To view the generated barcode
from PIL import Image #to open thei barcode and show 
Image.open('Generated_barcode.png')