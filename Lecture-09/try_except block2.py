#Get the name of a file.
filename = input("Enter the filename: ")
try:
    #Open the file
    infile = open(filename, 'r')
    #Read the contents of the file
    contents = infile.read()
    #Display the contents of the file
    print(contents)
    #Close the file
    infile.close()
except IOError:
    print('An error occurred trying to read the file.')
    print('the file', filename)

print('End of program')