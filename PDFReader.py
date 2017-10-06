import PyPDF2
import os

out_folder = "C:\\Users\\DanFang\\Desktop\\76ers"
os.chdir(out_folder)


def split_pdf(pdf_file):
    read_file = PyPDF2.PdfFileReader(pdf_file)
    for page_num in range(0, read_file.getNumPages()):
        page = read_file.getPage(page_num)
        page_content = page.extractText()
        seat_location = page_content[(page_content.index('UPPER:') + len('UPPER:')):page_content.index(',')].replace(
            ':', '_')
        section = seat_location[:seat_location.index('_')]
        row_location = seat_location[seat_location.index('_') + 1:]
        row = row_location[:row_location.index('_')]
        if len(row) == 1:
            row = '0' + row
        seat = row_location[row_location.index('_') + 1:]
        if len(seat) == 1:
            seat = '0' + seat
        print(row, seat)
        out_file = PyPDF2.PdfFileWriter()
        out_file.addPage(page)
        with open('split\\' + section + row + seat + '.pdf', 'wb') as file:
            out_file.write(file)


sixers_1 = open('76.pdf', 'rb')
sixers_2 = open('76_2.pdf', 'rb')

split_pdf(sixers_1)
split_pdf(sixers_2)


merger = PyPDF2.PdfFileMerger()
files = [x for x in os.listdir('split')]
for file in sorted(files):
    merger.append(PyPDF2.PdfFileReader(open(os.path.join('split', file), 'rb')))

merger.write("output.pdf")