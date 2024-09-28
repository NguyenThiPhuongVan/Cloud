#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:41:58 2024

@author: nguyenthiphuongvan2005
"""

#bai33_Viết chương trình nhập vào số nguyên dương n. Kiểm tra xem n có phải là số chính phương hay không? 
#(Số chính phương là số khi lấy căn bậc 2 có kết quả là nguyên).


import math 
n= int(input("Nhập số nguyên dương n: "))
while n<=0:
    n= int(input("Nhập lại n: "))
A= math.sqrt(n)
if n==A**2:
    print (f"{n} là số chính phương")
else:
    print ("không phải số chính phương")

    
           
           
    
           
    

             