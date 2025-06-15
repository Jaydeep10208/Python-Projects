import PyPDF2
pdfiles = ["1.pdf", "2.pdf"]
mereger = PyPDF2.PdfMerger()

for filename in pdfiles:
    pdfile= open(filename, "rb")
    pdfReader = PyPDF2.PdfReader(pdfile)
    mereger.append(pdfReader)
# pdfiles.close()
mereger.write("merged.pdf")