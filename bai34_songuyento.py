#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:55:10 2024

@author: nguyenthiphuongvan2005
"""

#bai34_Viết chương trình nhập vào số nguyên dương n. Kiểm tra xem n có phải là số nguyên tố hay không?

n = int(input("Nhập số nguyên dương: "))
while n<=0:
    n = int(input("Nhập lại:"))
if n <2:
    print("Không phải là số nguyên tố: ")
else:
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            print("Không phải là số nguyên tố")
            break 
    else:
            print("Là số nguyên tố")
            