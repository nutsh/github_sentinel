import requests

class UpdateFetcher:
    def __init__(self, config):
        self.config = config

    def fetch_updates(self, subscriptions):
        updates = []
        headers = {"Authorization": f"token {self.config.github_token}"}
        for repo in subscriptions:
            response = requests.get(f"https://api.github.com/repos/{repo}/events", headers=headers)
            if response.status_code == 200:
                updates.append({"repo": repo, "events": response.json()})
        return updates
