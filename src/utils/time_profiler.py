from time import time


class SimpleTimer:
    def __enter__(self):
        self.start_time = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'{self.msg}: {time() - self.start_time}s')

    def __init__(self, msg=''):
        self.start_time = None
        self.end_time = None
        self.duration = None
        self.msg = msg

    def tic(self):
        self.start_time = time()

    def toc(self):
        self.end_time = time()
        self.duration = self.end_time - self.start_time
        return self.duration
