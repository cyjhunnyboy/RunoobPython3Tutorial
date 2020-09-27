# -*- coding: UTF-8 -*-
# author: chen_yong_jun

# 类似列表推导式，同样集合支持集合推导式(Set comprehension)
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
