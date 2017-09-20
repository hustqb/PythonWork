"""
Hello World, but with more meat.
更复杂一点的helloworld
"""

import wx


class HelloFrame(wx.Frame):
	"""
	A Frame that says Hello World
	一个框架，显示hello world，还有其他的一些功能
	"""

	def __init__(self, *args, **kw):
		# 调用父类(wx.Frame)的__init__函数
		super(HelloFrame, self).__init__(*args, **kw)

		# create a panel in the frame
		pnl = wx.Panel(self)

		# and put some text with a larger bold font on it
		st = wx.StaticText(pnl, label="Hello World!", pos=(25, 25))
		font = st.GetFont()
		font.PointSize += 10
		font = font.Bold()
		st.SetFont(font)

		# create a menu bar
		self.make_menu_bar()

		# and a status bar
		self.CreateStatusBar()
		self.SetStatusText("Welcome to wxPython!")

	def make_menu_bar(self):
		"""
		A menu bar is composed of menus, which are composed of menu items.
		This method builds a set of menus and binds handlers to be called
		when the menu item is selected.
		定义菜单栏：菜单名和与之绑定的事件
		"""
		'''File menu包括hello item和exit item'''
		# Make a file menu with Hello and Exit items
		file_menu = wx.Menu()
		# The "\t..." syntax defines an accelerator key that also triggers
		# the same event
		hello_item = file_menu.Append(-1, "&Hello...\tCtrl-H",
		                              "Help string shown in status bar for this menu item")
		file_menu.AppendSeparator()
		# When using a stock ID we don't need to specify the menu item's label
		exit_item = file_menu.Append(wx.ID_EXIT)

		'''help menu包括about item'''
		# Now a help menu for the about item
		help_menu = wx.Menu()
		about_item = help_menu.Append(wx.ID_ABOUT)

		# Make the menu bar and add the two menus to it. The '&' defines
		# that the next letter is the "mnemonic" for the menu item. On the
		# platforms that support it those letters are underlined and can be
		# triggered from the keyboard.
		menu_bar = wx.MenuBar()
		menu_bar.Append(file_menu, "&File")
		menu_bar.Append(help_menu, "&Help")

		# Give the menu bar to the frame
		self.SetMenuBar(menu_bar)

		# Finally, associate a handler function with the EVT_MENU event for
		# each of the menu items. That means that when that menu item is
		# activated then the associated handler function will be called.
		self.Bind(wx.EVT_MENU, self.on_hello, hello_item)  # args：事件类型，事件，绑定对象
		self.Bind(wx.EVT_MENU, self.on_exit, exit_item)
		self.Bind(wx.EVT_MENU, self.on_about, about_item)

	def on_exit(self, event):
		"""Close the frame, terminating the application."""
		self.Close(True)

	def on_hello(self, event):
		"""Say hello to the user."""
		wx.MessageBox("Hello again from wxPython")

	def on_about(self, event):
		"""Display an About Dialog"""
		wx.MessageBox("This is a wxPython Hello World sample",
		              "About Hello World 2",
		              wx.OK | wx.ICON_INFORMATION)


if __name__ == '__main__':
	'''1. 创建一个app对象'''
	app = wx.App()
	'''2. 创建一个frame框架，
	看来重点在这里'''
	frm = HelloFrame(None, title='Hello World 2')
	'''3. 显示frame框架'''
	frm.Show()
	'''4. 启动app对象'''
	app.MainLoop()
