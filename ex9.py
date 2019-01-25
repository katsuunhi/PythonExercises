# 九、邮件轰炸机

# 你的一个朋友生日快到了，你决定搞个恶作剧——用邮件塞满他的邮箱。

# 功能描述：首先去注册十个邮箱，然后用这是个邮箱轮流发送随机生成的邮件内容给你的朋友。调整发送的频率，以免被服务器拒绝。

import re
import time
import json
import imaplib
import smtplib
from email.mime.text import MIMEText
from email.header import Header
# 目标邮箱账号
the_pattern = "2460670348@qq.com"


class GetMail(object):
    @classmethod
    def mail_login(self, mail_type, mail_ssl, mail_username, mail_password):
        """邮箱登录,并检索目标人未读邮件"""
        get_server = imaplib.IMAP4_SSL(mail_type, mail_ssl)
        get_server.login(mail_username, mail_password)
        get_server.select("INBOX")  # 默认收件夹是INBOX
        typ, data = get_server.search(None, 'UNSEEN')  # SEEN--已读邮件,UNSEEN--未读邮件,ALL--全部邮件
        if data[0]:
            number_list = data[0].split()  # 邮件编号list,编号越大邮件时间越近
            for the_mail_number in number_list:
                # 将邮件标记为已读
                get_server.store(the_mail_number, '+FLAGS', '\\SEEN')
                # 邮件内容详情
                mail_data = str(get_server.fetch(the_mail_number, '(RFC822)')[1])
                # 正则匹配查找目标邮箱账号
                if re.search(the_pattern, mail_data):
                    self.send_mail(mail_username, mail_password)
                    get_server.logout()
                    return 'END'
                else:
                    print("未匹配到目标邮箱,继续执行")
                    return 'CONTINUE'
        else:
            print("未检索到未读邮件")

    @classmethod
    def send_mail(self, mail_type, mail_username, mail_password):
        """发送邮件"""
        # 邮件内容
        msg = self.the_task()       # 获取文件数据内容
        message = MIMEText("'%s'" % msg, 'plain', 'utf-8')
        # 发件人
        message['From'] = Header(mail_username, 'utf-8')
        # 收件人
        message['To'] = Header(the_pattern, 'utf-8')
        # 邮件主题
        message['Subject'] = Header('邮件主题:测试', 'utf-8')
        # 发件服务器
        send_mail_type = 'smtp.exmail.qq.com'
        try:
            # 发短信采用默认端口25,不然会报错
            send_server = smtplib.SMTP(send_mail_type, 25)
            send_server.login(mail_username, mail_password)
            send_server.sendmail(mail_username, the_pattern, message.as_string())
            print("邮件发送成功!!!")
            send_server.quit()
        except smtplib.SMTPException:
            print("邮件发送失败")

    @classmethod
    def the_task(self):
        """
        获取邮件内容,并返回数据,类型为json
        """
        # 做了假数据,具体获取活动数据的方法就不写了
        data_dict = {'task_1': 100, 'task_2': 101, 'task_3': 102}
        json_data = json.dumps(data_dict)
        return json_data


def process_start():
    while True:
        ret = GetMail.mail_login(mail_type='imap.exmail.qq.com', mail_ssl=993, mail_username='1598902968@***.cn', mail_password='katsuunhi6')
        if ret == 'END':
            print("邮件已发送,休眠一分钟继续执行")
            # 休眠一分钟继续执行
            time.sleep(60)
        else:
            print("休眠一分钟继续执行")
            time.sleep(60)
            continue


if __name__ == "__main__":
    # 执行程序
    process_start()