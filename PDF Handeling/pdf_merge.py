import PyPDF2

merger = PyPDF2.PdfMerger()

pdf_files = ['sample1.pdf','sample2.pdf'] #Files Name

for pdf_file in pdf_files:
    merger.append(pdf_file)

merger.write("merged_PDF_pages.pdf")   #Merged PDF Name
merger.close()
