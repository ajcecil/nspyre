# nspyre - Run python modules/commands on your nspire
module for TI-nspire cx II/TI-nspire cx II CAS or other TI calculators runing python

## [Statistics](https://github.com/ajcecil/nspyre/blob/main/python/nspyre.py)
The first function group in this module is geared towards statistics with many commonly used equations and opperations used in statistical analysis.

### Current available functions:
Opperation|Function|Output
----------|--------|-----
Mean/Average|mean(data)|mean
Median|median(data)|median
Confidence|confidence(error_rate)|coefficient of confidence
Five Number Summary|fivenum(data)|minimum, q1, q2, q3, maximum
SampleVariance|s_variance(data)|sample variance
Standard Deviation| stnd_dev(data)|standard deviation
Confidence Interval|con_int(data, mu)| T value
Solving for Mu|solve_mu(data, T)| mu_lower, mu_upper

This project should continure to expand and grow with changes in structure to optimize usage on an nspire or other devices with memory and storage limitations.


## [Installation](https://github.com/ajcecil/nspyre/tree/main/ti-files)
To install the module download [nspyre_compiler.tns](https://github.com/ajcecil/nspyre/blob/main/ti-files/nspyre_compiler.tns) to you calculator then on the calculator open the file and go to Menu -> Actions -> Install as Python module (Or menu -> 1 -> 7)

## Accessing nspyre module
To access the module open a python file on the calculator and go to menu -> More Modules (menu -> A) and you should see the nspyre module as an option on the list. If you select the module from this list the calculator auto-imports all functions in the module, using:
```python
from nspyre import *
```
Functions from the module can then be referenced as shown below:
``` python
data = [2,5,3,8,3]
median(data)
```

To import the statistics functions alone, the above statement can be modified to:
```python
from nspyre import statistics
```

with the import of the one group of functions the calculators memory is under less load, but each function must be referenced as shown below:
``` python
data = [2,5,3,8,3]
statistics.median(data)
```

This can be made easier with a shortcut value:
``` python
stat = statistics()
data = [2,5,3,8,3]
stat.median(data)
```
