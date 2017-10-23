from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO, BytesIO
import time

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()  #
    codec = 'utf-8'
    laparams = LAParams()
    laparams.all_texts = True

    # laparams.all_texts = False
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)

    interpreter = PDFPageInterpreter(rsrcmgr, device)   #
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
        # print(i)
    pages = PDFPage.get_pages(
        pdfFile, pagenos,
        maxpages=maxpages,
        password=password,
        caching=caching,
        check_extractable=True)

    for i, page in enumerate(pages):
        # if i==2:
        #     print(retstr.getvalue())
        retstr.write("-------------------ahihi-------------------------")
        interpreter.process_page(page)


    device.close()
    textstr = retstr.getvalue()
    retstr.close()
    return textstr

def write_txt_file(txtName, str):
    file_name = txtName
    with open(file_name, 'w') as x_file:
        x_file.write(str)

if __name__ == "__main__":
    scrape = open("testdoc.pdf", 'rb') # for local files
    #scrape = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf") # for external files
    pdfFile = BytesIO(scrape.read())
    outputString = readPDF(pdfFile)
    # print(outputString)
    write_txt_file("result"+time.strftime("%Y%m%d-%H%M%S")+".txt", outputString)
    pdfFile.close()


# def pdf_to_csv(filename):
#     from io import StringIO
#     from pdfminer.converter import LTChar, TextConverter
#     from pdfminer.layout import LAParams
#     from pdfminer.pdfparser import PDFParser,PDFDocument
#     from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
#
#     class CsvConverter(TextConverter):
#         def __init__(self, *args, **kwargs):
#             TextConverter.__init__(self, *args, **kwargs)
#         def end_page(self, i):
#             from collections import defaultdict
#             lines = defaultdict(lambda : {})
#             for child in self.cur_item._objs:                #<-- changed
#                 if isinstance(child, LTChar):
#                     (_,_,x,y) = child.bbox
#                     line = lines[int(-y)]
#                     line[x] = child._text.encode(self.codec) #<-- changed
#
#             for y in sorted(lines.keys()):
#                 line = lines[y]
#                 self.outfp.write(";".join(line[x] for x in sorted(line.keys())))
#                 self.outfp.write("\n")
#
#     # ... the following part of the code is a remix of the
#     # convert() function in the pdfminer/tools/pdf2text module
#     rsrc = PDFResourceManager()
#     outfp = StringIO()
#     device = CsvConverter(rsrc, outfp, codec="utf-8", laparams=LAParams())
#         # becuase my test documents are utf-8 (note: utf-8 is the default codec)
#
#     doc = PDFDocument()
#     fp = open(filename, 'rb')
#     parser = PDFParser(fp)
#     parser.set_document(doc)
#     doc.set_parser(parser)
#     doc.initialize('')
#
#     interpreter = PDFPageInterpreter(rsrc, device)
#
#     for i, page in enumerate(doc.get_pages()):
#         outfp.write("START PAGE %d\n" % i)
#         if page is not None:
#             interpreter.process_page(page)
#         outfp.write("END PAGE %d\n" % i)
#
#     device.close()
#     fp.close()
#
#     return outfp.getvalue()