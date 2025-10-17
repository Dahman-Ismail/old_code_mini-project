
# Install all dependencies for the QR Code app
# !pip install pyqrcode
# !pip install pypng
# !pip install pillow
# !apt-get install -y libzbar0  # installs the native ZBar library required by pyzbar
# !pip install pyzbar

import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

# Create a QR code
qr = pyqrcode.create("Coding With Evan")
qr.png('myCode.png', scale=8)

# Decode the QR code
d = decode(Image.open('myCode.png'))
print(d[0].data.decode('ascii'))
