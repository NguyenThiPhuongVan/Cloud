#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 18:02:56 2024

@author: nguyenthiphuongvan2005
"""

#bai32_Viết chương trình tính tiền cước TAXI. Biết rằng: 1 km đầu tiên là 15000đ, từ km thứ 2 đến thứ 5 giá là 13500đ, 
#từ km thứ 6 giá là 11000đ, nếu đi hơn 120km thì sẽ được giảm 10% trên tổng tiền.

km = float(input("nhập số km đi được: "))
tien = 0
if km==1:
    tien = 15000
    print("số tiền:", tien)
elif 2<=km<=5:
    tien = 15000 + (km-1)*13500
    print("số tiền:", tien)
elif km>=6:
    tien = 15000 + 4*13500 + (km-5)*11000
    print("số tiền:", tien)
if km>120:
    tien = (15000+ 4*13500 + (km-5)*11000)*0.9
    print("số tiền được giảm 10% là:", tien)
    