"""
先用wxPython官网上的一个简单的例子来展示wxpython设计GUI的格式。
一共四步（这里我们不算import部分）：
	1. 创建一个app对象
	2. 创建一个frame框架
	3. 显示frame框架
	4. 启动app对象
那么下面我们来介绍一个复杂一点的GUI代码——show_dic_picture.py
"""
# First things, first. Import the wxPython package.
import wx

# Next, create an application object.
app = wx.App()

# Then a frame.
frm = wx.Frame(None, title="Hello WxPython")

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()
