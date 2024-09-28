# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 09:20:53 2024

@author: PhuongVan
"""

#bai45_Tính

s= 0 
ts= 1
ms= 0
n= int(input("Nhap n: "))
while n <= 0:
    n= int(input("Nhap lai n: "))
x= float(input("Nhap x: "))

for i in range(1, n+1):
    ts= x**i
    ms= ms + i
    s += ts/ms
print(round(s,2))