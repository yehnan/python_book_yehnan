

import random
import time
from threading import Thread, Lock

num_agents = 10
num_tickets = [100]

def sell_tickets(agent_id, nt, lock):
    total = 0
    while True:
        with lock:
            if nt[0] > 0:
                print('Agent %d sells a ticket No. %d' % (agent_id, nt[0]))
                nt[0] -= 1
                total += 1
            elif nt[0] == 0:
                break;
        #time.sleep(random.randrange(1, 3))
        time.sleep(random.random() * (1 + agent_id/2))
    print('Agent %d done. Totally sells %d tickets' % (agent_id, total))

lock = Lock()
for i in range(num_agents):
    t = Thread(target=sell_tickets, args=(i, num_tickets, lock))
    t.start()

