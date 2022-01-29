# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 输入和输出
pickle 模块
    Python的pickle模块实现了基本的数据序列和反序列化。
    通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
    通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象
    基本接口：
        pickle.dump(obj, file, [,protocol])
    有了pickle这个对象, 就能对file以读取的形式打开:
        x = pickle.load(file)

    注解：从file中读取一个字符串，并将它重构为原来的Python对象。
         file：类文件对象，有read()和readline()接口。
'''
import pprint
import pickle

if __name__ == "__main__":
    # 使用pickle模块从文件中重构Python对象
    pkl_file = open("tmp/data.pkl", "rb")

    data1 = pickle.load(pkl_file)
    pprint.pprint(data1)

    data2 = pickle.load(pkl_file)
    pprint.pprint(data2)

    pkl_file.close()
