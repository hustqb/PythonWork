#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "zhang_qinbin@163.com"  # 用户名
mail_pass = "01267101zhang"  # 口令

sender = 'zhang_qinbin@163.com'
receivers = ['pcwang1993@163.com', 'wuhengsky@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('电话号码是：15629050867', 'plain', 'utf-8')
message['From'] = Header("zhang_qinbin@163.com")
message['To'] = Header('pcwang1993@163.com;wuhengsky@163.com;983910368@qq.com')

subject = '电话'
message['Subject'] = Header(subject, 'utf-8')

try:
	smtpObj = smtplib.SMTP()
	smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
	smtpObj.login(mail_user, mail_pass)
	smtpObj.sendmail(sender, receivers, message.as_string())
	print "邮件发送成功"
except smtplib.SMTPException:
	print "Error: 无法发送邮件"