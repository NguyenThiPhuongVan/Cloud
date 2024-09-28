# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 08:03:04 2024

@author: PhuongVan
"""

#bai47_Viết chương trình liệt kê tất cả bộ nghiệm nguyên của phương trình sau: 2x + 7y + 9z = 979 với x, y, z > 0 và x + y + z lớn nhất

lon_nhat = 0
bo_nghiem = 0
for x in range (1, 490):
    for y in range (1, 140):
        for z in range (1, 109):
            if 2*x + 7*y + 9*z == 979:
                tong = x + y + z
                if tong > lon_nhat:
                    lon_nhat = tong 
                    bo_nghiem = (x,y,z)
                
if bo_nghiem:
    print(f'{bo_nghiem} voi {x + y + z} = {lon_nhat}')
