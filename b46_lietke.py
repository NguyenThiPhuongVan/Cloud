# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 07:58:20 2024

@author: PhuongVan
"""

#bai46_Viết chương trình liệt kê tất cả bộ nghiệm nguyên của phương trình sau: 2x + 7y + 9z = 979 với (x, y, z > 0)


# 2*x + 7*y + 9*2 = 979
# tim x: cho y, z = 1:
# 2*x + 7*1 + 9*1 = 979 => x = （979-（7+9））/2= 485.5
# 2*1 + 7*y + 9*1 = 979 => x = （979-（2+9））/7= 138.5
# 2*1 + 7*1 + 9*2 = 979 => x= （979- （2+7））/9= 108.7

ds =[]
for x in range (1, 490):
    for y in range (1, 140):
        for z in range (1, 109): 
            if 2*x + 7*y + 9*z == 979:
                ds += [(x,y,z)]
if ds: 
    print(f'{ds}')
                