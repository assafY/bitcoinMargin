def main():
	import dataGather
	bitcoinName = "XBTC"
	data = dataGather.get(bitcoinNam)
	import prediction
	expectation = prediction.flux(data)
	import chartMaker
	chart = chartMaker.makeChart(data, expectation)
	#Do something to print the chart
	#FANCY IOS MAGIC GOES HERE
if __name__ = "__main__":
	main()
