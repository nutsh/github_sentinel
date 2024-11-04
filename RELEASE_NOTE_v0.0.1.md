# GitHub Sentinel v0.0.1

## 发布日期

2024-11-04

## 主要功能

GitHub Sentinel 是一款专为开发者和项目管理人员设计的自动化工具，能够定期监控和汇总订阅的 GitHub 仓库动态。以下是 v0.0.1 版本的主要功能：

### 功能特性

1. **订阅管理模块**
   - 添加、删除和查看订阅仓库。
2. **更新获取模块**
   - 通过 GitHub API 获取订阅仓库的最新更新。
3. **通知模块**
   - 通过电子邮件或 Slack 通知用户最新的更新。
4. **报告生成模块**
   - 生成包含仓库动态的详细报告，便于项目管理。
5. **配置模块**
   - 支持 GitHub API token 和通知方式的配置。

### 文件结构


下面是将当前代码版本设置为 v0.0.1 的 Git 操作步骤，以及生成对应的 Release Note：

1. 确认所有更改已提交
首先，确保所有代码变更已经提交到 Git 仓库中：

bash
复制代码
git add .
git commit -m "Initial version of GitHub Sentinel"
2. 打标签设置版本号
使用 Git 打标签，将当前提交设置为 v0.0.1：

bash
复制代码
git tag -a v0.0.1 -m "Release version v0.0.1: Initial version with core functionality"
3. 推送标签到远程仓库
将标签推送到远程仓库，以便其他开发者能够看到这个版本：

bash
复制代码
git push origin v0.0.1
4. 生成 Release Note
创建一个 Release Note 文件，描述此版本的主要功能和亮点。可以将其命名为 RELEASE_NOTE_v0.0.1.md。

Release Note 内容如下：

markdown
复制代码
# GitHub Sentinel v0.0.1

## 发布日期

2024-11-04

## 主要功能

GitHub Sentinel 是一款专为开发者和项目管理人员设计的自动化工具，能够定期监控和汇总订阅的 GitHub 仓库动态。以下是 v0.0.1 版本的主要功能：

### 功能特性

1. **订阅管理模块**
   - 添加、删除和查看订阅仓库。
2. **更新获取模块**
   - 通过 GitHub API 获取订阅仓库的最新更新。
3. **通知模块**
   - 通过电子邮件或 Slack 通知用户最新的更新。
4. **报告生成模块**
   - 生成包含仓库动态的详细报告，便于项目管理。
5. **配置模块**
   - 支持 GitHub API token 和通知方式的配置。

### 文件结构

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

### 使用方法

- **配置**: 在 `config.py` 中设置 GitHub API Token 和通知方式。
- **运行**: 在项目目录下运行 `python main.py` 启动工具。

## 贡献者

感谢所有为 GitHub Sentinel 项目做出贡献的开发者！

---

此版本作为项目的初始版本，包含基础的订阅、更新、通知和报告功能，适用于简单的 GitHub 仓库动态跟踪。
