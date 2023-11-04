# excel_reader.py

import pandas as pd

class ExcelReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        return pd.read_excel(self.file_path)
    # report_generator.py

class ReportGenerator:
    def generate(self, data):
        reports = []

        for index, row in data.iterrows():
            report = dict(row)
            reports.append(report)

        return reports
# email_sender.py

import smtplib
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self, server, port, user, password):
        self.server_info = (server, port, user, password)

    def send(self, email, subject, content):
        server = smtplib.SMTP(*self.server_info[:2])
        server.starttls()
        server.login(*self.server_info[2:])

        message = MIMEText(content)
        message['Subject'] = subject
        message['From'] = self.server_info[2]
        message['To'] = email

        server.send_message(message)
        server.quit()
# main.py

from excel_reader import ExcelReader
from report_generator import ReportGenerator
from email_sender import EmailSender

def main():
    reader = ExcelReader('成绩表.xlsx')
    generator = ReportGenerator()
    email_sender = EmailSender('smtp.example.com', 587, 'user@example.com', 'password')

    # 读取Excel文件
    data = reader.read()

    # 生成成绩单
    reports = generator.generate(data)

    # 发送成绩单
    for report in reports:
        subject = f"{report['姓名']}的成绩单"
        content = f"学号: {report['学号']}\n成绩: {report['成绩']}"
        email_sender.send(report['电子邮件'], subject, content)
        print(f"对 {report['姓名']} 成功发送了一封成绩通知邮件。")

if __name__ == '__main__':
    main()