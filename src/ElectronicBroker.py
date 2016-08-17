from googlefinance import getQuotes
import json
import time
import threading

class ElectronicBroker(threading.Thread):
	def __init__(self, symbol, exchange):
		print("Initializing an Electronic Broker for " + symbol + "...")
		super(ElectronicBroker, self).__init__()
		self.symbol = symbol
		self.exchange = exchange
		self.isRunning = True
	def run(self):
		while self.isRunning:
			data = getQuotes(self.exchange + ":" + self.symbol)
			with open("StockData/" + self.exchange + "." + self.symbol + "-" + time.strftime("%m.%d.%y") + ".dat", "a") as f:
				for item in data:
					f.write(item.get("LastTradeDateTime") + " " + item.get("LastTradePrice") + "\n")
			time.sleep(5)
	def stop(self):
		print("Stopping an Electronic Broker for " + self.symbol + "...")
		self.isRunning = False