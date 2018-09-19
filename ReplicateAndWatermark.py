from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape

out_folder = "C:\\Users\\DanFang\\Desktop"
os.chdir(out_folder)

original_doc = PdfFileReader(open('hwccopy1.pdf', 'rb'))
output = PdfFileWriter()


packet = io.BytesIO()
new_canvas = canvas.Canvas(packet, pagesize=landscape(letter))


for page in range(37, 47):
    new_canvas.setFont('Helvetica', 10)
    string = '09180' + str(page).zfill(2)
    new_canvas.drawString(290, 18, str(string))
    new_canvas.showPage()

new_canvas.save()


packet.seek(0)
new_pdf = PdfFileReader(packet)

for i in range(0, 10):
    page = original_doc.getPage(i)
    #page = new_pdf.getPage(i)
    page.mergePage(new_pdf.getPage(i))
    output.addPage(page)

output_stream = open('hwc_addl_20.pdf', 'wb')
output.write(output_stream)
output_stream.close()
