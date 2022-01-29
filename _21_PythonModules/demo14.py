# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 模块
从一个包中导入*
    设想一下，如果我们使用from sound.effects import *会发生什么？
    Python会进入文件系统，找到这个包里面所有的子模块，一个一个的把它们都导入进来。
    但是很不幸，这个方法在Windows平台上工作的就不是非常好，因为Windows是一个大小写不区分的系统。
    在这类平台上，没有人敢担保一个叫做ECHO.py 的文件导入为模块echo还是Echo甚至ECHO。
    （例如，Windows 95就很讨厌的把每一个文件的首字母大写显示）而且DOS的8+3命名规则对长模块名称的处理会把问题搞得更纠结。
    为了解决这个问题，只能烦劳包作者提供一个精确的包的索引了。

    导入语句遵循如下规则：如果包定义文件__init__.py存在一个叫做__all__的列表变量，
    那么在使用from package import *的时候就把这个列表中的所有名字作为包内容导入。

    作为包的作者，可别忘了在更新包之后保证__all__也更新了啊。你说我就不这么做，我就不使用导入*这种用法，
    好吧，没问题，谁让你是老板呢。这里有一个例子，在:file:sounds/effects/__init__.py中包含如下代码:
        __all__ = ["echo", "surround", "reverse"]
    这表示当你使用from sound.effects import *这种用法时，你只会导入包里面这三个子模块。

    如果__all__真的没有定义，那么使用from sound.effects import *这种语法的时候，
    就不会导入包sound.effects里的任何子模块。他只是把包sound.effects和它里面定义的所有内容导入进来
    （可能运行__init__.py里定义的初始化代码）。

    这会把__init__.py里面定义的所有名字导入进来。并且他不会破坏掉我们在这句话之前导入的所有明确指定的模块。看下这部分代码:
        import sound.effects.echo
        import sound.effects.surround
        from sound.effects import *
    这个例子中，在执行from...import前，包sound.effects中的echo和surround模块都被导入到当前的命名空间中了。
    （当然如果定义了__all__就更没问题了）

    通常我们并不主张使用*这种方法来导入模块，因为这种方法经常会导致代码的可读性降低。
    不过这样倒的确是可以省去不少敲键的功夫，而且一些模块都设计成了只能通过特定的方法导入。

    记住，使用from Package import specific_submodule这种方法永远不会有错。
    事实上，这也是推荐的方法。除非是你要导入的子模块有可能和其他包的子模块重名。

    如果在结构中包是一个子包（比如这个例子中对于包sound来说），而你又想导入兄弟包（同级别的包）你就得使用导入绝对的路径来导入。
    比如，如果模块sound.filters.vocoder要使用包sound.effects中的模块echo，你就要写成from sound.effects import echo。
        from . import echo
        from .. import formats
        from ..filters import equalizer

    无论是隐式的还是显式的相对导入都是从当前模块开始的。主模块的名字永远是"__main__"，
    一个Python应用程序的主模块，应当总是使用绝对路径引用。

    包还提供一个额外的属性__path__。这是一个目录列表，里面每一个包含的目录都有为这个包服务的__init__.py，
    你得在其他__init__.py被执行前定义哦。可以修改这个变量，用来影响包含在包里面的模块和子包。

    这个功能并不常用，一般用来扩展包里面的模块。
'''
from _18_PythonModules.tool.fibonacci import fib, fib2

if __name__ == "__main__":
    fib(1000)
    print(fib2(100))
