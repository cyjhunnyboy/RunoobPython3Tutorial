# -*- coding: UTF-8 -*-
# author: chen_yong_jun

n = 100
sums = 0
counter = 1
while counter <= n:
    sums = sums + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sums))

