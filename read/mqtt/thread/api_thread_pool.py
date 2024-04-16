from time import sleep
from threading import Thread
import Queue


class DispatcherThread(Thread):

    def __init__(self, *args, **kwargs):
        super(DispatcherThread, self).__init__(*args, **kwargs)
        self.interested_threads = []

    def run(self):
        while 1:
            if some_condition:
                self.dispatch_message(some_message)
            else:
                sleep(0.1)

    def register_interest(self, thread):
        self.interested_threads.append(thread)

    def dispatch_message(self, message):
        for thread in self.interested_threads:
            thread.put_message(message)


class WorkerThread(Thread):

    def __init__(self, *args, **kwargs):
        super(WorkerThread, self).__init__(*args, **kwargs)
        self.queue = Queue()

    def run(self):
        # Tell the dispatcher thread we want messages
        dispatcher_thread.register_interest(self)

        while 1:
            # Wait for next message
            message = self.queue.get()

            # Process message
            # ...

    def put_message(self, message):
        self.queue.put(message)


dispatcher_thread = DispatcherThread()
dispatcher_thread.start()

worker_threads = []
for i in range(10):
    worker_thread = WorkerThread()
    worker_thread.start()
    worker_threads.append(worker_thread)

dispatcher_thread.join()
