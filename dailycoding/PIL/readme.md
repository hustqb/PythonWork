# 生成图片验证码
## PIL
Python Imaging Library(PIL)为Python提供了处理图片的接口，包括文件格式化、图片处理、图表处理等。
不过PIl从2009年开始就不更新了，不支持Python3，但是，Pillow完成了PIL未完成的工作。
## 代码
生成图片验证码三部曲：
1. 生成随机数字
2. 为随机数生成随机颜色
3. 为底图噪声生成随机颜色
### 效果图

<img src=https://raw.githubusercontent.com/hustqb/PythonWork/tree/master/dailycoding/PIL/code.jpg>

## 参考

[廖雪峰的官方网站——PIL](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320027235877860c87af5544f25a8deeb55141d60c5000) 

[Pillow](https://pillow.readthedocs.io/en/4.3.x/)