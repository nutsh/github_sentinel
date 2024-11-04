class Config:
    def __init__(self):
        # 读取配置，例如 GitHub API token 和更新周期
        self.github_token = "your_github_token_here"
        self.update_frequency = "daily"
        self.notification_channel = "email"
