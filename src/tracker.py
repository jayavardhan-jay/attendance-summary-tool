from collections import deque
import time

class AttendanceTracker:
    def __init__(self, max_size=5):
        self.summaries = deque(maxlen=max_size)

    def add_summary(self, summary):
        self.summaries.append({
            "created_at": time.time(),
            "summary": summary
        })

    def latest(self):
        if not self.summaries:
            return None
        return self.summaries[-1]["summary"]
