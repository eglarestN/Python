import pyqrcode

from pyqrcode import QRCode

s = input("enter a url: ")

url = pyqrcode.create(s)

url.svg("myqr.svg", scale=8)

url.png("myqr.png", scale=8)
