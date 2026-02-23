## error types ##

## syntax error ##
## print"hola como estas" # falta un parentesis
print("hola como estas")

## name error ##
language="Ruso y ingles"
print(language)

## index error ##
my_list=["python","Java","sql"]      
print(my_list[2])

## module not found error ##
## import maths
import math

## abtribute error ##
# print(math.PI) # math no tiene un atributo llamado PI, es pi
print(math.pi)

## key error ##
my_dict={"name":"python","version":3.8}
#print(my_dict["neme"]) ## la clave es "name", no "neme"
print(my_dict["name"])

## import error ##
#from math import PI # math no tiene un atributo llamado PI, es pi
from math import pi
print(pi)

## value error ##
#my_int=int("10 años") ## no se puede convertir "10 años" a un entero
my_int=int("10")
print(type(my_int))

## zero division error ##
#print(10/0) ## no se puede dividir por cero
print(10/2)

