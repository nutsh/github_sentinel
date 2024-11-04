class ReportGenerator:
    def __init__(self, config):
        self.config = config

    def generate_report(self, updates):
        report = "GitHub Sentinel Report:\n"
        for update in updates:
            report += f"Repository: {update['repo']}\n"
            for event in update["events"]:
                report += f"- {event['type']} by {event['actor']['login']}\n"
        return report
