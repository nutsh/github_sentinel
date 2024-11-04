class Notifier:
    def __init__(self, config):
        self.config = config

    def send_notification(self, report):
        if self.config.notification_channel == "email":
            self.send_email(report)
        elif self.config.notification_channel == "slack":
            self.send_slack(report)

    def send_email(self, report):
        # 使用 SMTP 发送邮件
        print("Sending email notification...")

    def send_slack(self, report):
        # 使用 Slack API 发送消息
        print("Sending Slack notification...")
