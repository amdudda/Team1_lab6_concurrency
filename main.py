'''
Cribbed threading code from https://pythonprogramming.net/threading-tutorial-python/
Modified threading code for use in this project.
'''

import threading, time
from queue import Queue
from googleAPI import *
import apikeys as AK
from storePics import savePic

print_lock = threading.Lock()
result_array=[]

def downloadImages(worker):
    imageurl = googleAPI(*worker)  # the asterisk unpacks the tuple into a list of arguments
    with print_lock:
        # try to call another function inside exampleJob
        print(imageurl)
        result_array.append(imageurl)
        savePic(*imageurl)



# The threader thread pulls an worker from the queue and processes it
def threader():
    while True:
        # gets an worker from the queue
        worker = q.get()

        # Run the example job with the avail worker in queue (thread)
        downloadImages(worker)

        # completed with the job
        q.task_done()

# Create the queue and threader
q = Queue()

# how many threads are we going to allow for? ten for now.
for x in range(10):
     t = threading.Thread(target=threader)

     # classifying as a daemon, so they will die when the main dies
     t.daemon = True

     # begins, must come after daemon definition
     t.start()

# record our start time
start = time.time()

# set up worker objects for googleAPI to process
items=[("HONY",AK.GCS_ID_HONY),("Bustos", AK.GCS_ID_BUSTOS),("Pixabay",AK.GCS_ID_PIXABAY)]
# and queue them up for the 10 threads we set up
for worker in items:
    q.put(worker)

# wait until the thread terminates.
q.join()

# with 10 workers and 20 tasks, with each task being .5 seconds, then the completed job
# is ~1 second using threading. Normally 20 tasks with .5 seconds each would take 10 seconds.
print(result_array)
# print('Entire job took:',time.time() - start)