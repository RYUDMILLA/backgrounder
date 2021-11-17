# import sys
# import time

# def spinning_cursor():
#     while True:
#         for cursor in '|/-\\':
#             yield cursor

# def spin_cursor(stop):
#     spinner = spinning_cursor()
#     while(stop == False):
#         sys.stdout.write(next(spinner))
#         sys.stdout.flush()
#         time.sleep(0.1)
#         sys.stdout.write('\b')



import sys
import time
import threading

class Spinner:
    busy = False
    delay = 0.1

    @staticmethod
    def spinning_cursor():
        while 1: 
            for cursor in '|/-\\': yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): 
            self.delay = delay

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def __enter__(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        self.busy = False
        time.sleep(self.delay)
        if exception is not None:
            return False

