# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 09:42:31 2024

@author: Student
"""

#bai40

s= 0 
n= int(input("Nhap n: "))
while n <= 0:
    n= int(input("Nhap lai n: "))
    
for i in range(1, n+1):
    s += 1 / (2 * i)
print(round(s,2)) 