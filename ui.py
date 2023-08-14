# ui.py

import tkinter as tk
from timer import Timer
from config import WORK_DURATION, SHORT_BREAK_DURATION, LONG_BREAK_DURATION, SESSIONS_BEFORE_LONG_BREAK

class FocusTimerApp:
    def __init__(self, timer, stats):
        self.timer = timer
        self.stats = stats

        self.window = tk.Tk()
        self.window.title("Focus Timer")

        self.timer_label = tk.Label(self.window, text="")
        self.timer_label.pack()

        self.stats_label = tk.Label(self.window, text="")
        self.stats_label.pack()

        self.start_button = tk.Button(self.window, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(self.window, text="Stop", command=self.stop_timer)
        self.stop_button.pack()

        self.timer.on_timer_start = self.on_timer_start
        self.timer.on_timer_stop = self.on_timer_stop
        self.timer.on_timer_finished = self.on_timer_finished

        self.update_timer_label()
        self.update_stats_label()

    def start_timer(self):
        self.timer.start()

    def stop_timer(self):
        self.timer.stop()

    def on_timer_start(self):
        print("Timer started!")

    def on_timer_stop(self):
        print("Timer stopped!")

    def on_timer_finished(self):
        print("Timer finished!")

    def update_timer_label(self):
        minutes, seconds = divmod(self.timer.current_time, 60)
        self.timer_label.config(text=f"{minutes:02}:{seconds:02}")
        self.window.after(1000, self.update_timer_label)  # Update the timer label every second

    def update_stats_label(self):
        stats = self.stats.get_stats()
        self.stats_label.config(text=f"Work Sessions: {stats['work_sessions']}, Short Breaks: {stats['short_breaks']}, Long Breaks: {stats['long_breaks']}")
        self.window.after(60000, self.update_stats_label)  # Update the stats label every minute

    def run(self):
        self.window.mainloop()
