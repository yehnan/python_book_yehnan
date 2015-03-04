# -*- coding: utf-8 -*-
# 電影院賣票 10個售票員（窗口） 共150張票
# 每人負責15張
# future: 有些售票員動作較慢，也有可能他的客人動作較慢，讓動作快的人負責賣較多張的票
# future: 有些售票員可能突然肚子痛，關閉窗口；之後再回來賣票

import random
import time
from threading import Thread

print('main start')

numAgents = 10
numTickets = 150

random.seed()

def sellTickets(agentID, numTicketsToSell):
	while numTicketsToSell > 0:
		print('Agent ', agentID, ' sells a ticket ', numTicketsToSell)
		numTicketsToSell -= 1
		time.sleep(random.randrange(1, 3)) # simulating the time needed for selling a ticket
	print('Agent ', agentID, ' all down')

ts = []
for i in range(numAgents):
	t = Thread(target=sellTickets, args=(i, numTickets//numAgents))
	ts.append(t)

for i in range(numAgents):
	ts[i].start()

print('main end')

