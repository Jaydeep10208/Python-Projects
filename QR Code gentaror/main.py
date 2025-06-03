# How to generate QR code using Python

import qrcode
data = "Heloo World"
qr = qrcode.make(data)

qr.save("qrcode.png")
# Display the QR code
print("QR code generated successfully ")