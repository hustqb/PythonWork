# coding=utf-8
"""
1. 命令行输入python simpleExample.py -h
	输出：帮助信息
2. 命令行输入python simpleExample.py 4
	输出：16
"""
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",
                    type=int)
args = parser.parse_args()
print(args.square**2)
