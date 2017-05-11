import barcode
from barcode.writer import ImageWriter
ean = barcode.get('upca', '123456789012', writer=ImageWriter())
filename = ean.save('upca')
filename