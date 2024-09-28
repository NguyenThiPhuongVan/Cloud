# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 10:50:40 2024

@author: Student
"""

#bai35_Tính S = 1 + 2 + 3 + ... + n (n nguyên và lớn hơn 0)

s=0
n= int(input("Nhap n: "))
while n <= 0:
    n= int(input("Nhap lai n: "))
for i in range(1, 1+n):
    s += i
print(s) 
    