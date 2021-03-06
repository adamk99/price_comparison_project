import csv
import os

"""
This first block gets current working directory into cwd. Then uses the cwd to join and make a new
path using os.path.join for the "Sci-Fi Books" folder.  It then prints the current directory and
lists all the files in the directory.
"""

cwd = os.getcwd()  # Get the current working directory (cwd)
print("\n \n", cwd)
print("\n")
directory = os.path.join(cwd, "Sci-Fi Books")
listfiles = os.listdir(directory)  # Get all the files in that directory
print("Files in %r: %s" % (directory, listfiles))
print("\n \n \n")

print(directory)

x = 0
new_csv_path = os.path.join(cwd, "csv" + str(x))

print(new_csv_path)

while os.path.isfile(new_csv_path) == True:
    x+=1
    new_csv_path = os.path.join(cwd, 'csv' + str(x))
    print(new_csv_path)
    
    
newfile = open('csv' + str(x), mode = 'r+')
newfile.close()

for root,dirs,files in os.walk(directory):
    for file in files:
        if file.endswith('.csv'):
            print('File name: ', file)
            filepath=os.path.join(directory, file)
            print('File path: ', filepath, '\n')
            f = open(filepath, mode= 'r', encoding= 'utf-8') 
            # initializing the titles and rows list
            fields = []
            rows = []
  
            #creating a csv reader object
            csvreader = csv.reader(f)
      
            #extracting field names through first row
            fields = next(csvreader)
  
            #extracting each data row one by one
            for row in csvreader:
                rows.append(row)
  
            #get total number of rows
            print("Total no. of rows: %d"%(csvreader.line_num))
  
            #printing the field names
            print('Field names are: ' + ', '.join(field for field in fields))
  
            #printing first 5 rows
            print('\nFirst 5 rows are:\n')
            for row in rows[:5]:
                #parsing each column of a row
                for col in row:
                    print("%10s"%col),
                print('\n')
            print('-------------------- CSV FILE END --------------------\n\n')
            f.close()