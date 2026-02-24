## python package manager ##
from importlib.resources import path
from unittest import result
from urllib import response

import numpy
print(numpy.__version__)

numpy_arr=numpy.array([1,2,3,4,5])
print(numpy_arr)
print(type(numpy_arr))

import pandas
print(pandas.__version__)

pandas_df=pandas.DataFrame({'Name':['Alejandro','Elisa'],'Age':[26,27]})
print(pandas_df)
print(type(pandas_df))

import requests
print(requests.__version__)

response=requests.get('https://www.google.com')
print(response.status_code)

## jaguar package ##

from ew_package import arithmetics
print(arithmetics.sum_two_numbers(5,10))
print(arithmetics.multiply_two_numbers(5,10))

