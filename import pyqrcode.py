import pyqrcode

qr_url = 'https://www.linkedin.com/in/eduardo-%C3%A2ngelo-4902611a2/'

qr_code = pyqrcode.create(qr_url)

qr_code.svg(
    'qrcode.svg',
    scale=8,
)