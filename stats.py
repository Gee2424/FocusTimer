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
            self.save_stats()

    def save_stats(self):
        with open(self.stats_file, "w") as f:
            json.dump(self.stats, f)

    def increment_counter(self, counter_name):
        if counter_name in self.stats:
            self.stats[counter_name] += 1
            self.save_stats()

    def increment_work_sessions(self):
        self.increment_counter("work_sessions")

    def increment_short_breaks(self):
        self.increment_counter("short_breaks")

    def increment_long_breaks(self):
        self.increment_counter("long_breaks")

    def get_stats(self):
        return self.stats

# Usage example
if __name__ == "__main__":
    stats = Stats()
    stats.increment_work_sessions()
    stats.increment_short_breaks()
    stats.increment_long_breaks()
    print(stats.get_stats())
