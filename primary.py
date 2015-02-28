def main():
	import dataGather
	bitcoinName = "XBTC"
	data = dataGather.get(bitcoinName)
	import prediction
	expectation = prediction.flux(data)
	import chartMaker
	chart = chartMaker.makeChart(data, expectation)
	#Do something to print the chart

if __name__ = "__main__":
	main()
