# main.py
import tkinter as tk
from tkinter import messagebox
from timer import Timer
from config import WORK_DURATION, SHORT_BREAK_DURATION, LONG_BREAK_DURATION, SESSIONS_BEFORE_LONG_BREAK
from stats import Stats
from ui import FocusTimerApp

# Function to handle events
def on_timer_start():
    print("Timer started!")
    stats.increment_work_sessions()

def on_timer_stop():
    print("Timer stopped!")

def on_timer_finished():
    print("Timer finished!")

def start_button_click():
    if messagebox.askokcancel("Focus Timer", "Ready to focus for 25 minutes?"):
        timer.start()

# Create an instance of Timer with callback functions
timer = Timer(work_time=WORK_DURATION, short_break_time=SHORT_BREAK_DURATION, long_break_time=LONG_BREAK_DURATION)
timer.on_timer_start = on_timer_start
timer.on_timer_stop = on_timer_stop
timer.on_timer_finished = on_timer_finished

# Create an instance of Stats to track user's progress
stats = Stats()

# Create the main application window
app = FocusTimerApp(timer, stats)

# Assign the start button click handler
app.start_button['command'] = start_button_click

# Start the application
app.run()
