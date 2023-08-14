# stats.py
import json


class Stats:
    def __init__(self, stats_file="stats.json"):
        self.stats_file = stats_file
        self.stats = {"work_sessions": 0, "short_breaks": 0, "long_breaks": 0}
        self.load_stats()

    def load_stats(self):
        try:
            with open(self.stats_file, "r") as f:
                self.stats = json.load(f)
        except FileNotFoundError:
            self.save_stats()  # Create a new stats file if it doesn't exist

    def save_stats(self):
        with open(self.stats_file, "w") as f:
            json.dump(self.stats, f)

    def increment_work_sessions(self):
        self.stats["work_sessions"] += 1
        self.save_stats()

    def increment_short_breaks(self):
        self.stats["short_breaks"] += 1
        self.save_stats()

    def increment_long_breaks(self):
        self.stats["long_breaks"] += 1
        self.save_stats()

    def get_stats(self):
        return self.stats
