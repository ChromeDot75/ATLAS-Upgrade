import uproot
from collections.abc import Mapping
import numpy as np
import matplotlib.pyplot as plt
import mplhep

file = uproot.open("N:\Year 4\Main Project\Preliminary Results\W3_Run_63\data\strun60_63.root")


#print(file)

#print(file.keys())

#isinstance(file, Mapping)
classnames_list = list(file.classnames())

#print(classnames_list[1])

#print(file.keys())

keys_l = list(file.keys())
#print(keys_l[1])

strobe_delay = uproot.open("N:\Year 4\Main Project\Preliminary Results\W3_Run_63\data\strun63_3.root")

strobe_delay_l = list(strobe_delay.classnames())


print(strobe_delay.classnames(filter_classname="*a*"))
print(strobe_delay.classnames(filter_classname='*h_scan*'))

