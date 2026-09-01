#This program reads and displays the contents
# of the philosophers.txt file.
def main():
    #Open the philosophers.txt file for reading.
    infile = open('philosophers.txt', 'r')

    #Read the file's contents.
    file_contents = infile.read()

    #Close the file.
    infile.close()

    #Display the contents that were read from the file.
    print(line1, end='')
    print(line2, end='')
    print(line3, end='')