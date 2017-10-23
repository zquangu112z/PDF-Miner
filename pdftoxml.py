from xml.etree import ElementTree
from pprint import pprint
import os

def main():
    print("Calling PDFDUMP.py")
    os.system("dumppdf.py -a aaa.pdf > out.xml")

    # Preprocess the file to eliminate bad XML.
    print( "Screening the file")
    o = open("output.xml","w") #open for append
    for line in open("out.xml"):
       line = line.replace("&#", "Invalid_XML") #some bad data in xml for formatting info.
       o.write(line)
    o.close()

    print( "Opening XML output")
    tree = ElementTree.parse('output.xml')
    lastnode = ""
    lastnode2 = ""
    list = {}
    entry = {}

    for node in tree.iter(): # Run through the tree..
        # Check if New node
        if node.tag == "key" and node.text == "T":
            lastnode = node.tag + node.text
        elif lastnode == "keyT":
            for child in node.iter():
                entry["ID"] = child.text
            lastnode = ""

        if node.tag == "key" and node.text == "V":
            lastnode2 = node.tag + node.text
        elif lastnode2 == "keyV":
            for child in node.iter():
                if child.tag == "string":
                    if entry.has_key("ID"):
                        entry["Value"] = child.text
                        list[entry["ID"]] = entry["Value"]
                        entry = {}
            lastnode2 = ""

    pprint(list)

if __name__ == '__main__':
  main()