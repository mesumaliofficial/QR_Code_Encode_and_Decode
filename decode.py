from pyzbar.pyzbar import decode

from PIL import Image

img = Image.open("C:/Mesum/Python/GIAIC_Projects/Project_5_Assignments/Assignments 01/03_advanced/Project_4_QR_Code_Encoder_and_Decoder/myqrcode.png")

result = decode(img)

print(result)