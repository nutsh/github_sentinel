class SubscriptionManager:
    def __init__(self, config):
        self.config = config
        # 初始化订阅列表（可以从文件或数据库中加载）
        self.subscriptions = ["owner/repo1", "owner/repo2"]

    def add_subscription(self, repo):
        self.subscriptions.append(repo)
        # 保存订阅信息到文件或数据库

    def remove_subscription(self, repo):
        self.subscriptions.remove(repo)
        # 更新订阅信息到文件或数据库

    def get_subscriptions(self):
        return self.subscriptions
