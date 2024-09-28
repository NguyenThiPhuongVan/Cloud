# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 09:29:06 2024

@author: Student
"""

#bai43 

s= 0 
n= int(input("Nhap n: "))
while n <= 0:
    n= int(input("Nhap lai n: "))
    
for i in range(1, n+1):
    s += i / (i + 1)
print(round(s,2)) 
