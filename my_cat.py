import sys
file_names = sys.argv[1:] #select file names from index 1
result = "" #create a string 
for i in file_names: #for each file (from index = 1) in current directory 
    f = open(i, "r") #open these files
    read = f.read() #read these files
    result+=read #to result add content of all files in one string
print(result, end = "") 
