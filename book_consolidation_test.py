import csv
import os
from operator import itemgetter
"""
This first block gets current working directory into cwd. Then uses the cwd to join and make
a new path using os.path.join for the "Sci-Fi Books" folder.  It then prints the current
directory and lists all the files in the directory.
"""

cwd = os.getcwd()  # Get the current working directory (cwd)
print("\n \n", cwd)
print("\n")
directory = os.path.join(cwd, "Sci-Fi Books")
listfiles = os.listdir(directory)  # Get all the files in that directory
print("Files in %r: %s" % (directory, listfiles))
print("\n \n \n")
print(directory)

"""
goal:
Create NEW csv file.  If run again enumerate and create a new file. for ex. csv0, if csv0 is
already created create csv1 and so on and so forth.

Once created we will use existing read loop to edit at the same time organizing it line by
line alphabetically.
"""
x = 0
new_csv_path = os.path.join(cwd, "csv" + str(x))

print(new_csv_path)

while os.path.isfile(new_csv_path) == True:
    x+=1
    new_csv_path = os.path.join(cwd, 'csv' + str(x))
    print(new_csv_path)
    
newfile=  open('csv' + str(x), mode = 'x')
newfile.close()
"""
explain for loop and additional functions

"""

for root,dirs,files in os.walk(directory):
    for file in files:
        if file.endswith('.csv'):
            print('File name: ', file)
            filepath=os.path.join(directory, file)
            print('File path: ', filepath, '\n')

            append_all= []

            #open file to be read
            with open(filepath, mode= 'r', encoding= 'utf-8', newline= '') as f:
                for line in f:
                        append_all.append(line.split(','))

            # for line in append_all[:5]:
            #     print(line)


            
            # addlines = [line for line in csv.reader(f)]

            # print(f"This is the number of lines in each excel doc: {len(addlines)}\n")
            
            # #open file to be written to
            # print(new_csv_path)
            # csvappend = open(new_csv_path, mode= 'w', encoding= 'utf-8', newline= '')
            
            # csv.writer(csvappend).writerows(addlines)
            


            
            # # initializing the titles and rows list
            # fields = []
            # rows = []

            # #creating a csv reader object
            # csvreader = csv.reader(f)
      
            # #extracting field names through first row
            # fields = next(csvreader)
  
            # #extracting each data row one by one
            # for row in csvreader:
            #     rows.append(row)
                
            # #get total number of rows
            # print("Total no. of rows: %d"%(csvreader.line_num))
  
            # # printing the field names
            # print('Field names are: ' + ', '.join(field for field in fields))
  
            # # printing first 5 rows
            # print('\nFirst 5 rows are:\n')
            # for row in rows[:5]:
            #     #parsing each column of a row
            #     for col in row:
            #         print("%10s"%col),
            #     print('\n')
            

            print('-------------------- CSV FILE END --------------------\n\n')
            # csvappend.close()
            f.close()
            
with open(new_csv_path, mode= 'w', encoding= 'utf-8', newline= '') as append_file:
    csv.writer(append_file).writerows(append_all)





# with open('studentScores.csv', 'r') as f:
#     data = [line for line in csv.reader(f)]

# newRecord = [Score, Name, Gender, FormGroup, Percentage]
# data.append(newRecord)

# data.sort(key=itemgetter(1))  # 1 being the column number

# with open('studentScores.csv', 'w') as f:
#     csv.writer(f).writerows(data)