# coding=utf-8
"""
统计天龙八部.txt里的一些文本信息
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像的负号'-'显示为方块的问题


def read_characters(characters_path, txt_format='utf-8'):
	"""
	将角色.txt中的所有人物名字提取出来并保存在一个list中。
	"""
	names = []
	with open(characters_path, 'r', encoding=txt_format) as f:  # 对于Python3最好指定文件的编码方式，否则为系统默认(windows为gbk)
		for line in f:  # line的数据类型为str
			if len(line) == 0:  # 该行为空
				pass
			line = line.strip()
			names += line.split('、')
	return names


def statistics(stt_dir, line):
	for k in stt_dir.keys():
		stt_dir[k] += line.count(k)
	return stt_dir


def plot_bar(outpath, stt_dir, nums=10):
	"""
	Draw a histogram of TianLongBaBu's characters showup times.
	:param outpath:
	:param stt_dir:
	:param nums: The number of characters.
		E.g, if nums=10, there will be 10 bars in the histogram for 10 characters.
	:return:
	"""
	characters_stt = sorted(stt_dir.items(), key=lambda x: x[1], reverse=True)[:nums]
	characters = [x[0] for x in characters_stt]
	stts = [x[1] for x in characters_stt]
	fig = plt.figure()
	plt.bar(range(len(stts)), stts, width=0.5, color='yellow', alpha=0.6)
	plt.xticks(np.arange(len(stts)) + 0.5 / 2, characters)
	plt.title('天龙八部任务名字的出现次数排名')
	fig.savefig(outpath, pad_inches='tight')
	plt.close()


class TextStatistics(object):
	def __init__(self, book_path, book_format):
		self.path = book_path
		self.format = book_format
		pass

	def read_book(self, names):
		stt_dir = dict.fromkeys(names, 0)
		with open(self.path, encoding=self.format) as f:
			count = 0
			for line in f:
				if len(line) == 0:  # 该行为空
					pass
				if self.format == 'utf-8':
					stt_dir = statistics(stt_dir, line)
				else:
					stt_dir = statistics(stt_dir, line)
				if count % 100 == 0:
					print(count)
				count += 1
		return stt_dir


if __name__ == '__main__':
	names_main = read_characters('tlbb_characters.txt')
	ts = TextStatistics('tlbb_utf.txt', 'utf-8')
	# ts = TextStatistics('tlbb_gb2312.txt', 'gbk')  # 另一个例子，编码方式为gb2312(gbk)
	stt_dir_main = ts.read_book(names_main)
	plot_bar('statistics.png', stt_dir_main)
