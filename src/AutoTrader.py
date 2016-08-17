from ElectronicBroker import ElectronicBroker
import threading
import sys

__author__ = "Matthan Myers"
__copyright__ = "Copyright 2016, AutoTrader"
__credits__ = ["Matthan Myers"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Matthan Myers"
__email__ = "matthanmyers@gmail.com"
__status__ = "Experimental"

def main():
	print("\nWelcome to AutoTrader!\n### Created by " + __author__ + ", " + __copyright__ +
	".\n### Version " + __version__ +
	".\n### For questions, comments or suggestions, contact " + __maintainer__ + " at " + __email__ + ".\n-------------------\n\n")
	symbols = []
	with open('Symbols.cfg', 'r') as f:
		for line in f:
			symbols.append(line.split())
	stocks = []
	for symbol in symbols:
		stock = ElectronicBroker(symbol[0], symbol[1])
		stocks.append(stock)
		stock.start()
	print("All Electronic Brokers have been initialized.")

	while True:
		cmd = input("\nEnter a command: ")
		if cmd == "exit":
			for stock in stocks:
				stock.stop()
			print("Exiting program...")
			exit()
		elif cmd == "add":
			newSymbol = input("Enter a symbol and exchange to add: ").split()
			with open('Symbols.cfg', 'a') as f:
				f.write("\n" + newSymbol[0] + " " + newSymbol[1])
			newStock = ElectronicBroker(newSymbol[0], newSymbol[1])
			stocks.append(newStock)
			newStock.start()
		elif cmd == "rmv":
			rmvSymbol = input("Enter a symbol and exchange to remove: ").split()
			with open('Symbols.cfg', 'r') as f:
				lines = f.readlines()
			with open('Symbols.cfg', 'w') as f:
				for line in lines:
					if line != rmvSymbol[0] + " " + rmvSymbol[1] and line != "\n":
						f.write(line)
			for rmvStock in stocks:
				if rmvStock.symbol == rmvSymbol[0] and rmvStock.exchange == rmvSymbol[1]:
					rmvStock.stop()
					stocks.remove(rmvStock)
		else:
			print("\"" + cmd + "\"" + " is not a valid command.")

if __name__ == "__main__":
	main()