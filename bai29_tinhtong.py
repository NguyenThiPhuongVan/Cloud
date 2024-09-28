#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 18:11:16 2024

@author: nguyenthiphuongvan2005
"""

#bai29_Tính tổng các chữ số N nguyên dương. (Nhập N = 6789 thì 6+7+8+9 = 30)

n = int(input("nhập n:"))
tong = 0
while n>0:
    tong +=  n%10
    n = n // 10
print("kết quả là:", tong)
