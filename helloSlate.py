from io import  BytesIO
import slate,time

def write_txt_file(txtName, str):
    file_name = txtName
    with open(file_name, 'w') as x_file:
        x_file.write(str)


scrape = open("testdoc.pdf", 'rb') # for local files
    #scrape = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf") # for external files
pdfFile = BytesIO(scrape.read())

with pdfFile as f:
    doc = slate.PDF(f)
write_txt_file("slateResult"+time.strftime("%Y%m%d-%H%M%S")+".txt", ''.join(doc[0]))
# write_txt_file("slateResult"+time.strftime("%Y%m%d-%H%M%S")+".txt", ' '.join(doc))

# print(doc[0])



