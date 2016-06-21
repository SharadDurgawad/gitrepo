__author__ = 'dell'

try:
    fp = open("file.txt", "r")
    fp.write("This is the first line of the file")
except IOError:
    print("\n Can't find file or data")
else:
    print("\n Data has been written successfully!!!")
    fp.close()
