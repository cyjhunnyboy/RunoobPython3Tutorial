# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 OS 文件/目录方法
 os.chflags() 方法
 描述：
    os.chflags()方法用于设置路径的标记为数字标记。多个标记可以使用OR来组合起来。
    只支持在Unix下使用。
语法：
    os.chflags(path, flags)
    参数：
        path -- 文件名路径或目录路径。
        flags -- 可以是以下值：
            stat.UF_NODUMP: 非转储文件
            stat.UF_IMMUTABLE: 文件是只读的
            stat.UF_APPEND: 文件只能追加内容
            stat.UF_NOUNLINK: 文件不可删除
            stat.UF_OPAQUE: 目录不透明，需要通过联合堆栈查看
            stat.SF_ARCHIVED: 可存档文件(超级用户可设)
            stat.SF_IMMUTABLE: 文件是只读的(超级用户可设)
            stat.SF_APPEND: 文件只能追加内容(超级用户可设)
            stat.SF_NOUNLINK: 文件不可删除(超级用户可设)
            stat.SF_SNAPSHOT: 快照文件(超级用户可设)
返回值：
    该方法没有返回值。
'''
import os, stat

if __name__ == "__main__":
    path = "/tmp/foo.txt"

    # 为文件设置标记，使得它不能被重命名和删除
    flags = stat.SF_NOUNLINK
    retval = os.chflags(path, flags)
    print("返回值：%s" % retval)
