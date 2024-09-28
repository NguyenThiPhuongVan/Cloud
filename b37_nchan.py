# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 10:14:15 2024

@author: Student
"""

#bai37_Tính S = 2 + 4 + 6 + ... + n  (với n chẵn > 0)

s= 0 
n= int(input("Nhap n: "))
while n % 2 != 0 or n <= 0:
    n= int(input("Nhap lai n: "))

for i in range (2,1+n,2):
    s += i 
print(s)
    