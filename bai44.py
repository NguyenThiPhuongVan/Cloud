# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 09:25:26 2024

@author: PhuongVan 
"""

#bai44

s= 0 
n= int(input("Nhap n: "))
while n <= 0:
    n= int(input("Nhap lai n: "))
    
for i in range(1, n+1):
    s += (2*i + 1)/ (2*i + 2)
print(round(s,2))