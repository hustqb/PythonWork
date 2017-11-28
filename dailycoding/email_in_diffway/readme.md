# smtp
## 代码
发送邮件，这个其实很简单，麻烦的是前面为邮箱设置第三方登录的权限。

要编写程序来发送和接受邮件，本质上就是：

	* 编写MUA(mail user agent)把邮件发送到MTA(mail transger agent)
	* 编写MUA(mail user agent)从MDA上收邮件(mail delivery agent)

	
	1. 发邮件时，MUA和MTA使用的协议就是SMTP：Simple Mail Transfer Protocol，后面MTA到另一个MTA也是用的SMTP协议
	2. 收邮件时，MUA和MDA使用的协议有两种：POP：Post Office Protocal，目前版本是3，俗称POP3;IMAP：Internet Message Access Protocal，目前版本是4，优点是不但能去邮件，还可以直接操作MDA上存储的邮件，比如从收件箱移到垃圾箱等等。

## 参考
[廖雪峰的官方网站——SMTP发送邮件](https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832745198026a685614e7462fb57dbf733cc9f3ad000)