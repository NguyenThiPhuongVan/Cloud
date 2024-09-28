# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 09:54:52 2024

@author: Student
"""

#bai39

s= 0 
n= int(input("Nhap n: "))
while n <= 0:
    n= int(input("Nhap lai n: "))
    
for i in range(1, n+1):
    s += 1 / i 
print(round(s,2)) 