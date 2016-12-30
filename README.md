# Nepali Units Converter

Python scripts that allow for conversion among legacy based local Nepali units of area, volume and weight to metric units and among themselves and vice versa.

The formulas used if obtained from Nepal Rastra Bank, Agriculture Survey Report, 1972 where the formula is given comprehensively.

These set of scripts are created as an archive of the formula as no other comprehensive conversion script seem available.

These formulas have been used in agriculture related applications.


### How it is arranged :
- formulas.py -- all weights that are required for conversion
- areaConverter.py -- formulas for area conversion
- volumeConverter.py -- formulas for volume conversion
- weightConverter.py -- formulas for weight conversion

The scripts to use the formulas :
- nepaliUnitConverter.py -- commandline script to convert 
- converter.py -- a basic wx based gui for conversions

###Usage :
One can either edit the nepaliUnitConverter.py file, make necessary changes to the following code at the bottom of the file:
localUnit = "MuriMato"
metricUnit = "Hectares"
valueToBeConverted = 1
fromTo = "Metric To Local" #can be Metric to Local, Local to Metric
currentUnits = "area" #can be Area, Weight or Volume
and run the script

or 

one can run the GUI and do the conversions there

###DISCLAIMER
I have not put too much effort into this to be used as a working application, rather worked on it on the part of preserving the formulas and the weights as well as to provide a simple documentation of local units used for area, weight and volume. So the application itself is rusty for use.