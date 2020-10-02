# -*- coding: UTF-8 -*-
# author: chenyongjun
import shutil

# 针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口
shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')
