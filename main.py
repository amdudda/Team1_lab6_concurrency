'''
Cribbed threading code from https://pythonprogramming.net/threading-tutorial-python/
'''

import threading, time
from queue import Queue
from googleAPI import *

print_lock = threading.Lock()

def exampleJob(worker):
    time.sleep(.5) # pretend to do some work.
    with print_lock:
        # try to call another function inside exampleJob
        googleAPI(threading.current_thread().name,worker)

# The threader thread pulls an worker from the queue and processes it
def threader():
    while True:
        # gets an worker from the queue
        worker = q.get()

        # Run the example job with the avail worker in queue (thread)
        exampleJob(worker)

        # completed with the job
        q.task_done()

# Create the queue and threader
q = Queue()

# how many threads are we going to allow for
for x in range(10):
     t = threading.Thread(target=threader)

     # classifying as a daemon, so they will die when the main dies
     t.daemon = True

     # begins, must come after daemon definition
     t.start()

# record our start time
start = time.time()

# set up worker objects for googleAPI to process
items=[("one",1),"two","three","eins","zwei","drei","un","deux","trois","ena","dio","treis"]
# and queue them up for the 10 threads we set up
for worker in items:
    q.put(worker)

# wait until the thread terminates.
q.join()

# with 10 workers and 20 tasks, with each task being .5 seconds, then the completed job
# is ~1 second using threading. Normally 20 tasks with .5 seconds each would take 10 seconds.
print('Entire job took:',time.time() - start)