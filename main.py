from worker import Worker
from writer import Writer
from Queue import Queue


class MainClass():
    def __init__(self):
        THREADS_LIMIT = 5
        self.queue = Queue()
        self.writer = Writer()
        self.writer.start()
        self.threads = []
        worker = Worker('/', self)
        self.threads.append(worker)
        worker.start()

        while len(self.threads) > 0 or self.queue.qsize() > 0:
            if len(self.threads) < THREADS_LIMIT:
                new_dir = self.queue.get()
                thread = Worker(new_dir, self)
                self.threads.append(thread)
                thread.start()

        while self.writer.queue.qsize() > 0:
            pass

        self.writer.got_to_run = False

        print "Done"

    def on_thread_finished(self, thread):
        try:
            self.threads.remove(thread)
        except:
            pass

    def add_to_queue(self, directory):
        self.queue.put(directory + '/')

    def write(self, file):
        self.writer.add(file)


if __name__ == '__main__':
    MainClass()
