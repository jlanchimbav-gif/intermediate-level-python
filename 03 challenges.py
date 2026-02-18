## challenges en python ##

"""
EL FAMOSO FIZZBUZZ".
Escribe un programa que muestre por comsola (con un print)los 
números del 1 al 100 (ambos incluidos y con un salto de linea entre 
cada impresion ) sustituyendo los siguientes:
- multiplos de 3 la palabra "fizz"
- multiplos de 5 la palabra "buzz"
- multiplos de 3 y 5 la palabra "fizzbuzz". # type: ignore
"""

def fizzbuzz():
    for index in range(1, 101):
       if index % 3 == 0 and index % 5 == 0:
             print("fizzbuzz")
       elif index % 3 == 0:
            print("fizz")
       elif index % 5 == 0:
            print("buzz")
       else:
            print(index)
fizzbuzz()

"""
Escribe una funcion que reciba dos palabras (strings) y que devuelva 
verdadero o falso (bolt) segun sean anagrmas o no
- Un anagrama consiste en formar una palabra reordenando TODAS las letras de otra
palabra inicila.
No hace falta comprobar que ambas palabras existan.
Dos palabras iguales no son anagramas.
"""       
 
def is_anagram(word_one, word_two):
   if word_one == word_two:
        return False
   return sorted(word_one) == sorted(word_two)
   
print(is_anagram("roma","ramo")) 

""""
LA SUSECION DE FIBONACCI
Escribe un programa que inmprima los primeros 50 numeros de la susecion 
de fibonacci empezando por el 0.
- La serie de fibonacci se compone por una sucesion de numeros en la que cada numero es la suma de los dos anteriores.
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
"""

def fibonacci(): 
    
    prev=0
    next=1   
           
    for index in range(0, 51):
        print(index)
        fib = prev + next
        prev = next
        next = fib
         
         
fibonacci()        

""""
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automatica.
- si le pasamos "hola mundo" nos debe devolver "odnum aloh"
"""
def reverse_string(string):
    reversed_string = ""
    for index in range(len(string)-1, -1, -1):
        reversed_string += string[index]
    return reversed_string

print(reverse_string("hola mundo"))