from config import Config
from subscription_manager import SubscriptionManager
from update_fetcher import UpdateFetcher
from notifier import Notifier
from report_generator import ReportGenerator

def main():
    # 加载配置
    config = Config()

    # 初始化各模块
    subscription_manager = SubscriptionManager(config)
    update_fetcher = UpdateFetcher(config)
    notifier = Notifier(config)
    report_generator = ReportGenerator(config)

    # 获取订阅仓库列表
    subscriptions = subscription_manager.get_subscriptions()

    # 获取更新
    updates = update_fetcher.fetch_updates(subscriptions)

    # 生成报告
    report = report_generator.generate_report(updates)

    # 发送通知
    notifier.send_notification(report)

if __name__ == "__main__":
    main()
