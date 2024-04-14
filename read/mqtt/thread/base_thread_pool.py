from concurrent.futures.thread import ThreadPoolExecutor


class BaseThreadPool:

    def __init__(self, max_thread: int, prefix: str):
        self.max_thread = max_thread
        self.prefix = prefix
        self.thread_pool = ThreadPoolExecutor(max_workers=self.max_thread, thread_name_prefix=self.prefix)

    def get_thread_pool(self):
        return self.thread_pool
