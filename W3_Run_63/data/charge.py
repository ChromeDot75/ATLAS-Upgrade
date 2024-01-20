import uproot


fh = uproot.open(r"N:\CERN\W3_Run_63\data\strun63_3.root")

charge = int(float(fh['configuration/module_5/chip_4/Calibration voltage']))

print(charge)