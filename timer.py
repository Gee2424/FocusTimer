import time
import threading

class Timer:
    def __init__(self, work_time=25 * 60, short_break_time=5 * 60, long_break_time=15 * 60):
        self.work_time = work_time
        self.short_break_time = short_break_time
        self.long_break_time = long_break_time
        self.is_running = False
        self.current_time = 0
        self.on_timer_start = None
        self.on_timer_stop = None
        self.on_timer_finished = None

    def start(self):
        if not self.is_running:
            self.is_running = True
            if self.on_timer_start:
                self.on_timer_start()
            threading.Thread(target=self._run_timer).start()

    def stop(self):
        if self.is_running:
            self.is_running = False
            if self.on_timer_stop:
                self.on_timer_stop()

    def _run_timer(self):
        self.current_time = self.work_time
        while self.current_time > 0 and self.is_running:
            time.sleep(1)
            self.current_time -= 1
        if self.is_running and self.on_timer_finished:
            self.on_timer_finished()

# Usage example
if __name__ == "__main__":
    def on_start():
        print("Timer started!")

    def on_stop():
        print("Timer stopped!")

    def on_finish():
        print("Timer finished!")

    timer = Timer()
    timer.on_timer_start = on_start
    timer.on_timer_stop = on_stop
    timer.on_timer_finished = on_finish

    timer.start()
    time.sleep(10)  # Simulate the timer running for 10 seconds
    timer.stop()
