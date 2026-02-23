## file handling ##

import os
from zipfile import ZipFile

#.text file 
#txt_file=open("intermediate-level-python/my_file.txt","w+")##


txt_file=open(r"C:\Users\lanch\.vscode-R\intermediate-level-python\07 file handling.txt","r+")
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

os.remove(r"C:\Users\lanch\.vscode-R\intermediate-level-python\my_file.txt")

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