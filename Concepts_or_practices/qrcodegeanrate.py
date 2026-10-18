import qrcode
qr  =  qrcode.make("https://github.com/OmrajeAmbure/IB_2026/tree/main/Tasks",box_size=3)
qr.resize((300,300))
qr.save("IB_Tasks_Code.png")