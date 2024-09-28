# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 09:31:22 2024

@author: Student
"""

#bai42

s= 0 
n= int(input("Nhap n: "))
while n <= 0:
    n= int(input("Nhap lai n: "))
    
for i in range(1, n+1):
    s += 1 / i * (i + 1)
print(round(s,2)) 