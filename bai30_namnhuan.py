#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 18:07:38 2024

@author: nguyenthiphuongvan2005
"""

#bai30_Viếtchươngtrìnhnhậpvàothángnăm.Hãychobiếtthángđócóbaonhiêu ngày? (Để kiểm tra năm nhuận Dương lịch, bạn lấy năm đó chia cho 4. 
#Nếu chia hết cho 4 thì năm đó là năm nhuận. Với các năm tròn thế kỷ, có 2 số 00 ở cuối thì lấy số năm chia cho 400. 
#Nếu chia hết cho 400 thì là năm nhuận ~ Năm nhuận là năm chia hết cho 4 và không chia hết cho 100 hoặc chia hết cho 400)


month = 0
year = 0
# Sử dụng vòng lặp để yêu cầu nhập tháng và năm hợp lệ
while month < 1 or month > 12:
    month = int(input("Nhập tháng (1-12): "))
    if month < 1 or month > 12:
        print("Tháng không hợp lệ. Vui lòng nhập lại.")

year = int(input("Nhập năm: "))

# Kiểm tra năm nhuận
nhuan = False
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    nhuan = True

# Xác định số ngày trong tháng
if month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31  # Tháng có 31 ngày
elif month in [4, 6, 9, 11]:
    days = 30  # Tháng có 30 ngày
elif month == 2:
    if nhuan:
        days = 29  # Tháng 2 trong năm nhuận
    else:
        days = 28  # Tháng 2 trong năm không nhuận

print(f"Tháng {month} năm {year} có {days} ngày.")
