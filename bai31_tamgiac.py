#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 18:05:44 2024

@author: nguyenthiphuongvan2005
"""

#bai31_Nhập vào ba số nguyên dương. Kiểm tra xem 3 số đó có lập thành tam giác không? 
#Nếu có hãy cho biết tam giác đó thuộc loại nào? (Cân, vuông, đều...).

a = int(input("nhập cạnh a: "))
b = int(input("nhập cạnh b: "))
c = int(input("nhập cạnh c: "))
if a+b>c or a+c>b or b+c>a:
    if a==b==c:
        print("tam giác đều")
    elif a==b or b==c or c==a:
        print("tam giác cân")
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
            print("tam giác vuông")
    else:
        print("tam giác thường")
else:
    print("không phải tam giác")
    
