import qrcode

#code = qrcode.make('https://www.youtube.com/watch?v=615G3XshjFI')
#code.save('vol1.png')

code = qrcode.QRCode(
    version=1,
    error_correction = qrcode.ERROR_CORRECT_L,
    box_size=50,
    border=2
)

code.add_data('https://www.youtube.com/watch?v=615G3XshjFI')
code.make(fit=True)

image = code.make_image(fill_color="red",back_color="black")
image.save('vol2.png')
