# coding=utf-8
"""
-v及其全程--verbosity都是可选择参数，
如果命令行后加上了-v或--verbosity，
	输出：verbosity turned on
"""
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-v',
                    '--verbosity',
                    help='increase output verbosity',
                    action='store_true')
args = parser.parse_args()
if args.verbosity:
	print('verbosity turned on')
