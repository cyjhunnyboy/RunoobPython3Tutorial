# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数据结构
        将列表当作队列使用
            也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；
            但是拿列表用作这样的目的效率不高。在列表的最后添加或者弹出元素速度快，
            然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）
"""
from collections import deque

if __name__ == "__main__":
    queue = deque(["Eric", "John", "Michael"])
    print(queue)

    # Terry arrives
    queue.append("Terry")
    # Graham arrives
    queue.append("Graham")
    print(queue)

    # The first to arrive now leaves
    queue.popleft()
    print(queue)

    # The second to arrive now leaves
    queue.popleft()
    # Remaining queue in order of arrival
    print(queue)
