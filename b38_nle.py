# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 09:55:35 2024

@author: Student 
"""

#bai38_Tính S = 1 * 2 * 3 * ... * n  (với n lẻ > 0)

s=1
n= int(input("Nhap n: "))
while n % 2 == 0 or n <= 0:
    n= int(input("Nhap lai n: "))
for i in range(1, 1+n):
    s*= i
print(s)
  

    
    