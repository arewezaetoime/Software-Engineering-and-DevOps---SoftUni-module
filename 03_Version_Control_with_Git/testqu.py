import threading
import queue
import timeit


time = timeit.timeit()
que = queue.Queue()

def worker():
    while True:
        item = que.get()
        print(f'working on the item: {item}')
        # print('Finished processing')
        que.task_done()

# Turn-on the worker thread.
threading.Thread(target=worker, daemon=True).start()

# Send thirty task requests to the worker.
for item in range(30):
    que.put(item)

# Block until all tasks are done.
que.join()
print('All work completed')

print(time)

# time2 = time.timeit()

# for _ in range(30):
#     print('sasa')

# print(time2)