__author__ = 'dell'

try:
    fp = open("file.txt", "w")
    fp.write("Hello World, Bibtya here !!!!")
except IOError:
    print("\n Can't find file or data")
else:
    print("\n Content has been written successfully!!!")
    fp.close()
