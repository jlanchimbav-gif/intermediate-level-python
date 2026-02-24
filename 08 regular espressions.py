## regular expressions ##
import re
from tokenize import group

my_string=" hola , esta es la leccion 8 de nivel intermedio de python"
my_other_string="esta no es una leccion 5 de nivel principiante de python"

re.match(" esta es la leccion 8", my_string)
re.search(" esta es la leccion 8", my_string)
print(re.search(" esta es la leccion 8", my_string))
print(re.search(" esta es la leccion 8", my_other_string))

print(re.search(" esta es la leccion 8", my_string).span())

match=re.match(" esta es la leccion 8", my_string)
print(match)
if not match==None:
    print(match)
    start,end=match.span()
    print(start,end)
    print(match.group())
    
## search ##
search=re.search(" esta es la leccion 8", my_string)
print(search)
if not search==None:
    print(search)
    start,end=search.span()
    print(start,end)
    print(search.group())
    
## findall ##
findall=re.findall(" esta es la leccion 8", my_string)    
print(findall)

## split ##
split=re.split(" ", my_string)
print(split)

## sub ##
sub=re.sub(" ", "-", my_string)
print(sub)

## patterns ##
patterns=r"[lL]eccion"
findall=re.findall(patterns, my_string)
print(findall)

patterns=r"[lL]eccion|expresiones"
findall=re.findall(patterns, my_string)
print(findall)

patternsr=r"[0-9]"
findall=re.findall(patternsr, my_string)
print(findall)

email=" jlanchimbav@uneme.edu.ec"
patternsemail=r"[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+"
findall=re.findall(patternsemail, email)
print(findall)
