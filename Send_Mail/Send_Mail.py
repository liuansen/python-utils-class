# -*- coding:utf-8 -*-
# author：Anson
from __future__ import unicode_literals

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import formataddr

from settings import MAIL_SMTP, MAIL_HOST, MAIL_USER, MAIL_PWD


class SendEmail(object):

    def __init__(self, subject, body, to_user):
        self.mail_smtp = MAIL_SMTP
        self.mail_host = MAIL_HOST
        self.mail_user = MAIL_USER
        self.mail_pwd = MAIL_PWD

        self.subject = subject
        self.body = body
        self.to_user = to_user

    def handle(self, file_path):
        ret = True
        try:
            msg = MIMEMultipart()
            msg.attach(MIMEText(self.body, 'plain', 'utf-8'))
            msg['From'] = formataddr(["FromRunoob", self.mail_user])
            msg['To'] = formataddr(["FK", self.to_user])
            msg['Subject'] = self.subject

            if len(file_path) != 0:
                att1 = MIMEApplication(open(file_path, 'rb').read())
                att1["Content-Type"] = 'application/octet-stream'
                att1["Content-Disposition"] = 'attachment; filename="123.zip"'
                msg.attach(att1)

            server = smtplib.SMTP_SSL(self.mail_smtp, self.mail_host)  
            server.login(self.mail_user, self.mail_pwd)
            server.sendmail(self.mail_user, [self.to_user, ], msg.as_string())
            server.quit()
        except Exception:
            ret = False

        return ret


if __name__ == '__main__':
    s = SendEmail('', '', '')
    ret = s.handle('')
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
