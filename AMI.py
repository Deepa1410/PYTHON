import qrcode
text="Hello AMI this is deepa"
r=qrcode.QRCode()
r.add_data(text)
r.make(fit=True)
img=r.make_image(fill_color="black",back_color="white")
img.save("day8.png")
