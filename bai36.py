# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 10:43:17 2024

@author: Student
"""

#bai36_Tính S = 12 + 22 + 32 + ... + n2 (n nguyên và lớn hơn 0)

s=0
n= int(input("Nhap n: "))
while n <= 0:
    n= int(input("Nhap lai n: "))
for i in range(1,1+n):
    s += i**2
print(s)
    
    
    