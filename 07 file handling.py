## file handling ##

import os
from zipfile import ZipFile

#.text file 
#txt_file=open("intermediate-level-python/my_file.txt","w+")##


txt_file=open(r"C:\Users\lanch\.vscode-R\intermediate-level-python\07 file handling.txt","w+")
txt_file.write("mi nombre es Jorge Alejandro\nmis apellidos son Lanchimba Vivas\n26 años"
               "\nidiomas ruso y ingles/naprendiendo python y java\naprendiendo python y java")

#print(txt_file.read())#aprendiendo python y java

#print(txt_file.readline())#
print(txt_file.readlines())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nSoy estudiante de ingenieria")
txt_file.seek(0)
print(txt_file.readline())

txt_file.close()

#os.remove(r"C:\Users\lanch\.vscode-R\intermediate-level-python\my_file.txt")

# jso file ##

import json
json_file=open(r"C:\Users\lanch\.vscode-R\intermediate-level-python\my_file.json","w+")

json_test={
     "name":"Jorge Alejandro",
     "surname":"Lanchimba Vivas",
     "edad":26,
     "idiomas":["ruso","ingles"],
     "aprendiendo":["python","java"]
     }

json.dump(json_test,json_file, indent=4)

json_file.close()

with open(r"C:\Users\lanch\.vscode-R\intermediate-level-python\my_file.json","r") as json_file:
    data=json.load(json_file)
    print(data)
    
json_dict=json.loads(json.dumps(json_test))
print(json_dict)    
print(type(json_dict))

# csv file ##
import csv
csv_file=open(r"C:\Users\lanch\.vscode-R\intermediate-level-python\my_file.csv","r+")

csv_writer=csv.writer(csv_file)
csv_writer.writerow(["name","surname","edad","idiomas","aprendiendo"])
csv_writer.writerow(["Jorge Alejandro","Lanchimba Vivas",26,"ruso","python"])

json_file.close()

with open(r"C:\Users\lanch\.vscode-R\intermediate-level-python\my_file.csv","r") as csv_file:
    csv_reader=csv.reader(csv_file)
    for line in csv_reader:
        print(line)
## xlsx file ##
## import ## debe intalar modulo 

## xml file ##
import xml
