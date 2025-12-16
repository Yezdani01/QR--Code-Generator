import qrcode

url = input("Enter the URL: ")
filename = input("You want to save it as: ")
if not (filename.endswith(".png")):
    filename = filename + ".png"

image = qrcode.make(url)
image.save(filename)
