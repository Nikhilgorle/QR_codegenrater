import pyqrcode
import png
from pyqrcode import QRCode

# string which represent the QR code
s="https://bard.google.com/chat"

# Generate QR code
url=pyqrcode.create(s)

# save the png file
url.svg("temp.svg",scale=5)
url.png("bard.png",scale=5)

import os
os.remove("temp.svg")