from asyncio import constants
from ensurepip import version
import qrcode 

#qr code for my linkedin profile (Sercan Efe Karaman, UI UX Designer)

code = qrcode.QRCode(
    version = 1,
    box_size = 50,
    border = 2
    )     

code.add_data("https://www.linkedin.com/in/sercan-efe-karaman-30055a210/")
code.make(fit = True)

image = code.make_image(fill_color="black",back_color="white")
image.save("qr1.png")