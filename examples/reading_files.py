import sys

# this will read lines from the standard input
# call it like so: python reading_files.py < somefile.txt
for line in sys.stdin:
    line = line.strip()
    print line


# this will read lines from a file
# call it like so: python reading_files.py somefile.txt
filename = sys.argv[1]
with open(filename, 'r') as infile:
    content = infile.read() # or use infile.readlines() to make an array of lines
print content
