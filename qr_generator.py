import pyqrcode

import png

from pyqrcode import QRCode

link = 'https://www.instagram.com/clout_maison/?hl=bg'

url = pyqrcode.create(link)
url.png('clout_maison.png', scale=8)