import areaConverter
import weightConverter
import volumeConverter

def convert(currentUnits, fromTo, localUnit, metricUnit, valueToBeConverted):
	returnValue = 0
	functionString = "" 
	if fromTo == "Local To Metric":
		if metricUnit == "Acres":
			valueToBeConverted = valueToBeConverted / 2.47105381
			metricUnit = "Hectares"
		else:
			pass
		functionString = "convert" + localUnit + "To" + metricUnit	
	elif fromTo == "Metric To Local":	
		functionString = "convert" + metricUnit + "To" + localUnit
	else:
		pass
	functionString = "".join(functionString.split())
	if currentUnits.lower() == "area":
		returnValue = getattr(areaConverter, functionString)(float(valueToBeConverted))
	elif currentUnits.lower() == "weight":
		returnValue = getattr(weightConverter, functionString)(float(valueToBeConverted))
	elif currentUnits.lower() == "volume":
		returnValue = getattr(volumeConverter, functionString)(float(valueToBeConverted))
	else:
		pass
	return returnValue

if __name__ == "__main__":
	localUnit = "MuriMato"
	metricUnit = "Hectares"
	valueToBeConverted = 1
	fromTo = "Metric To Local"
	currentUnits = "area" #can be Area, Weight or Volume
	print convert(currentUnits, fromTo, localUnit, metricUnit, valueToBeConverted)
