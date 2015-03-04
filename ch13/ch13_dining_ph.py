

import random
import time
import threading
from contextlib import contextmanager

# Thread-local state to stored information on locks already acquired
_local = threading.local()

@contextmanager
def acquire(*locks):
	# Sort locks by object identifier
	locks = sorted(locks, key=lambda x: id(x))
	# Make sure lock order of previously acquired locks is not violated
	acquired = getattr(_local, 'acquired', [])
	if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
		raise RuntimeError('Lock Order Violation')
	# Acquire all of the locks
	acquired.extend(locks)
	_local.acquired = acquired

	try:
		for lock in locks:
			lock.acquire()
		yield
	finally:
		# Release locks in reverse order of acquisition
		for lock in reversed(locks):
			lock.release()
		del acquired[-len(locks):]

# The philosopher thread
def philosopher(id, left, right):
    while True:
        with acquire(left, right):
            print(id, 'eating')
            time.sleep(random.random())
        print(id, 'thinking')
        time.sleep(random.random())

# The sticks (represented by locks)
num_sticks = 5
sticks_lock = [threading.Lock() for n in range(num_sticks)]

# Create all of the philosophers
for n in range(num_sticks):
    t = threading.Thread(target=philosopher,
                         args=(n, sticks_lock[n], 
                               sticks_lock[(n+1) % num_sticks]))
    t.start()


