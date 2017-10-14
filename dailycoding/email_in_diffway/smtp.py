#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
发送邮件
最麻烦的其实是为邮箱开通第三方登录权限
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "zh***bin@163.com"  # 用户名
mail_pass = "012***hang"  # 口令

sender = 'zhang***@163.com'
receivers = ['pc***93@163.com', 'wu***gsky@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('电话号码是：15***0867', 'plain', 'utf-8')
message['From'] = Header("zh***n@163.com")
message['To'] = Header('pc***93@163.com;wu***ky@163.com;98***68@qq.com')

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