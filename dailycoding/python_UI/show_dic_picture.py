# coding=utf-8
from __future__ import print_function

try:
	import wx
except ImportError as e:
	print(e)
	print('安装地址:', 'https://www.wxpython.org/download.php')
import os


class PBDirFrame(wx.Frame):
	def __init__(self, app, curdir):
		"""
		
		:param app: 应用
		:param curdir: 根目录
		"""
		wx.Frame.__init__(self, None, -1, u"选择文件夹", size=(250, 500))
		self.app = app
		# 设置字体
		font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, 'Courier New')
		self.SetFont(font)
		# 文件夹listbox
		self.list = wx.ListBox(self, -1, (0, 0), (200, 600), '', wx.LB_SINGLE)
		self.list.Bind(wx.EVT_LISTBOX_DCLICK, self.on_dclick)
		# 加载当前文件夹
		os.chdir(curdir)
		self.load_dir(curdir)
		# 绑定事件
		self.Bind(wx.EVT_CLOSE, self.on_close)
		# 显示窗口
		self.Show()
	
	def on_close(self, event):
		self.Destroy()
		self.app.close()
	
	def on_dclick(self, event):
		"""
		listbox双击事件
		:param event:
		:return:
		"""
		if self.list.GetSelection() == 0:  # 判断是否选择了返回上一层文件夹
			path = os.getcwd()
			print(path)
			pathinfo = os.path.split(path)
			dir_ = pathinfo[0]
		else:  # 获得需要进入的下一层文件夹
			dir_ = self.list.GetStringSelection()
		
		if os.path.isdir(dir_):  # 进入文件夹
			self.load_dir(dir_)
		elif os.path.splitext(dir_)[-1] == '.png':  # 显示图片
			# elif os.path.splitext(dir_)[-1] == '.jpg':  # 显示图片
			self.app.show_zcbh_message(dir_)
	
	def load_dir(self, prior_dir):
		# 不是目录则不进行操作
		if not os.path.isdir(prior_dir):
			return
		self.list.Clear()  # 清空
		self.list.Append('...')  # 添加返回上一层文件夹标志
		for element in os.listdir(prior_dir):
			self.list.Append(element)
		os.chdir(prior_dir)  # 设置工作路径
	
	def get_next_zcbh(self):
		"""
		获得下一张要显示的图片
		:return:
		"""
		index = self.list.GetSelection()
		i = index
		while i + 1 < self.list.GetCount():
			i += 1
			if os.path.splitext(self.list.GetString(i))[-1] == '.png':
				break
		if i < self.list.GetCount():
			index = i
		self.list.SetSelection(index)
		return self.list.GetStringSelection()
	
	def get_pre_zcbh(self):
		"""
		获得上一张图片
		:return:
		"""
		index = self.list.GetSelection()
		i = index
		while i - 1 > 0:
			i -= 1
			if os.path.splitext(self.list.GetString(i))[-1] == '.png':
				break
		if i > 0:
			index = i
		
		self.list.SetSelection(index)
		return self.list.GetStringSelection()


class PBPicFrame(wx.Frame):
	max_width = 800
	max_height = 400
	
	def __init__(self, app, sample_path):
		wx.Frame.__init__(self, None, -1, u"筛选样本", size=(800, 600))
		self.app = app
		self.path = sample_path
		
		self.SetSizeHints(-1, -1)
		bs1 = wx.BoxSizer(wx.VERTICAL)
		'''图片展示区间'''
		bs11 = wx.BoxSizer(wx.VERTICAL)
		bs11.SetMinSize(wx.Size(-1, 400))
		self.bmp = wx.StaticBitmap(self, 0, wx.NullBitmap, (0, 0), (800, 400))  # 相框
		bs11.Add(self.bmp, 0, wx.ALL, 5)
		bs1.Add(bs11, 1, wx.EXPAND, 5)
		'''用户名展示区间'''
		bs12 = wx.BoxSizer(wx.HORIZONTAL)
		self.m_staticText5 = wx.StaticText(self, -1, u"用户")
		self.m_staticText5.Wrap(-1)
		bs12.Add(self.m_staticText5, 0, wx.ALL, 5)
		self.display_text = wx.TextCtrl(self, style=wx.TE_READONLY | wx.TE_CENTER)
		bs12.Add(self.display_text, 0, wx.ALL, 5)
		bs1.Add(bs12, 1, wx.EXPAND, 5)
		'''交互区间'''
		bs13 = wx.BoxSizer(wx.HORIZONTAL)
		self.m_staticText6 = wx.StaticText(self, -1, u"故障类型")
		self.m_staticText6.Wrap(-1)
		bs13.Add(self.m_staticText6, 0, wx.ALL, 5)
		self.input_text = wx.TextCtrl(self, -1, wx.EmptyString)
		bs13.Add(self.input_text, 0, wx.ALL, 5)
		self.button_rewrite = wx.Button(self, -1, u"back")
		bs13.Add(self.button_rewrite, 0, wx.ALL, 5)
		self.button_ok = wx.Button(self, -1, u"OK")
		bs13.Add(self.button_ok, 0, wx.ALL, 5)
		bs1.Add(bs13, 1, wx.EXPAND, 5)
		
		self.SetSizer(bs1)
		self.Layout()
		self.Centre(wx.BOTH)
		
		self.Bind(wx.EVT_MOUSEWHEEL, self.on_change_message)
		self.Bind(wx.EVT_KEY_DOWN, self.on_key_down)
		self.Bind(wx.EVT_TEXT_ENTER, self.save, self.input_text)
		self.Bind(wx.EVT_BUTTON, self.bsave, self.button_ok)
		self.Bind(wx.EVT_BUTTON, self.rewrite, self.button_rewrite)
		self.name = None
		self.bmppath = None
		self.pos = None
		self.Hide()
	
	def show_zcbh_message(self, path):
		"""
		显示用户的数据图片和用户名
		:param path:
		:return:
		"""
		self.show_image(path)
		self.show_name(path)
	
	def show_name(self, path):
		"""
		显示用户名
		:param path:
		:return:
		"""
		if os.path.splitext(path)[-1] != '.png':
			return
		self.name = path[4:-4]
		self.display_text.SetValue(self.name)
	
	def show_image(self, path):
		if os.path.splitext(path)[-1] != '.png':
			return
		self.bmppath = path
		# print(path)
		# print(os.getcwd())
		image = wx.Image(path, wx.BITMAP_TYPE_PNG)  # 如果图片类型是png
		# image = wx.Image(path, wx.BITMAP_TYPE_JPEG)  # 如果图片类型是jpeg
		bmp = image.ConvertToBitmap()
		size = self.get_size(bmp)
		bmp = image.Scale(size[0], size[1]).ConvertToBitmap()
		self.bmp.SetSize(size)
		self.bmp.SetBitmap(bmp)
		self.Show()
	
	def get_size(self, bmp):
		"""
		调整图片尺寸
		:param bmp:
		:return:
		"""
		width = bmp.GetWidth()
		height = bmp.GetHeight()
		if width > self.max_width:
			height = height * self.max_width / width
			width = self.max_width
		if height > self.max_height:
			width = width * self.max_height / height
			height = self.max_height
		size = width, height
		return size
	
	def on_change_message(self, event):
		"""
		鼠标滚轮浏览用户
		:param event:
		:return:
		"""
		rotation = event.GetWheelRotation()
		if rotation < 0:
			self.app.show_next_zcbh()
		else:
			self.app.show_pre_zcbh()
	
	def on_key_down(self, event):
		"""
		键盘控制图片放大缩小
			数字1放大
			数字2缩小
		:param event:
		:return:
		"""
		keycode = event.GetKeyCode()
		if keycode == 49:
			self.size_up()
		elif keycode == 50:
			self.size_down()
		event.Skip()  # 这个貌似很重要，要同时触发app上的快捷键
	
	def size_up(self):
		self.max_width += 50
		self.max_height += 75
		self.show_zcbh_message(self.bmppath)
	
	def size_down(self):
		self.max_width -= 50
		self.max_height -= 75
		self.show_zcbh_message(self.bmppath)
	
	def save(self, event):
		"""
		获取样本类型，并保存
		:param event:
		:return:
		"""
		# print(self.input_text.GetValue())
		data_type = self.input_text.GetValue()
		sample = self.name + ',' + data_type
		print(sample)
		filename = self.path
		with open(filename, 'a') as f:
			f.write(sample + '\n')
		self.app.show_next_zcbh()
		self.input_text.Clear()
		self.input_text.SetFocus()
	
	def bsave(self, event):
		# data_type = self.input_text.GetValue()
		self.save(event)
	
	def rewrite(self, event):
		self.app.show_pre_zcbh()


class PBApp(wx.App):
	def __init__(self, curdir_path, sample_path, redirect=False):
		wx.App.__init__(self, redirect)  # redirect=False将信息输出到dos界面
		# 显示文件夹列表界面
		self.dirframe = PBDirFrame(self, curdir_path)
		# 显示图片界面
		self.picframe = PBPicFrame(self, sample_path)
	
	# 绑定事件
	# self.Bind(wx.EVT_KEY_DOWN, self.on_key_down)
	
	def show_zcbh_message(self, path):
		self.picframe.show_zcbh_message(path)
		self.picframe.SetFocus()
	
	def show_next_zcbh(self):
		path = self.dirframe.get_next_zcbh()
		self.show_zcbh_message(path)
	
	def show_pre_zcbh(self):
		path = self.dirframe.get_pre_zcbh()
		self.show_zcbh_message(path)
	
	def on_key_down(self, event):
		keycode = event.GetKeyCode()
		if keycode == 27:  # ESC键
			# 切换图片窗体的显示和隐藏
			if self.picframe.IsShown():
				self.picframe.Hide()
			else:
				self.picframe.Show()
	
	def close(self):
		try:
			self.picframe.Close()
		except wx.PyDeadObjectError:
			pass


def main(curdir_path, sample_path):
	app = PBApp(curdir_path, sample_path)
	app.MainLoop()


if __name__ == '__main__':
	inpath_curdir = r'E:\keras\figure\vcfp'  # 当前要打开的文件夹
	# inpath_curdir = r'C:\Users\hustqb\Pictures\501'
	outpath_sample = r'E:\keras\sample\DataFrame\vol\vol_break_type.csv'  # 样本信息的保存地址
	# outpath_sample = r'C:\Users\hustqb\Pictures\501.csv'
	main(inpath_curdir, outpath_sample)
