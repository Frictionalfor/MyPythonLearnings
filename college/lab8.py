"""Packages and Modules"""

#Build-in Modules
import qrcode

data = "https://www.geeksforgeeks.org/python/python-programming-language-tutorial/"
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("lab8(.py)output.png")
print("QR code generated and saved as lab8(.py)output.png")

#Importing a user-defined module
import mymodule

mymodule.greet("Happy")
result = mymodule.add(5, 3)
print("Addition result:", result)
squared = mymodule.square(4)
print("Square result:", squared)


