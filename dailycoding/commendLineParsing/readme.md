# argparse--Parser for commend-line options, arguments and sub-commands
## 简介
argparse模块是Python中一个有关命令行交互的接口。通过这个模块，我们可以定义程序需要的命令行参数及这些参数的解析方法。
同时，argparse模块可以自动创建help信息，并且在用户的命令有误时，可以友好地将其指出来。
## 代码
### simpleExample
1. 命令行输入`python simpleExample.py -h`，输出：<font color=grean>帮助信息</font>
2. 命令行输入`python simpleExample.py 4`，输出：<font color=grean>16</font>
### optionalArguments
`-v`及其全称`--verbosity`都是可选择参数，如果命令行后加上了`-v`或`--verbosity`，输出：<font color=grean>verbosity turned on</font>
### moreComplex
固定参数和可选参数混合使用:
1. `python moreComplex.py 4 -v`，输出：the square of 4 equals 16
2. `python moreComplex.py 4`，输出：4
## 参考
### 入门argparse简介
[argparser模块学习](http://www.jianshu.com/p/a50aead61319)
### 官方指南
官方指南通过许多例子由浅入深介绍argparse模块的功能，这里的脚本就是出自官方指南的前3个例子。
[argparse tutorial](https://docs.python.org/3/library/argparse.html)