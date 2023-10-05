import time
import threading

class ProfileDecorator:
    def __init__(self, func):
        self.func = func
        self.lock = threading.Lock()
        self.calls = 0
        self.totalTime = 0

    def __call__(self, *args, **kwargs):
        startTime = time.time()
        result = self.func(*args, **kwargs)
        endTime = time.time()

        with self.lock:
            self.calls += 1
            self.totalTime += endTime - startTime

        return result

    def get_stats(self):
        with self.lock:
            return self.calls, self.totalTime
        
    def clear_stats(self):
        with self.lock:
            self.calls = 0
            self.totalTime = 0