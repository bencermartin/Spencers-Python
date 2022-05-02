from PyPDF2 import PdfFileReader, PdfFileWriter
pdf_file_path = 'Paper.pdf'
pdf = PdfFileReader(pdf_file_path)
pdfwriter = PdfFileWriter()
for page_num in range(2,10):
    pdfwriter.addPage(pdf.getPage(page_num))
with open('NewPDF.pdf', 'wb') as out:
    pdfwriter.write(out)
print('PDF file has been split')

