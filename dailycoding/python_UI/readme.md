# Python图形界面
做Python UI当然可以使用Python标准库中的Tkinter，但是wxPython的功能更多，更好用。
wxPython应该是有强大而稳定的团队在维护，它的网站和官方文档也非常详实。
## wxPython
wxPython是一个关于Python的跨平台GUI工具集。
通过wxPython，开发者可以为它们的Python应用程序创建交互界面，并且几乎不需要做跨平台的改动。
## 代码
### HelloWxPython
先用wxPython官网上的一个简单的例子来展示wxpython设计GUI的格式。
一共四步（这里我们不算import部分）：
	1. 创建一个app对象
	2. 创建一个frame框架
	3. 显示frame框架
	4. 启动app对象
### ComplicatedHello
更复杂一点的wxPython例子，添加了一些菜单和按钮。
### show_dic_picture
这个Python GUI有两个功能：
1. 浏览文件夹内的图片，并可以实现文件夹的上下级跳转
2. 在浏览图片的同时，可以为图片做标记，标记数据存储在**statistics.csv**文件内
这个脚本的意义？
&emsp;&emsp;在计算机视觉领域，使用神经网络前总是需要一些标定好的图片，这个脚本可以简化我们浏览和标定图片的工作。
### 效果展示
<img src='demo.png'>

[统计信息](https://github.com/hustqb/PythonWork/blob/master/dailycoding/python_UI/statistics.csv)

## 参考
wxPython小程序来自于[wxPython官方文档](https://www.wxpython.org/pages/overview/)

图片浏览器主要参考自——[使用wxpython实现的一个简单图片浏览器实例](http://www.jb51.net/article/52060.htm)