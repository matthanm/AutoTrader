from googlefinance import getQuotes
import json
import time
import threading

class ElectronicBroker(threading.Thread):
	def __init__(self, symbol):
		super(ElectronicBroker, self).__init__()
		self.symbol = symbol
	def run(self):
		while True:
			data = getQuotes(self.symbol)
			for item in data:
				print(item.get("LastTradeDateTime"))
				print(item.get("LastTradePrice"))
			time.sleep(5)