# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BhoAO0TKalib-6D20H3ab7jjAlA5-oti

***Random Number Generater***
"""

# importing the random module
import random

num=random.randint(0000,1999)
print(num)

enter_val=int(input("enter pin number: "))

if enter_val==num:
  print("your OTP is valid")
else:
  print("your OTP is Invalid")