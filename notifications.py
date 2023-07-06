# notifications.py
from plyer import notification

def notify_timer_start():
    notification.notify(
        title="Focus Timer",
        message="Your focus session is starting now. Time to work!",
        timeout=10
    )

def notify_timer_end():
    notification.notify(
        title="Focus Timer",
        message="Your focus session has ended. Time for a break!",
        timeout=10
    )

def notify_break_end():
    notification.notify(
        title="Focus Timer",
        message="Your break has ended. Time to get back to work!",
        timeout=10
    )
