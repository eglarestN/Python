from pdf2docx import Converter

pdf_file =r"MUHAMMED EMİR YILDIRIM-Siber Güvenlik101.pdf"

docx_file = r"MUHAMMED EMİR YILDIRIM-Siber Güvenlik101.docx"

cv = Converter(pdf_file)

cv.convert(docx_file)

cv.close()