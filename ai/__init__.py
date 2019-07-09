print('\033[92mimport pandas as pd\033[0m')
print('\033[92mimport sklearn\033[0m')
print('\033[92mimport numpy as np\033[0m')
import pandas
globals()['pd'] = pandas
__import__('pandas', globals(), locals())
import sklearn
globals()['sklearn'] = sklearn
import numpy
globals()['np'] = numpy

