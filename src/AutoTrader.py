from ElectronicBroker import ElectronicBroker
import threading

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
	f = open('Symbols.txt', 'r')
	symbols = f.read().split()
	stocks = []
	for symbol in symbols:
		stock = ElectronicBroker(symbol)
		stocks.append(stock)
		print("Starting thread for " + symbol + "...")
		stock.start()

if __name__ == "__main__":
	main()