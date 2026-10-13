import qrcode
qr  =  qrcode.make("https://www.linkedin.com/in/omraje-ambure-589294246/",box_size=3)
qr.resize((300,300))
qr.save("qr.png")