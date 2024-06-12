import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io
import os
import re

def pdfparser(pdfname, txtname):

    data = ""
    fp = open(pdfname, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data =  retstr.getvalue()

    re.sub("\n!\n", " ", data)
    f = open(txtname, "w")
    f.write(data)
    f.close()

if __name__ == '__main__':
    dir = sys.argv[1]
    for f in os.listdir(dir):
        filename = os.fsdecode(f)
        if filename.endswith("pdf"): 
            pdffile = dir + "/" + filename   
            txtname = pdffile.replace("_pdfs", "_txts").replace(".pdf", ".txt")
            print("Attempting to convert " + pdffile)
            pdfparser(pdffile, txtname)
            print("Converted " + txtname) 

  
