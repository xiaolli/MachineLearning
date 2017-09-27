import queue
import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadId, name, q):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.q = q

    def run(self):
        print('start thread:' + self.name)
        print_data(self.name, self.q)
        print('end thread:' + self.name)


def print_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print('%s processing %s' % (threadName, data))
        else:
            queueLock.release()

        time.sleep(1)


threadList = ['thread1', 'thread2', 'thread3']
nameList = ['one', 'two', 'three', 'four', 'five']
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadId = 1

for tName in threadList:
    thread = myThread(threadId, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadId += 1

queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

while not workQueue.empty():
    pass

exitFlag = 1

for t in threads:
    t.join()

print('exit main thread!')
