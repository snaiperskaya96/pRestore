from worker import Worker
from writer import Writer
from Queue import Queue


class Backup:
    def __init__(self, target, out, threads, verbose):
        if target[-1] != '/':
            target += '/'
        self.THREADS_LIMIT = threads
        self.queue = Queue()
        self.writer = Writer(out)
        self.writer.start()
        self.threads = []
        worker = Worker(target, self)
        self.threads.append(worker)
        worker.start()

        while len(self.threads) > 0 or not self.queue.empty():
            if len(self.threads) < self.THREADS_LIMIT and not self.queue.empty():
                new_dir = self.queue.get()
                if new_dir is not None:
                    thread = Worker(new_dir, self)
                    self.threads.append(thread)
                    thread.start()
            for thread in self.threads:
                if thread.done:
                    self.threads.remove(thread)

        while not self.writer.queue.empty():
            pass

        for thread in self.threads:
            thread.join()

        self.writer.stop()
        self.writer.join()

        print "Done"

    def on_thread_finished(self, thread):
        try:
            self.threads.remove(thread)
        except:
            print 'cant '

    def add_to_queue(self, directory):
        self.queue.put(directory + '/')

    def write(self, f):
        self.writer.add(f)


