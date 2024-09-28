#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 18:13:22 2024

@author: nguyenthiphuongvan2005
"""

#bai28_Nhập vào số N từ bàn phím (điều kiện N nguyên dương) nếu người dùng nhập không đúng thì bắt nhập lại. 
#Sao đó in ra tất cả ước số của N.

a = int(input("Nhập số nguyên dương: "))
while a <=0:
    a = int(input("Nhập lại:"))
print("các ước số của N là:", )   
for i in range(1,a+1):
    if a%i == 0:
        print(i)
        