import threading
import time

class MyThread(threading.Thread):
    def __init__(self, target, pause_event, cancel_event):
        super().__init__()
        self.target = target
        
        self.pause_event = pause_event
        self.cancel_event = cancel_event

    def run(self):
        
        while not self.cancel_event.is_set():
            while self.pause_event.is_set():
                print("Thread Paused")
            print("Thread is running")
            # time.sleep(5)
            return self.target()

        print("Thread cancelled")

    def pause(self):
        self.pause_event.set()

    def resume(self):
        self.pause_event.clear()

    def cancel(self):
        self.cancel_event.set()

if __name__ == "__main__":
    pause_event = threading.Event()
    cancel_event = threading.Event()
    thread = MyThread(pause_event, cancel_event)
    thread.start()

    time.sleep(5)  # Let the thread run for 5 seconds
    thread.pause()

    print("Thread paused for 3 seconds")
    time.sleep(3)  # Pause for 3 seconds

    thread.resume()

    time.sleep(5)  # Let the thread run for another 5 seconds
    thread.cancel()
