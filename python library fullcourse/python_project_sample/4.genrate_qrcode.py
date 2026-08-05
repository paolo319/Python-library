import qrcode

url = input("Enter the Url: ").strip()
file_path = "C:\\Users\\Paolo\\OneDrive\\Desktop\\python library fullcourse\\qrcode_sample\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR code has successfully generated")
