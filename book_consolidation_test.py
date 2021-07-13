# importing csv module
import csv
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
print("\n \n")
  
directory = os.path.join(cwd,"Sci-Fi Books")
for root,dirs,files in os.walk(directory):
    for file in files:
       if file.endswith(".csv"):
           f=open(file, mode= 'r', encoding= 'utf-8')  
           # initializing the titles and rows list
           fields = []
           rows = []
  
           # reading csv file
           with open(filename, mode= 'r', encoding= 'utf-8') as csvfile:
                # creating a csv reader object
                csvreader = csv.reader(f)
      
                # extracting field names through first row
                fields = next(f)
  
                # extracting each data row one by one
                for row in f:
                    rows.append(row)
  
                # get total number of rows
                print("Total no. of rows: %d"%(csvreader.line_num))
  
           # printing the field names
           print('Field names are:' + ', '.join(field for field in fields))
  
           #  printing first 5 rows
           print('\nFirst 5 rows are:\n')
           for row in rows[:5]:
                # parsing each column of a row
                for col in row:
                    print("%10s"%col),
                print('\n')
           f.close()
