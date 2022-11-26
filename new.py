from PyPDF2 import PdfMerger

merger = PdfMerger()

for pdf in ["Django-3.pdf", "cv.pdf"]:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()
