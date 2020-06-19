import pyqrcode
import png

url = "www.google.com"

qr_code = pyqrcode.create(url)

qr_code.svg("QR.svg", scale=10)

qr_code.png("QR.png", scale=6)
