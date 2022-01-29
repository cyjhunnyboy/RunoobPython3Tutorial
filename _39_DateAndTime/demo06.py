# -*- coding: UTF-8 -*-
# author: chenyongjun
"""
time.altzone
返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
"""
import time

print("time.altzone %d " % time.altzone)
