# GitHub Sentinel

GitHub Sentinel 是一款开源的自动化工具，专为开发者和项目管理人员设计，用于定期监控和汇总订阅的 GitHub 仓库动态。通过该工具，用户可以方便地管理订阅仓库，自动获取最新更新，并通过电子邮件或 Slack 通知进行推送，还可以生成详细的更新报告，以便团队更高效地跟踪项目进展。

## 项目功能

- **订阅管理**: 管理 GitHub 仓库的订阅，包括添加、删除和查看订阅的仓库。
- **更新获取**: 定期从 GitHub 获取订阅仓库的最新动态。
- **通知系统**: 通过电子邮件或 Slack 向用户推送最新的仓库更新。
- **报告生成**: 生成详细的更新报告，便于用户查看项目的变更情况。

## 安装与使用

### 克隆项目

```bash
git clone https://github.com/nutsh/github_sentinel.git
cd github_sentinel
```

### 配置

在 `config.py` 文件中，设置您的 GitHub API Token 和通知方式：

```python
class Config:
    def __init__(self):
        # 读取配置，例如 GitHub API token 和更新周期
        self.github_token = "your_github_token_here"
        self.update_frequency = "daily"
        self.notification_channel = "email"  # 可选：'email' 或 'slack'
```

### 运行项目

在项目目录下运行以下命令来启动 GitHub Sentinel：

```bash
python main.py
```

## 项目结构

```
github_sentinel/
├── __init__.py
├── main.py                 # 主入口文件
├── config.py               # 配置模块
├── subscription_manager.py # 订阅管理模块
├── update_fetcher.py       # 更新获取模块
├── notifier.py             # 通知系统模块
├── report_generator.py     # 报告生成模块
├── utils.py                # 实用工具模块
└── data/                   # 数据存储目录
```

## 贡献

欢迎各位开发者贡献代码！您可以通过创建 issue 或提交 pull request 的方式来参与项目的开发和改进。

## 许可证

此项目基于 MIT 许可证进行发布。