from simple_zpl2 import ZPLDocument, QR_Barcode,Code128_Barcode
from PIL import Image
import io
zpl = ZPLDocument()

# zpl.add_field_origin(420, 30)
# qr_data = 'QA,IC/11/2021/007-1 - XXS#210003#4'
# qr = QR_Barcode(qr_data, 2, 6, zpl._QR_ERROR_CORRECTION_STANDARD)
# zpl.add_barcode(qr)



# zpl.add_field_origin(250, 100, '0')
# zpl.add_font('C', zpl._ORIENTATION_NORMAL, 20)
# zpl.add_field_data('Cable Management')

# zpl.add_field_origin(250, 120, '0')
# zpl.add_font('C', zpl._ORIENTATION_NORMAL, 20)
# zpl.add_field_data('Box')

# zpl.add_field_origin(300, 160, '0')
# zpl.add_font('C', zpl._ORIENTATION_NORMAL, 20)
# zpl.add_field_data('10 pcs')

# zpl.add_field_origin(450, 50)
# qr_data = 'QA,{}'.format('LOT-000001')
# qr = QR_Barcode(qr_data, 2, 6, zpl._QR_ERROR_CORRECTION_STANDARD)
# zpl.add_barcode(qr)


# zpl.add_field_origin(50, 50)
# barcode_data = '{}'.format('LOT-000001')
# bc = Code128_Barcode(barcode_data, 'N', 50, 'Y', 'N', 'Y')
# zpl.add_barcode(bc)

zpl.add_field_origin(20, 20)
code128_data = 'TEST BARCODE'
bc = Code128_Barcode(code128_data, 'N', 30, 'Y')
zpl.add_barcode(bc)



# zpl.add_field_origin(20, 20)
# code128_data = 'TEST BARCODE'
# bc = Code128_Barcode(code128_data, 'N', 30, 'Y')
# zpl.add_barcode(bc)

# zpl.add_comment('Style')
# zpl.add_field_origin(390, 30, '0')
# zpl.add_font('C', zpl._ORIENTATION_90, 20)
# zpl.add_field_data('KEMEJA PRIA Biru')

# zpl.add_comment('Style2')
# zpl.add_field_origin(370, 30, '0')
# zpl.add_font('C', zpl._ORIENTATION_90, 20)
# zpl.add_field_data('dan pink hijau')

# zpl.add_comment('Size')
# zpl.add_field_origin(310, 30, '0')
# zpl.add_font('C', zpl._ORIENTATION_90, 40)
# zpl.add_field_data('XL')

# zpl.add_comment('Nama')
# zpl.add_field_origin(270, 30, '0')
# zpl.add_font('C', zpl._ORIENTATION_90, 20)
# zpl.add_field_data('Diana')

# zpl.add_comment('Nama2')
# zpl.add_field_origin(250, 30, '0')
# zpl.add_font('C', zpl._ORIENTATION_90, 20)
# zpl.add_field_data('Diana')

print(zpl.zpl_text)
# Mengatur ukuran kertas label
# png = zpl.render_png(label_width=4, label_height=6)
# file = io.BytesIO(png)
# img = Image.open(file)

# # Membuka gambar dan penampil gambar default di sistem Kamu
# img.show()
