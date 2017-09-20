# coding=utf-8
"""
初始化一个app。
用一个frame实现目录的功能，其上只有一个listbox；
用另一个frame实现图片展示的功能，
两个frame通过app进行信息的传递。
"""
try:
	import wx
except ImportError:
	import wx
	print('安装地址:', 'https://www.wxpython.org/download.php')
	print('或使用pip的方式安装：', 'pip install -U wxPython')
import os
start_path = os.getcwd()  # 程序运行的路径，决定了保存结果文件的路径


class PBDirFrame(wx.Frame):
	def __init__(self, app, cur_dir):
		"""
		显示图片列表的frame
		:param app: 应用
		:param cur_dir: 根目录
		"""
		super(PBDirFrame, self).__init__(None, -1, title='选择', size=(250, 500))
		self.app = app

		'''设置字体'''
		font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
		               wx.FONTWEIGHT_NORMAL, faceName='Courier New')
		self.SetFont(font)

		'''listbox'''
		self.list = wx.ListBox(self, id=-1, pos=(0, 0), size=(200, 600))
		os.chdir(cur_dir)
		self.load_dir(os.getcwd())

		'''事件绑定'''
		self.Bind(wx.EVT_CLOSE, self.on_close)  # 关闭frame窗口事件
		self.list.Bind(wx.EVT_LISTBOX_DCLICK, self.on_dclick)  # 双击事件

		self.Show()
	
	def on_close(self, event):
		"""关闭窗口，关闭app"""
		self.Destroy()
		self.app.close()
	
	def on_dclick(self, event):
		"""listbox双击事件"""
		'''判断是否返回上级文件夹'''
		if self.list.GetSelection() == 0:
			path = os.getcwd()
			pathinfo = os.path.split(path)
			cur_dir = pathinfo[0]  # 上级文件夹路径
		else:
			cur_dir = self.list.GetStringSelection()  # 选中文件夹路径

		'''判断是否是图片'''
		if os.path.isdir(cur_dir):
			self.load_dir(cur_dir)
			os.chdir(cur_dir)
		elif os.path.splitext(cur_dir)[-1] == '.png':  # 显示图片
			self.app.show_zcbh_message(cur_dir)
		else:
			print('It\'s not directionary or pictures followed by \'.png\'')
	
	def load_dir(self, prior_dir):
		"""加载文件夹中的内容到ListBox"""
		if not os.path.isdir(prior_dir):  # 不是目录则不进行操作
			return
		self.list.Clear()  # 清空
		self.list.Append('...')  # 添加返回上一层文件夹标志
		for element in os.listdir(prior_dir):
			self.list.Append(element)

	def get_next_zcbh(self):
		"""获得下一张要显示的图片"""
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
		"""获得上一张图片"""
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
	
	def __init__(self, app, result_path):
		super(PBPicFrame, self).__init__(None, -1, "展示", size=(800, 600))
		self.app = app
		self.result_path = result_path
		
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

		'''事件绑定'''
		self.Bind(wx.EVT_MOUSEWHEEL, self.on_change_message)  # 鼠标滚动事件
		self.Bind(wx.EVT_TEXT_ENTER, self.save, self.input_text)  # 文本输入事件
		self.Bind(wx.EVT_BUTTON, self.bsave, self.button_ok)  # 按键
		self.Bind(wx.EVT_BUTTON, self.rewrite, self.button_rewrite)  # 按键
		self.Bind(wx.EVT_CLOSE, self.on_close)  # 关闭frame窗口事件
		self.name = None
		self.bmppath = None
		self.pos = None
		self.Hide()
	
	def show_zcbh_message(self, path):
		if os.path.splitext(path)[-1] != '.png':
			return
		self.show_image(path)
		self.show_name(path)
	
	def show_name(self, path):
		"""显示图片名称"""
		self.name = os.path.splitext(path)[0]
		self.display_text.SetValue(self.name)
	
	def show_image(self, path):
		"""显示图片"""
		self.bmppath = path
		image = wx.Image(path, wx.BITMAP_TYPE_PNG)  # 如果图片类型是png
		bmp = image.ConvertToBitmap()
		size = self.scale_size(bmp)
		bmp = image.Scale(size[0], size[1]).ConvertToBitmap()
		self.bmp.SetSize(size)
		self.bmp.SetBitmap(bmp)
		self.Show()
	
	def scale_size(self, bmp):
		"""调整图片尺寸"""
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
		"""鼠标滚轮浏览用户"""
		rotation = event.GetWheelRotation()
		if rotation < 0:
			self.app.show_next_zcbh()
		else:
			self.app.show_pre_zcbh()
	
	def save(self, event):
		"""获取样本类型，并保存"""
		data_type = self.input_text.GetValue()
		sample = self.name + ',' + data_type
		print(type(self.name))
		print(type(','))
		print(type(data_type))
		print(sample)
		with open(self.result_path, 'a') as f:
			f.write(sample + '\n')
		self.app.show_next_zcbh()
		self.input_text.Clear()
		self.input_text.SetFocus()
	
	def bsave(self, event):
		self.save(event)
	
	def rewrite(self, event):
		self.app.show_pre_zcbh()

	def on_close(self, event):
		"""关闭窗口"""
		self.Destroy()


class PBApp(wx.App):
	def __init__(self, curdir_path, result_path, redirect=False):
		wx.App.__init__(self, redirect)  # redirect=False将信息输出到dos界面
		self.dirframe = PBDirFrame(self, curdir_path)
		self.picframe = PBPicFrame(self, os.path.join(start_path, result_path))
	
	def show_zcbh_message(self, path):
		"""
		显示图片及其信息的触发条件：
			1. 双击文件列表中的图片名
			2. 鼠标滑动
		"""
		self.picframe.show_zcbh_message(path)
		# self.picframe.SetFocus()
	
	def show_next_zcbh(self):
		path = self.dirframe.get_next_zcbh()
		self.show_zcbh_message(path)
	
	def show_pre_zcbh(self):
		path = self.dirframe.get_pre_zcbh()
		self.show_zcbh_message(path)
	
	def close(self):
		try:
			self.picframe.Close()
		except RuntimeError:
			pass


def main(curdir_path, sample_path):
	app = PBApp(curdir_path, sample_path)
	app.MainLoop()


if __name__ == '__main__':
	inpath_curdir = r'pictures'  # 当前要打开的图片文件夹
	outpath_sample = r'statistics.csv'  # 样本信息的保存地址
	main(inpath_curdir, outpath_sample)
